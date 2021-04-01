import csv
import json

#convert csv to json
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    with open(csvFilePath, encoding='utf-8') as csvf: 
                csvReader = csv.DictReader(csvf) 

                for row in csvReader: 
                        jsonArray.append(row)
  
    
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'better_than_spotify.csv'
jsonFilePath = r'better_than_spotify.json'
csv_to_json(csvFilePath, jsonFilePath)