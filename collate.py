import os
from pathlib import Path
import csv

with open("StatList.txt", "r") as StatList:
    stats = StatList.read().splitlines()

# === DO NOT EDIT BELOW THIS LINE ===

types = ["Light Cruiser",
         "Heavy Cruiser",
         "Battlecruiser",
         "Battleship",
         "Light Aircraft Carrier",
         "Aircraft Carrier",
         "Destroyer",
         "Monitor",
         "Repair Ship"]

working_dir = os.getcwd()
ship_files_dir = os.path.join(working_dir, "ShipFiles")
names = [' '.join(f[:-4].split('_')) for f in os.listdir(ship_files_dir)
         if os.path.isfile(os.path.join(ship_files_dir, f))]
paths = [os.path.join(ship_files_dir, f) for f in os.listdir(ship_files_dir)
         if os.path.isfile(os.path.join(ship_files_dir, f))]

# Generate header line of CSV
header = "Name"
for stat in stats:
    header += "," + str(stat)

print("Generating CSV at " + working_dir + ".")

with open("Compilation.csv", 'w', newline='') as ship_csv:
    ship_csv.write(header)
    ship_csv.write('\n')

# Generate a row for each file
for name, path in zip(names, paths):
    values = {}
    with open(path, 'rb') as body:
        for line in body:
            for index, stat in enumerate(stats):
                if stat in str(line):
                    try:
                        value = line.decode('utf-8').split('=')[1].strip()
                    except IndexError:
                        print("There was an invalid " + stat + " found on " + name + "'s page. Feel free to ignore, or see the readme.")
                    except KeyError:
                        print("We can't find " + stat + "in the page for " + name + ". Please see the readme.")
                    if stat == "Type" and value not in types:
                        continue
                    values[stat] = value
    result = name
    with open("Compilation.csv", 'a', newline='') as ship_csv:
        for stat in stats:
            result += ',' + values[stat]
        ship_csv.write(result)
        ship_csv.write('\n')
        print("Row added for " + name + ".")
