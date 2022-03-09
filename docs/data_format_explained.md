# Format of the CSV data

* Seperation sign used = ';'
* Decimal sign = '.'


The first 7 rows of the data consists of meta data. Where the first two columns contain additional metadata. 
The first four rows of these two columns contain the following information:

* **Date** export: date of the export of the data
* **Period**: for which period data is saved. The notation of the date is; yyyyMMdd hh:mm - yyyyMMdd hh:mm, which means "start-end"
* **Source**: url of the website from which the data is downloaded
* **Description data**: link to a readme file

From the fith column onwards additional meta-information of the measuring stations and the relevant measuring setup is available. 
The following information is available (row 1 through 7):

* **StationsCode**: unique identifier for each station
* **StationsName**: name of the station
* **Latitude, Longitude**: coordinates of the station
* **StationArea**: location of the station (regional, suburb, city, unkown)
* **Measuring principle**: with which principle a component was determined
* **Measuring setup**: which device was used to measure

Row 8 contains the headers of the data:

| Component  | Bep.period  | Unit  | BeginDateTime  | EndDateTime    | NL01485 | NL01487  | other stations | 
| -----------| :---------: | :---: | :------------: | :------------: | :-----: | :------: | :------------: |
| NO2        | hour        | µg/m³ | 20200101 00:00 | 20200101 01:00 | 45.8    |  48.5    |  60            |

From row 9 the data is available.
