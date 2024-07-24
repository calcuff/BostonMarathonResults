# BostonMarathonResults

Years 2010-2024 were directly exported from the BAA [website](http://registration.baa.org/2022/cf/Media/iframe_ResultsSearch.cfm?mode=download&display=yes).

Years 2001-2009 were scraped from the BAA archives [website](http://registration.baa.org/cfm_Archive/iframe_ArchiveSearch.cfm?mode=entry&snap=75471469&). This archival site does not support direct downloads and I used a python web [scraper](scraper.py) to comb each page of results, 25 at a time, and save the result to an html file. The html files for each year were parsed with Beautiful Soup to read the encoded table data into a single csv file.