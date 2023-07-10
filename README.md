# Digital Product School Challenge

[Digital Product School (DPS)](https://www.digitalproductschool.io/) is a 3 months training program to empower the next generation of digital product makers, where diverse and cross-functional teams solve real-world challenges.

This repository contains what I developed as the AI Track challenge. The challenge is to predict the `total` number of accidents (under `accident_type`) in Munich for the year of 2020.

## Data

> The monthly traffic accidents data set includes: traffic accidents, escape accidents and alcohol accidents.

The dataset used can be both explored online and downloaded via [dataset](https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7).

As the quote indicates, this data represents traffic accidents. Although there are other columns in the dataset, only the first five columns were considered: `category`, `accident_type`, `year`, `month` and `value`.

Moreover, to make it easier for non-german speakers to understand, the values in the columns `category` and `accident_type` were translated considering the following dictionary:

```python
category_map = {
    "Alkoholunfälle": "alcohol",
    "Fluchtunfälle": "escape",
    "Verkehrsunfälle": "traffic"
}

accident_type = {
    "insgesamt": "total",
    "Verletzte und Getötete": "injured_or_killed",
    "mit Personenschäden": "personal_injury"
}
```

Finally, these transformations result in the data dictionary below:

| Column        | type    | description                                                     |
|---------------|---------|-----------------------------------------------------------------|
| category      | text    | one of ("alcohol", "escape", "traffic")                         |
| accident_type | text    | one of ("total", "injured_or_killed", "personal_injury")        |
| year          | numeric | data from 2000-2022                                             |
| month         | text    | either `Summe` (total) or ends with two digit month (e.g. `03`) |
| value         | numeric | number of registered occurances                                 |

## Step by Step Instructions 

```bash
conda create -n dpsenv
conda activate dpsenv
# conda env export > environment.yml
conda env update --file environment.yml
```
