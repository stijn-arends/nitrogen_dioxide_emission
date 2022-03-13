# The effect of a lockdown on the nitrogen dioxide emission in the Netherlands
Studying the effect of the lockdowns that were initiated due to the corona pandemic on the emission of nitrogen dioxide (NO2) in the Netherlands. 

[![Python version](https://img.shields.io/badge/python-3-blue)](https://www.python.org/download/releases/3.0/)
[![panel](https://img.shields.io/badge/Python%20package-panel-brightgreen)](https://panel.holoviz.org/)
[![bokeh](https://img.shields.io/badge/Python%20package-bokeh-brightgreen)](https://bokeh.org/)  


<img src="https://github.com/stijn-arends/nitrogen_dioxide_emission/blob/main/imgs/dashboard_NO2_gif.gif" alt="dashboardGIF" height="500" width="100%">


* * *
## Research question

* Did the lockdown have an effect on the NO2 emission in the Netherlands?


* * *
## Description 

This project studies the effect of the lockdowns that were initiated due to the corona pandemic on the nitrogen dioxide (NO2) emission in the Netherlands. NO2 emission data was used from several stations that are spread all over the Netherlands from the year 2020 and 2021. 

Two different maps were created to show the NO2 emission in the Netherlands with the use of [folium](https://python-visualization.github.io/folium/). For one map the NO2 emission is displayed for each station for a date that can be selected by the user, it also displays if the selected date was during a lockdown or not. The second map displays the NO2 emission over time. In addition to this, a plot was created to show the NO2 emission in a line graph. The user can then select a station of intereset plus the date of interest. The date can be modified using a date range slider. 

These different plots were cobined to create a dashboard about NO2 emission in the Netherlands. The dashboard was created using [panel](https://panel.holoviz.org/) and [bokeh](https://bokeh.org/).
<br/><br/>

* * *
## Data

### Source

* NO2 emission data: https://data.rivm.nl/data/luchtmeetnet/ 
  * Date accessed: 12-03-2022 
* Covid data: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
  * Date accessed: 12-03-2022 
* geojson data the Netherlands: https://www.webuildinternet.com/2015/07/09/geojson-data-of-the-netherlands/
  * Date accessed: 12-03-2022  

### Data description
A full description of the NO2 emission data format can be found in the [`docs/data_format_explained.md`](docs/data_format_explained.md) file.

### Downloading the data

#### NO2

The NO2 emission data that is used for this project can be automatically downloaded using a python script called [`download_data.py`](scripts/download_data.py).

> NOTE: this script will be logged and the output is stored in a folder called `logs` which will be created in the `scripts/` folder.

Example:

```bash
  python download_data.py -c config.yaml
```

> NOTE: [config.yaml](config.yaml) contains information about where the data should be stored and which urls need to be used to download the data.

Information about the script and how to use it can be aquired using the help argument:

```bash
  python download_data.py -h
```  

#### COVID and geojson

To download the COVID and geojson data please use the links provided in the [data source](#source) section.
<br/><br/>


* * *
## Installation


### Single install
The easiest way to install all the required packages is via conda. How to install conda on your system can be found [here](https://docs.anaconda.com/anaconda/install/index.html).

To create a new environment which contains all the required packages plus the right version run the following code:

```bash
  conda env create -f environment.yaml
```

This will create a new environment named `DSLS_prog_final` which can be used to run the code for this project.

> NOTE: the environment.yaml is located in the install/ directory [here](install/environment.yaml).

### Multiple installs
An other option is to install each package seperately, either with conda or pip.

conda:
```bash
  conda install <PACKAGE>=<VERSION>
```

pip
```bash
  pip install <PACKAGE>==<VERSION>
```

> NOTE: make sure to use the correct versions, which are listed [here](#packages).

* * *
## Getting started

### Running the notebook. 

The notebook contains the code for the analysis as well as the code to create the dashboard. It also contains a table of contents that can be used to navigate to a particular part, for example the code for the dashboard. 

The configuration file, which is described below, needs to be filled in to be able to run the [notebook](NO2_emission_corona.ipynb). Besides that, the notebook should be run from top to bottom to make sure that no erros occur. 

> NOTE: jupyter itself has to be launched first

### Configuration file

A configuration file, called [config.yaml](config.yaml), is used for this project to download the data and to analyze the data.
It stores information about where the data is stored, and from which URL the data needs to be downloaded from.

Example:
```YAML

# Location to store the data. 
# ../ is used because the script that downloads the data is located in the script/ folder.
datadir: '../data/'
geojson: 'data/provinces.geojson'
covid_data: "data/time_series_covid19_confirmed_global.csv"
urls: {
  "2020": "https://data.rivm.nl/data/luchtmeetnet/Vastgesteld-jaar/2020/",
  "2021": "https://data.rivm.nl/data/luchtmeetnet/Actueel-jaar/"
}

# Location of the data directory 
data: './data/'

```

* * *
## Justifying my actions

The [justification_choices_made.md](docs/justification_choices_made.md) file explains the choices that were made during this project. 


* * *
## Requirements

| Software                          | Version  |
| --------------------------------- | :------: |
| [Python](https://www.python.org/) | `3.9.7`  |

* * *
## Packages

| Package                                                           | Version        |
| ----------------------------------------------------------------- | :------------: |
| [bokeh](https://bokeh.org/)                                       | `2.4.2`        |
| [branca](https://pypi.org/project/branca/)                        | `0.4.2`        |
| [bs4](https://beautiful-soup-4.readthedocs.io/en/latest/)         | `4.10.0`       |
| [folium](https://python-visualization.github.io/folium/)          | `0.12.1.post1` |
| [holoviews](https://holoviews.org/)                               | `1.14.8`       |
| [hvplot](https://hvplot.holoviz.org/)                             | `0.7.3`        |
| [jupyter](https://jupyter.org/)                                   | `1.0.0`        |
| [numpy](https://numpy.org/)                                       | `1.21.5`       |
| [pandas](https://pandas.pydata.org/)                              | `1.4.1`        |
| [panel](https://panel.holoviz.org/)                               | `0.12.6`       |
| [pathlib](https://pathlib.readthedocs.io/en/0.5/l)                | `1.0.1`        |
| [pyyaml](https://pyyaml.org/)                                     | `6.0`          |
| [regex](https://docs.python.org/3/library/re.html)                | `2021.8.3`     |
| [requests](https://docs.python-requests.org/en/master/index.html) | `2.27.1`       |
| [scikit-learn](https://scikit-learn.org/stable/index.html)        | `1.0.2`        |
| [scipy](https://scipy.org/)                                       | `1.7.3`        |
| [statsmodel](https://www.statsmodels.org/stable/index.html)       | `0.13.0`       |
| [tqdm](https://pypi.org/project/tqdm/)                            | `4.62.3`       | 

* * *
## License

This project contains a MIT [license](./LICENSE.md)

* * *
## Author

Stijn Arends  
Student master Data Science for Life Sciences  
Hanze University of Applied Sciences  
11-03-2022
