import csv
from bs4 import BeautifulSoup
import os




# Initialize CSV data
csv_data = []
headers = ["YEAR", "BIB", "NAME", "AGE", "M/F", "CITY", "STATE", "COUNTRY", "DivisionType", "Overall", "Gender", "Division", "Official Time", "Net Time"]

YEAR='2009'
html_dir = './data/html/'+YEAR

for filename in sorted(os.listdir(html_dir)):
    if filename.endswith('.html'):
        filepath = os.path.join(html_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all relevant rows
        rows = soup.select('.tablegrid_table tbody tr')
        # Process each row
        for i, row in enumerate(rows):
            print("i: ", i)
            if i % 2 == 1:
                print("Continuing")
                continue
            cols = row.find_all('td')
            if len(cols) == 9:  # Ensure it's a data row and not a header
                print("Y ", cols[0].text.strip())
                year = cols[0].text.strip()
                print("B ", cols[1].text.strip())
                bib = cols[1].text.strip()
                print("name ", cols[2].text.strip())
                name = cols[2].text.strip()
                print("Age ", cols[3].text.strip())
                age = cols[3].text.strip()
                print("gender ", cols[4].text.strip())
                gender = cols[4].text.strip()
                print("City ", cols[5].text.strip())
                city = cols[5].text.strip()
                print("State ", cols[6].text.strip())
                state = cols[6].text.strip()
                print("Country ", cols[7].text.strip())
                country = cols[7].text.strip()
                print("division ", cols[8].text.strip())
                division = cols[8].text.strip()
                
                # Look for the detailed results
                details_table = row.find_next('table', class_='table_infogrid')
                if details_table:
                    details = details_table.find_all('td')
                    print("Overall ", details[0].text.strip())
                    overall = details[0].text.strip().replace(" ", "")
                    print("gender_place ", details[1].text.strip())
                    gender_place = details[1].text.strip().replace(" ", "")
                    print("division_place ", details[2].text.strip())
                    division_place = details[2].text.strip().replace(" ", "")
                    print("official_time ", details[3].text.strip())
                    official_time = details[3].text.strip()
                    print("net_time ", details[4].text.strip())
                    net_time = details[4].text.strip() if len(details) > 4 else ''
                else:
                    overall = gender_place = division_place = official_time = net_time = ''
                
                csv_data.append([year, bib, name, age, gender, city, state, country, division, overall, gender_place, division_place, official_time, net_time])

# Write to CSV
FILENAME=YEAR+'_marathon_results.csv'
with open('data/'+FILENAME, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(csv_data)

print("Data has been written to marathon_results.csv")