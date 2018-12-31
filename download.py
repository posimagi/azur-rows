import os
from pathlib import Path
import requests

# === CHANGE ME: Add ship names here to scrap more info ===
ships = ["San Diego", "Hood"]
# === DO NOT EDIT BELOW THIS LINE ===

working_dir = os.getcwd()
ship_files_dir = os.path.join(working_dir, "ShipFiles")
print("Setting download path to " + ship_files_dir + ".")
if not os.path.exists(ship_files_dir):
    os.mkdir(ship_files_dir)

ship_s = []
for ship in ships:
    ship_s.append('_'.join(ship.split()))
pages = []

for ship in ship_s:
    print("Downloading file for " + ship + "...")
    pages.append(
        "https://azurlane.koumakan.jp/w/index.php?title=" + ship + "&action=edit")

for ship, page in zip(ship_s, pages):
    r = requests.get(page)
    ship_file = ship + ".txt"
    print("Writing file for " + ship + "...")
    outfile = os.path.join(ship_files_dir, ship_file)
    with open(outfile, 'wb') as f:
        lines = r.content.splitlines()
        for line in lines:
            f.write(line)
            f.write(b'\n')
