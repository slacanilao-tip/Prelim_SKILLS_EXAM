import json
import csv

with open('/home/devasc/CPE41S1/prelim_skills_exam/covid_cases.json', 'r') as cases:
    data = json.loads(cases.read())

with open('covid_data.csv', 'w', newline='') as parsed_data:
    csv_file = csv.writer(parsed_data)
    csv_file.writerow(["dateRep","countriesAndTerritories","cases","deaths"])

for x in data['records']:
    csv_file.writerow(x["dateRep","countriesAndTerritories","cases","deaths"])

    print(data)





