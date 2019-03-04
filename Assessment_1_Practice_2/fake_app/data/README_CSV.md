# Read/Write CSV
Use Python's `csv` library to do the following with the attached `NHL_2018.csv`.Don't use any functions from the external libraries `pandas` or `numpy`, we'll get to those later in the course.

This CSV contains, as the name might imply, a ton of player statistics from the 2008 NHL season!What all those statistics actually mean isn't important for the scope of this exercise, though if you're curious
you can check out the source at [Hockey-Reference](https://www.hockey-reference.com/leagues/NHL_2008_skaters.html).

---

Using the attached CSV, let's read this into memory as a file object and create a new, abbreviated CSV of the important data we want. Here's a good start:

```
import csv

with open('NHL_2018.csv') as in_csv:
```

Let's write a new csv of all the players from the championship team in 2018 (Detroit, represented in the `Tm` column as `DET`), and let's normalize their stats so we can compare against each other more easily. Currently, the `PTS`, `BLK`, and `HIT` columns (PoinTS, BLocKed shots, and HITs) are just raw counts- they're not dependent on whether a player played one game or every game in the season. From a data analysis perspective, we'd like to be able to compare players more fairly.

To do so, we'll use the `GP` (Games Played) and `TOI` (Time On Ice) columns to normalize our data. What this actually means:

* There are 82 games in the season, so to pretend everyone played a full season, we'll need to multiply all of these our statistics by 82/GP to get each player's theoretical production

* Once we have that number, we also need to account for limited time (in hockey, players play parts of a whole game, not the entire 60 minutes). To do this we'll have to take the TOI column (written as a string of minutes:seconds) and find it's percentage of a full game (60 minutes). Then we multiply that number by each stat to get a player's approximate stats over a full 60 minute game for the whole season.

* Lastly, we need to clean up the names. Each player's name will look like `"Firstname Lastname\Firstla01"`, we'll want to clean these up to get rid of the extra characters.

The returned CSV should have rows that look like:

`Player Name | Games Played | (Points*(60/TOI))*(82/GP) | (Blocks*(60/TOI)) * 82/GP | (Hits*(60/TOI)) * 82/GP |`