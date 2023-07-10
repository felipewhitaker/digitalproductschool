from datetime import datetime

import pandas as pd
from dateutil.relativedelta import relativedelta
from sklearn.base import BaseEstimator


def create_timeindex(end_date: datetime, n_steps: int) -> pd.DatetimeIndex:
    # FIXME assumes monthly data
    return pd.date_range(
        start=end_date + relativedelta(months=1), periods=n_steps, freq="MS"
    )


class NamedModel:
    @property
    def name(self):
        return f"{self.__class__.__name__}"
    
class StatsInterface:

    def forecast(self, steps: int):
        return self.predict(steps)


class Persistence(BaseEstimator, NamedModel, StatsInterface):
    def __init__(self) -> None:
        super().__init__()
        self.last_value = None

    def fit(self, X, y=None):
        # FIXME assert X index is datetime
        self.last_value = X.iloc[-1]
        self.end_date = X.index[-1]
        return self

    def predict(self, n_steps: int) -> pd.Series:
        # FIXME assumes monthly data
        return pd.Series(
            [self.last_value] * n_steps,
            index=create_timeindex(self.end_date, n_steps),
            name=self.name,
        )


class Average(BaseEstimator, NamedModel, StatsInterface):
    def __init__(self, window: int) -> None:
        super().__init__()
        self.window = window

    def fit(self, X, y=None):
        self.data = X.iloc[-self.window :]
        self.end_date = X.index[-1]
        return self

    def predict(self, n_steps: int) -> pd.Series:
        index = create_timeindex(self.end_date, n_steps)
        return pd.Series(
            [self.data.mean()] * n_steps, index=index, name=self.name
        )


class Seasonal(BaseEstimator, NamedModel, StatsInterface):
    def __init__(self, freq: int) -> None:
        super().__init__()
        self.freq = freq

    def fit(self, X, y=None):
        self.data = X.iloc[-self.freq :]
        self.end_date = X.index[-1]
        return self

    def predict(self, n_steps: int) -> pd.Series:
        index = create_timeindex(self.end_date, n_steps)
        return pd.Series(
            [self.data[i % self.freq] for i in range(n_steps)],
            index=index,
            name=self.name,
        )
