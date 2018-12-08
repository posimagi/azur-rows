import os
import requests

# === CHANGE ME: Add ship names here to scrap more info ===
ships = ["San Diego", "Hood"]
# === DO NOT EDIT BELOW THIS LINE ===

homepath = os.path.join(os.environ["HOMEPATH"])
azur_dir = os.path.join(homepath, "AzurLane")
if not os.path.exists(azur_dir):
    os.mkdir(azur_dir)

ship_s = []
for ship in ships:
    ship_s.append('_'.join(ship.split()))
pages = []

for ship in ship_s:
    pages.append(
        "https://azurlane.koumakan.jp/w/index.php?title=" + ship + "&action=edit")

for ship, page in zip(ship_s, pages):
    r = requests.get(page)
    ship_file = ship + ".txt"
    outfile = os.path.join(azur_dir, ship_file)
    with open(outfile, 'wb') as f:
        lines = r.content.splitlines()
        for line in lines:
            f.write(line)
            f.write(b'\n')
