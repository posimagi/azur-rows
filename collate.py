import os
from pathlib import Path
import re

with open("StatList.txt", "r") as StatList:
    stats = StatList.read().splitlines()

delimiter = "|"

working_dir = os.getcwd()
ship_files_dir = os.path.join(working_dir, "ShipFiles")
names = [' '.join(f[:-4].split('_')) for f in os.listdir(ship_files_dir)
         if os.path.isfile(os.path.join(ship_files_dir, f))]
paths = [os.path.join(ship_files_dir, f) for f in os.listdir(ship_files_dir)
         if os.path.isfile(os.path.join(ship_files_dir, f))]

# Preparing header and initializing rows array
header = "Name"
for stat in stats:
    header += delimiter + str(stat)
rows = [header]

# Extracts the defined stat from the ship file via regex then adds to rows[]
for name, text_file in zip(names, paths):
    values = {}
    result = name
    with open(text_file, 'r', encoding='utf-8') as ship_file:
        ship_data = ship_file.read()
        print("===============================================")
        print("Extracting data for " + name + ".")
        for stat in stats:
            print("Searching for " + stat + ".")
            regex = re.search('(?<=\n'+stat+'=)(.*)', ship_data)
            try:
                values[stat] = regex.group(0)
                print(stat + " has been set to " + values[stat] + ".")
            except AttributeError:
                print("We can't find a " + stat + " for " + name +
                      ". Please confirm that the stat you're looking for " + 
                      "is properly spelled/capitalized according to the readme.")
                values[stat] = "Not found"
            result += delimiter + values[stat]
        rows.append(result)
        print(name + "'s data prepared.")
    
# Takes data from rows[] and writes it to CSV
with open("Compilation.csv", 'w', newline='', encoding='utf-8') as ship_csv:
    for row in rows:
        ship_csv.write(row)
        ship_csv.write('\n')
        name = row.split(delimiter)[0]
    print("===============================================")
    print("Data written to " + working_dir + " as Compilation.csv")