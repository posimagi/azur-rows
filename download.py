import os
from pathlib import Path
import requests
import re

# Importing data from the ShipList txt file.
with open("ShipList.txt", "r") as ShipList:
    ships = ShipList.read().splitlines()

<<<<<<< HEAD
# Set the directory to place ShipFile txt files.
=======
>>>>>>> ee68fa954ab5d6c204cb09d68b3816371c06518b
working_dir = os.getcwd()
ship_files_dir = os.path.join(working_dir, "ShipFiles")
print("Setting download path to " + ship_files_dir + ".")
if not os.path.exists(ship_files_dir):
    os.mkdir(ship_files_dir)

for ship in ships:
<<<<<<< HEAD
    print("Downloading file for " + ship + "...")
    # Use get request to download from the wiki
    try:
        page = requests.get("https://azurlane.koumakan.jp/w/index.php?title=" + ship + "&action=edit")
    except:
        print("Unable to access the website - please make sure you're able to access the wiki and/or the internet.")
        break
    print("Santitizing data...")
    
    # Magical regex to extract only the relevant data from the ShipMain class rather than all of the other unecessary HTML data.
    filtered_data = re.search('{{ShipMain(.|\n)*}}\n', page.text)
    
    # re.search returns data in groups, group 0 has the info we need. If an exception occurs, that means it can't find {{ShipMain}}, and is therefore not a valid ship page.
    try:
        result = filtered_data.group(0)
    except AttributeError:
        print("Unable to find the proper ship data class for " + ship + ". Verify the spelling is correct and that the page itself exists.")
        continue

    ship_file = ship + ".txt"
    outfile = os.path.join(ship_files_dir, ship_file)
    with open(outfile, 'a', encoding='utf-8') as shipdata:
        shipdata.write(result)
=======
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
>>>>>>> ee68fa954ab5d6c204cb09d68b3816371c06518b
