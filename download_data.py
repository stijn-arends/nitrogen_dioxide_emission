#!/usr/bin/env python3

# IMPORTS
import sys
import yaml

__author__ = "Stijn Arends"
__date__ = "16-01-2022"



def get_config() -> dict:
    """
    Read in config file and return it as a dictionary.
    
    :returns
    --------
    config - dict
        Configuration file in dictionary form.
    """
    with open("config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)
    return config


def main():
    config = get_config()
    data_dir = config['datadir']
    urls = config['urls']


if __name__ == "__main__":
    sys.exit(main())