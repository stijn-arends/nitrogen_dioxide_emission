#!/usr/bin/env python3

# IMPORTS
import sys
import yaml
from pathlib import Path

__author__ = "Stijn Arends"
__date__ = "16-01-2022"


class GetData:
    """
    A class to download data.

    ...

    Attributes
    ----------
    data_dir : str
        Location of data storage


    Methods
    -------
    make_data_dir():
        Create a directory in the system to store the data, if it doesn't exist yet.
    """

    def __init__(self, data_dir):
        self.data_dir = data_dir

    def make_data_dir(self) -> None:
        """
        Create a directory (if it does not exisit yet) to store the 
        data.

        :Excepts
        --------
        FileExistsError
            The directory already exists
        """
        path = Path(self.data_dir)
        try:
            path.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print(f"[{self.make_data_dir.__name__}] Folder is already there.")


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