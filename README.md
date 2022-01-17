# The effect of a lockdown on the nitrogen dioxide emission in the Netherlands
Studying the effect of the number of corona cases and the lockdowns on the emission of nitrogen dioxide

## Description 
* * *

### Data

### Data description
What is the format of the data? What does it contain?


## Installation
* * *

### Single install
The easiest way to install all the required packages is via conda. How to install conda on your system can be found [here](https://docs.anaconda.com/anaconda/install/index.html).

To create a new environment which contains all the required packages plus the right version run the following code:

```bash
  conda env create -f environment.yml
```

This will create a new environment named `mosquito_env` which can be used to run this repository.

> NOTE: the environment.yml is located in the install/ directory [here](install/environment.yml).

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

## Getting started
* * *
How to run the code?


## Requirements
* * *
| Software                          | Version  |
| --------------------------------- | :------: |
| [Python](https://www.python.org/) | `3.9.7`  |    


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


## License
* * *
This project contains a MIT [license](./LICENSE.md)
