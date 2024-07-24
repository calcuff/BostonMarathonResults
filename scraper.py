import requests
import time

YEAR = '2001'
initial_url = 'http://registration.baa.org/cfm_Archive/iframe_ArchiveSearch.cfm?mode=results&RequestTimeout=600&snap=61785674&'
url = 'http://registration.baa.org/cfm_Archive/iframe_ArchiveSearch.cfm?mode=results&criteria=&StoredProcParamsOn=yes&&VarRaceYearLowID='+YEAR+'&VarRaceYearHighID=0&VarAgeLowID=18&VarAgeHighID=100&VarGenderID=0&VarBibNumber=&VarLastName=&VarFirstName=&VarStateID=0&VarCountryOfResidenceID=0&VarCity=&VarZip=&VarTimeLowHr=&VarTimeLowMin=&VarTimeLowSec=00&VarTimeHighHr=&VarTimeHighMin=&VarTimeHighSec=59&VarSortOrder=ByTime&VarAddInactiveYears=0&records=25&headerexists=Yes&bordersize=0&bordercolor=%23ffffff&rowcolorone=%23FFCC33&rowcolortwo=%23FFCC33&headercolor=%23ffffff&headerfontface=Verdana%2CArial%2CHelvetica%2Csans%2Dserif&headerfontcolor=%23004080&headerfontsize=12px&fontface=Verdana%2CArial%2CHelvetica%2Csans%2Dserif&fontcolor=%23000099&fontsize=10px&linkfield=&linkurl=&linkparams=&queryname=SearchResults&tablefields=RaceYear%2CFullBibNumber%2CFormattedSortName%2CAgeOnRaceDay%2CGenderCode%2CCity%2CStateAbbrev%2CCountryOfResAbbrev%2CReportingSegment'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'xyz',
    'Origin': 'http://registration.baa.org',
    'Pragma': 'no-cache',
    'Referer': 'http://registration.baa.org/cfm_Archive/iframe_ArchiveSearch.cfm?mode=results&RequestTimeout=600&snap=97105517&',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

# Fetch the first page
data_first_page = {
    'SortOrder': 'ByTime',
    'RaceYearLowID': YEAR,
    'RaceYearHighID': 0,
    'LastName': '',
    'FirstName': '',
    'City': '',
    'StateID': 0,
    'Zip': '',
    'CountryOfResidenceID': 0,
    'TimeLowHr': '',
    'TimeLowMin': '',
    'TimeHighHr': '',
    'TimeHighMin': '',
    'AgeLowID': 0,
    'AgeHighID': 100,
    'GenderID': 0,
    'BibNumber': ''
}

response = requests.post(initial_url, headers=headers, data=data_first_page, verify=False)
if response.status_code == 200:
    with open('data/html/'+YEAR+'/marathon_results_1.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("Saved marathon_results_1.html")
else:
    print(f"Failed to retrieve the first page, status code: {response.status_code}")
    exit()

start_index = 26
increment = 25
total_records = 13451           # Example total number of records
file_count = 2

while start_index < total_records:
    data = {
        'start': start_index,
        'next': 'Next 25 Records'
    }

    response = requests.post(url, headers=headers, data=data, verify=False)
    
    if response.status_code == 200:
        filename = f'data/html/{YEAR}/marathon_results_{file_count}.html'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Saved {filename}")
        
        start_index += increment
        file_count += 1
        time.sleep(2)
    else:
        print(f"Failed to retrieve data at start index {start_index}")
        break