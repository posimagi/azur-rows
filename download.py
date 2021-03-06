import os
from pathlib import Path
import re
try:
    import requests
except ModuleNotFoundError:
    # Requests library is not installed in python by default
    print("You will need to install the requests library to continue. You may install it using Pip.")


# Importing data from the ShipList txt file.
with open("ShipList.txt", "r") as ShipList:
    ships = ShipList.read().splitlines()

# Set the directory to place ShipFile txt files.
working_dir = os.getcwd()
ship_files_dir = os.path.join(working_dir, "ShipFiles")
print("Setting download path to " + ship_files_dir + ".")
if not os.path.exists(ship_files_dir):
    os.mkdir(ship_files_dir)

for ship in ships:
    # Use get request to download from the wiki
    print("Downloading file for " + ship + "...")
    try:
        page = requests.get(
            "https://azurlane.koumakan.jp/w/index.php?title=" + ship + "&action=edit")
    except:
        print("Unable to access the website - please make sure you're able to access the wiki and/or the internet.")
        break
    print("Sanitizing data...")

    # Regex to isolate/export only the relevant ShipMain info.
    filtered_data = re.search('{{ShipMain(.|\n)*}}\n', page.text)

    # re.search returns data in groups, group 0 has the info we need.
    # If an exception occurs, that means it can't find {{ShipMain}}, and is therefore not a valid ship page.
    try:
        result = filtered_data.group(0)
    except AttributeError:
        print("Unable to find the proper ship data class for " + ship +
              ". Verify the spelling is correct and that the page itself exists.")
        continue

    # Stripping leading whitespace, pipes, and erroneous whitespace surrounding equal signs
    result_list = result.split('\n')

    formatted_data = []
    for line in result_list:
        line = line.lstrip(' |')
        line = re.sub(' ?= ?','=',line)
        formatted_data.append(line)

    # Writing the file.
    ship_file = ship + ".txt"
    outfile = os.path.join(ship_files_dir, ship_file)
    with open(outfile, 'w', encoding='utf-8') as shipdata:
        shipdata.write('\n'.join(formatted_data))