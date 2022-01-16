#!/usr/bin/env python3

# IMPORTS
import sys
from typing import Any
import yaml
from pathlib import Path
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from tqdm import tqdm

__author__ = "Stijn Arends"
__date__ = "16-01-2022"


class FourOFourError(Exception):
    """Exception raised for 404 errors.

    Attributes:
        url -- url of a website
        message -- explanation of the error
    """

    def __init__(self, url):
        self.url = url
        self.message = f"404 Error for url: {url}"
        super().__init__(self.message)


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

    def check_file_exists(self, file_name, expected_size):
        """
        Check if a given file already exists and if the size of the file is 
        as big as it supposed to be.

        :parameters
        -----------
        file_name - String
            Name of the file
        expected_size - int
            Expected size of the file

        :returns
        --------
        True
            Return True if the file already exists AND if it has the expected file size
        False
            Return False if the file does not exists OR if it is NOT the expected file size

        :exception
        ----------
        FileNotFoundError
            If the file does not exists yet, return False
        """
        try:
            file = Path(self.data_dir + file_name)
            # Check if exists
            check = file.exists()
            # Get file size
            file_size = file.stat().st_size
            if check and file_size == expected_size:
                return True
            else:
                return False
        except FileNotFoundError as e:
            return False
            
    @staticmethod
    def find_NO2_files(url) -> list:
        """
        Find the files that contain information about NO2 and save there url in a list.

        :parameter
        ----------
        url - String
            String of an url

        :returns
        --------
        hrefs - list
            List of urls

        :Excepts
        --------  
        requests.RequestException
            An error that might occur while sending a request to the url
        """
        try:
            response = requests.get(url) 
            if response.status_code == 404:
                raise FourOFourError(url)
        except requests.RequestException as e: # requests.exceptions.RequestException
            print(f"Error: {e}")
            print(f"An error has occured while sending a request to the following url: {url}.")
            raise 

        soup = BeautifulSoup(response.text, features="html.parser")

        hrefs = []
        # Get the files from the url
        for a in soup.find_all('a'):
            if 'NO2' in a['href']:
                # a['href'] is the name of the file
                url_data = url + a['href']
                hrefs.append(url_data)
        return hrefs


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