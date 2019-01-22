## azur-rows - CSV dump for Azur Lane ship stats

### Introduction

azur-rows pulls stats from https://azurlane.koumakan.jp/,
then parses the files and outputs CSV for importing
into your spreadsheet program of choice.

### How to use

Modify the `ShipList.txt` file with the ships you want to have in the CSV.
Please enter them one ship per line, with underscores (`_`) 
instead of spaces within the names (i.e, "San_Diego" instead of "San Diego"),
in addition to making sure capitalization and spelling are correct.
When in doubt, find the ship's page on the wiki and copy the name from the URL.

Modify the `StatList.txt` file with any additional entries you want added or removed.
The names of the individual stats are based on what can be found on the above wiki site. 
To find them, go to the page of an individual ship and click on "View Source" at the top right 
(ex: https://azurlane.koumakan.jp/w/index.php?title=Trial_Bullin_MKII&action=edit). 
The individual values you see in that source file, like "Artist", "Class", "TorpedoGrade", etc. 
are the ones that will be entered into your CSV. 
The current `StatList.txt` file includes what I think are the useful entries.

Once those have been modified to your liking, run the `download.py` file. 
Wait for it to complete, then run `collate.py`. 
This will create a CSV file in your working directory, 
to which you can then import into whatever spreadsheet software you prefer.

**Note that the delimiter used by default is a pipe (`|`)**, so you will need to modify
your spreadsheet software's settings to accomodate for this. 
You can change the delimiter within the `collate.py` file near the top, 
but do NOT use commas as your delimiter if you are downloading 
any Skill descriptions, as those include commas and will get delimited.

### Troubleshooting

#### Downloading

##### "You will need to install the requests library to continue. You may install it using Pip."

Pretty self-explanatory, the instructions for this depend on what OS you're running this on. 
If you're on Windows, try looking at 
https://stackoverflow.com/questions/30536946/how-to-install-requests-module-in-python-3-4-version-on-windows.

On MacOS/Linux, you should be able to just run `pip install requests`, but no guarantees.

##### "Unable to access the website..."

Downloading _typically_ requires internet access, but that could also be just me.

Confirm you don't have any firewalls/AV blocking the Python binary and/or the script itself.

##### "Unable to find the proper ship data class..."

Verify the name, spelling, and capitalization of the ships you put in `ShipList.txt`.
This error means the page it downloaded was invalid, so either the website completely changed its
data structure or it downloaded the equivalent of a 404 page.

#### Collating

##### "We can't find a `stat` for `ship`."

It's looking for the line specified, 
so make sure that line is spelled correctly, exists, **and is capitalized appropriately**.
An example of this would be `healthMax` vs `HealthMax` - the second one is correct.
If this happens a lot on a single ship entry, make sure the file 
downloaded was also named correctly 
(such as if you downloaded "San Diego" instead of "San_Diego").
Please also verify that there are 
**no other files in the ShipFiles directory aside from the .txt files that the downloader creates!**