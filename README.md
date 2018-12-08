## azur-rows - CSV dump for Azur Lane ship stats

### Introduction

azur-rows pulls stats from https://azurlane.koumakan.jp/,
then parses the files and outputs CSV for importing
into your spreadsheet program of choice

### How to use

You may modify the list of `ships` in `download.py`,
and the list of `stats` in `collate.py`, to affect the scope
of the data to scrape.

Then, run `download.py` once, and after it finishes, run `collate.py` once.

When you run `download.py`, a directory called "AzurLane" will be created
in your home directory (user folder on Windows).
