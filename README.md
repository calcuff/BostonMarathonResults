# BostonMarathonResults

Years 2010-2024 were directly exported from the BAA [website](http://registration.baa.org/2022/cf/Media/iframe_ResultsSearch.cfm?mode=download&display=yes).

Years 2001-2009 were scraped from the BAA archives [website](http://registration.baa.org/cfm_Archive/iframe_ArchiveSearch.cfm?mode=entry&snap=75471469&). This archival site does not support direct downloads and I used a python web [scraper](scraper.py) to comb each page of results, 25 at a time, and save the result to an html file. The html files for each year were parsed with Beautiful Soup to read the encoded table data into a single csv file.

Additional weather data was pulled for historical weather patterns on the day of the race for each year. This includes the average, high and low temperatures for the day, wind speed and direction, percent humidity, and amount of rainfall. This data was pulled from historical weather [website](https://www.wunderground.com/history/daily/us/ma/east-boston/KBOS/date/2006-4-17).

There is work in progress for gathering home town/region elevation profile data per runner. Currently the dataset contains 1000 elevations above sea level from each of the 50 states and some for Canada. There are about 11,000 unique US towns represented from the past 24 years of the Boston Marathon and I initially sampled AK, AL, CA, and Alberta extensively. I then switched to sampling the most represented towns every 1000 records or so. After joining that with the runners data set I found I had about 184K records with elevation data, out of the ~506K original participants.