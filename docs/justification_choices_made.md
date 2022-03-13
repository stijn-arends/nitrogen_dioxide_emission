# Justification of the choices that were made during this project


* * *
### Data maintenance 

The data is stored and maintained by third parties, links can be found in the [data source](../README.md#source) section in the README. The data that was originally used 
for this project can be found inside this reposity in the [data](../data/) and [geojson](../geojson/) folders. No personal or private data was used so the data can be 
stored in the repository. 

If additional NO2 emission data is published then it can be downloaded using the [download data script](../scripts/download_data.py). 

* * *
### Coding

Not every piece of code is organized inside of a class. I thought that for some pieces of code that it was not necessary. 
These pieces of code do not particularly belong to a specific class, and or don't benefit from being inside of one. An example of this is the function that checks if a 
date is during a lockdown, or the functions that plot a heatmap, or violin plot. 

However, the code for the dashboard is organized inside of classes where the SOLID principles were followed whever it was possible. 
For example, a base class was made to create a folium map, which can easily be extended by inherting it in a new class and adding additional functionalties. 
For example to create a map with markers or a heatmap over time. 

A [logging decorator](scripts/logger.py) was created to make sure that the code ran smoothly. If any exception occured while running the code than that would be logged, 
and if everything goes smoothly than that would be reported.

* * *
### Data filtering and imputation

The original data contained a lot of missing data. For starters, stations that had more then 30% missing values were removed. 
It was decided to remove these stations because interpolation or imputation of data with too many missing values is not reliable. 
The missing values of the stations that passed the initial filtering were imputed. 

Performance of four data imputation methods were measured on air quality measurement data (CO, O3, PM10, SO2, NOx, NO2). The four methods were, Mean Top Bottom, 
Neirest Neighbours, Linear regression, and Multiple imputation[[1]](#references). This study concluded that the Mean Top Bottom approach was best to impute air quality measurement data. 
However, the data that was used for that study had mostly small gaps in the data, for example one or three hours. Whereas the data for this project contains more larger 
gaps(i.e. 40 hours). While testing the Mean Top Bottom approach it became clear that it could not handle large gaps in the data. Therefore, another approach was tested; 
regression based data imputation. Measuring stations that had a relationship (correlation >= 0.7) with the station of interest were used to create a predictive model to 
fill the missing values. This method seems to work well, which is in contrast to the findings of N. A. Zakaria[[1]](#references). They concluded that the Linear regression method 
performed the worst out of the four methods that were tested. 

* * *
### Assigning lockdown states

The data needed a column which described whether or not a date was during a lockdown. First, the different lockdowns and their time span needed to be identified.
These were derived from the offical website of the Dutch goverment[[2]](#references). and wikipedia[[3]](#references)..
Here is a list of the different lockdowns in the Netherlands:

Lockdown:
* 14 oktober 2020 - 14 december 2020: partially lockdown
* 15 december 2020 - 27 april 2021: hard lockdown
* 28 april 2021 - 25 september 2021: a few restrictions
* 26 september 2021 - 26 november 2021: restrictions
* 27 november 2021 - 17 december 2021: lockdown in the evening
* 18 december 2021 -  5 januari 2022: lockdown

To be able to study the effect of the lockdowns on NO2 emission levels two labels needed to be created: Lockdown and No-lockdown.
For the purpose of this study the differences of the lockdowns were not accounted for and were treated as equal. 


* * * 
### Data format

The original format of the data is a wide data frame where each station has its own column. To be able to work with the data the NO2 emission values need to be inside of one 
column. TO achieve the data was transformed from wide to long, by creating a seperate column for the station ID and the NO2 emission values. 


* * *
### Data inspection

> NOTE: results of the data inspection can be found inside the [notebook](../NO2_emission_corona.ipynb) in section `2 Data inspection`.

When comparing the basic statistics of the two data frames it is clear that the year 2021 contains overall more covid cases. 
However, the statistics about the NO2 emission looks to be somewhat the same for both years. Something notably is that the NO2 emission values has a negative 
value as its minimum value, which is something that is not expected. This is most probably caused by measuring inaccuracies. These measuring inaccuracies can be caused by, 
for example rapidly changing wheater conditions (i.e. humidity, temperature)[[4]](#references).The max values for both years are far higher then the mean. This might indicate 
that there is an outlier present. However, according to the world health organiztaion(WHO) the maximum value of the hourly mean of NO2 emission might be much higher compared 
to the annual mean[[5]](#references). Indicating that this probably is not an outlier. In addition, a document of the WHO about Ambient (Outdoor) AirPollution Guidelines states that a hourly 
mean of 200 μg/m3 is normal[[6]](#references). These high values were also not introduced by data imputation. This was validated by checking the maximum values before the data imputation step. 

* * *
### Plotting 

#### Data inspection
Several plots were used to inspect the data. First, a heatmap was created to check if there were correlation between the different stations. 
The heatmap was created because information about the correlation between stations was needed for data imputation. Because, to impute data for a station, 
correlated stations were needed to create a model which produces reliable results. Second, a density plot was created to get an impression of the distribution of the NO2 
values for both lockdown states. Finally, violin plots were used to get a more detailed look at the distribution of the NO2 values for both lockdowns. Weidgets were also added
so that each station can be looked at individually. 

#### Checking assumptions
A Q-Q plot is used to check for normality because there is a large sample size (>50). A Q-Q plot is made for both years and lockdown states. 

#### Visualizing the data
Three different visualisation were used to display the data, two of them are maps and the other one is a line chart. First, a map was created that displays the location and names of the different stations. The NO2 value for a specific data is displayed when you click on a station. The date can be altered using a widget panel, which also displays if the selected date was during a lockdown or not. Next, a map was created to display the NO2 values over time for the different stations. This can give a quick overview on how the NO2 values change over time. Finally, a line chart was created to give a more detailed look on the NO2 emission for a certain station. Three widgets are linked to this plot, a select year widget, a data range slider, and a widget to select a station. The select year widget also influences the date range slider. In addition to this, the plot also displays where the lcokdowns start and end. 

* * *
### Statistical testing

The Levene's test of equality was used to check if the different groups contained equal variance. Median was used as center, because it is recommended for non-normal data[[7]](#references). Equal variance of NO2 emission levels was tested for the two lockdown states in both years. For both instances the null hypothesis was rejected and it was concluded that the groups did not have equal variance. 

In summary, the two different groups are not normally distributed and do not have equal variance. This means that a T-test or ANOVA can't be used to test if there is a significant difference between the two groups. However, a non-parametric test can be used.  

The Mann-Whitney U test was used to check for differences between the two groups. Because, "the Mann-Whitney U Test is a nonparametric version of the independent samples t-test. The test primarily deals with two independent samples that contain ordinal or continous data"[[8]](#references).

* * *
# References

[1] https://www.semanticscholar.org/paper/Imputation-methods-for-filling-missing-data-in-air-Zakaria-Noor/068aef2863fa856e8498f74674ecb4806df88c93  
[2] https://www.rijksoverheid.nl/onderwerpen/coronavirus-tijdlijn    
[3] https://nl.wikipedia.org/wiki/Maatregelen_tijdens_de_coronacrisis_in_Nederland#Maatregelen_naar_datum_van_aankondiging  
[4] https://www.luchtmeetnet.nl/informatie/overige/negatieve-waarden  
[5] https://www.ncbi.nlm.nih.gov/books/NBK138707/  
[6] https://environmentaldevices.com/wp-content/uploads/2020/05/WHO-Guidlines.pdf  
[7] https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levene.html  
[8] https://corporatefinanceinstitute.com/resources/knowledge/other/nonparametric-tests/
