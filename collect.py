import requests

urls = ["https://azurlane.koumakan.jp/w/index.php?title=Hood&action=edit"]

bodies = []
for url in urls:
    r = requests.get(url)
    bodies.append(r.content)

types = ["Light Cruiser",
         "Heavy Cruiser",
         "Battlecruiser",
         "Battleship",
         "Light Aircraft Carrier",
         "Aircraft Carrier",
         "Destroyer",
         "Monitor",
         "Repair Ship"]
stats = ["HealthMax",
         "AAMax",
         "Nationality",
         "Type"]

for body in bodies:
    lines = body.splitlines()
    for line in lines:
        for stat in stats:
            if stat in str(line):
                value = line.decode('utf-8').split('=')[1].strip()
                if stat == "Type" and value not in types:
                    continue
                print(stat + "," + value)
