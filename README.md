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

## Visualization

The time series representation of the download data can be seen below. It is clear the the data has a seasonal component, with a peak in the summer months and a trough in the winter months. Moreover, the data seems to have a trend, with a longer term pattern, with a descrease followed by an increase and then another decrease due to covid lockdowns.

![timeseries representation of data per `accident type`](imgs/timeseries.png)

Another way of observing such patterns is through a seasonal decomposition, which can be observed below. The seasonal component is clear, as well as the trend component. Moreover, the residuals seem to be stationary, which is a good sign for modelling.

![seasonal decompose of `total` `accident type`](imgs/seasonal_decompose.png)
## Step by Step Instructions 

### Running Locally

```bash
conda create -n dpsenv
conda activate dpsenv
# conda env export > environment.yml
conda env update --file environment.yml
```

### Running on AWS

```bash
# example extracted from SSH connect EC2 page 
ssh -i "dps.pem" ec2-user@ec2-52-201-231-31.compute-1.amazonaws.com
sudo yum -y install docker
# from https://stackoverflow.com/a/65478517/14403987
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose version
# from https://github.com/moby/moby/issues/17645#issuecomment-153291483
sudo su -
service docker start
docker images
logout # su ec2-user
docker-compose up
```