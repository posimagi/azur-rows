## azur-rows - CSV dump for Azur Lane ship stats

### Introduction

azur-rows pulls stats from https://azurlane.koumakan.jp/,
then parses the files and outputs CSV for importing
into your spreadsheet program of choice

### How to use

Modify the `ShipList.txt` file with the ships you want to have in the CSV.
Please enter them one ship per line, with underscores (`_`) instead of spaces.

Modify the `StatList.txt` file with any additional entries you want added or removed.
The names of the individual stats are based on what can be found on the above wiki site. To find them, go to the page of an individual ship and click on "View Source" at the top right (ex: https://azurlane.koumakan.jp/w/index.php?title=Trial_Bullin_MKII&action=edit). The individual values you see in that source file, like "Artist", "Class", "TorpedoGrade", etc. are the ones that will be entered into your CSV.

Once those have been modified to your liking, run the `download.py` file. Wait for it to complete, then run `collate.py`.  This will create a CSV file in your working directory, to which you can then import into whatever spreadsheet software you prefer.

### Troubleshooting

#### "The file size for `ship` is abnormal."

This usually means that someone's named was spelled incorrectly, or spaces were being used instead of underscores. This is just being used as a catch/warning - if the second part of the script works as intended, then you're probably fine.

#### "There was an invalid `stat` found on `ship`'s page."

This is due to improper santization, still a work in progress. This usually happens in Type (Battlecruiser, Destroyer, etc.) detection when the script finds something else mentioning type. This currently doesn't cause any problems with the CSV data, but more as a warning.
Please also verify that there are **no other files in the ShipFiles directory aside from the .txt files that the downloader creates!**

#### "We can't find `stat` in the page for `ship`."

If this is the only ship this is happening on, please verify the spelling of the ship. If this is happening on all ships, please verify the spelling of the stat on the wiki page's source. Please also verify that there are **no other files in the ShipFiles directory aside from the .txt files that the downloader creates!**