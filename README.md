# The effect of a lockdown on the nitrogen dioxide emission in the Netherlands
Studying the effect of the number of corona cases and the lockdowns on the emission of nitrogen dioxide

* * *
## Description 
* * *

### Data

### Source

* NO2 emission data: https://data.rivm.nl/data/luchtmeetnet/ 
* Covid data: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
* geojson data the Netherlands: https://www.webuildinternet.com/2015/07/09/geojson-data-of-the-netherlands/

### Data description
A full description of the NO2 emission data format can be found in the [`docs/data_format_explained.md`](docs/data_format_explained.md) file.  

* * *
## Installation
* * *

### Single install
The easiest way to install all the required packages is via conda. How to install conda on your system can be found [here](https://docs.anaconda.com/anaconda/install/index.html).

To create a new environment which contains all the required packages plus the right version run the following code:

```bash
  conda env create -f environment.yml
```

This will create a new environment named `DSLS_prog_final` which can be used to run the code for this project.

> NOTE: the environment.yml is located in the install/ directory [here](install/environment.yaml).

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
* * *

### Configuration file

A configuration file, called [config.yaml](config.yaml), is used for this project to download the data and to analyze the data.
It stores information about were the data is stored, and from which URL the data needs to downloaded from.

Example:
```YAML

datadir: 'data/'
urls: {
  "2020": "https://data.rivm.nl/data/luchtmeetnet/Vastgesteld-jaar/2020/",
  "2021": "https://data.rivm.nl/data/luchtmeetnet/Actueel-jaar/"
}
```

### Downloading the data

The data that is used for this project can be automatically downloaded using a python script called [`download_data.py`](scripts/download_data.py).

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

* * *
## Requirements
* * *
| Software                          | Version  |
| --------------------------------- | :------: |
| [Python](https://www.python.org/) | `3.9.7`  |  


* * *
## Packages
* * *
| Package                                                           | Version      |
| ----------------------------------------------------------------- | :----------: |
| [numpy](https://numpy.org/)                                       | `1.21.2`     |
| [pandas](https://pandas.pydata.org/)                              | `1.3.3`      |
| [bokeh](https://bokeh.org/)                                       | `2.3.3`      |
| [panel](https://panel.holoviz.org/)                               | `0.12.1`     |
| [holoviews](https://holoviews.org/)                               | `1.14.6`     |
| [hvplot](https://hvplot.holoviz.org/)                             | `0.7.3`      |
| [scipy](https://scipy.org/)                                       | `1.7.1`      |
| [jupyter](https://jupyter.org/)                                   | `1.0.0`      |
| [pyyaml](https://pyyaml.org/)                                     | `6.0`        |
| [pathlib](https://pathlib.readthedocs.io/en/0.5/l)                | `1.0.1`      |
| [requests](https://docs.python-requests.org/en/master/index.html) | `2.27.1`     |
| [bs4](https://beautiful-soup-4.readthedocs.io/en/latest/)         | `4.10.0`     |
| [statsmodel](https://www.statsmodels.org/stable/index.html)       |`0.13.0`      |
| [regex](https://docs.python.org/3/library/re.html)                | `2021.11.10` |

  
* * *
## License
* * *
This project contains a MIT [license](./LICENSE.md)
  
* * *
## Author
* * *
Stijn Arends  
Student master Data Science for Life Sciences  
17-01-2022  
