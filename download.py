import os
from pathlib import Path
import requests

# Importing data from the ShipList txt file.
with open("ShipList.txt", "r") as ShipList:
    ships = ShipList.read().splitlines()

working_dir = os.getcwd()
ship_files_dir = os.path.join(working_dir, "ShipFiles")
print("Setting download path to " + ship_files_dir + ".")
if not os.path.exists(ship_files_dir):
    os.mkdir(ship_files_dir)

for ship in ships:
    r = requests.get("https://azurlane.koumakan.jp/w/index.php?title=" + ship + "&action=edit")
    ship_file = ship + ".txt"
    print("Downloading file for " + ship + "...")
    outfile = os.path.join(ship_files_dir, ship_file)
    with open(outfile, 'wb') as f:
        lines = r.content.splitlines()
        for line in lines:
            f.write(line)
            f.write(b'\n')
    fileinfo = os.stat(outfile)
    filesize = int(fileinfo.st_size)
    if not 30000 < filesize < 75000:
        print("The file size for " + ship + " is abnormal, please confirm correct spelling/punctuation. See readme for details.")
