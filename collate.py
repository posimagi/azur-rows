import os

# === CHANGE ME: Add additional stats here, ===
#     in the form of the MediaWiki variables
#     found on the edit pages for each ship
#     (e.g. https://azurlane.koumakan.jp/w/index.php?title=Hood&action=edit)
stats = ["HealthMax",
         "AAMax",
         "Nationality",
         "Type"]
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

desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")
azur_dir = os.path.join(desktop, "AzurLane")
names = [' '.join(f[:-4].split('_')) for f in os.listdir(azur_dir) if os.path.isfile(os.path.join(azur_dir, f))]
paths = [os.path.join(azur_dir, f) for f in os.listdir(azur_dir) if os.path.isfile(os.path.join(azur_dir, f))]

# Generate header line of CSV
header = "Name"
for stat in stats:
    header += "," + str(stat)
print(header)

# Generate a row for each file
for name, path in zip(names, paths):
    values = {}
    with open(path, 'rb') as body:
        for line in body:
            for index, stat in enumerate(stats):
                if stat in str(line):
                    value = line.decode('utf-8').split('=')[1].strip()
                    if stat == "Type" and value not in types:
                        continue
                    values[stat] = value
    result = name
    for stat in stats:
        result += ',' + values[stat]
    print(result)

