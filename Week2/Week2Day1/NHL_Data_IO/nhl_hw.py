import csv

def new_csv():
    with open('NHL_2018.csv') as file_object:
        file_lines = file_object.readlines()

    with open('updated_csv.csv', 'w', newline="") as csvfile:
        fieldnames = ['Player Name |', 'Games Played |', '(Points*(60/TOI))*(82/GP) |', '(Blocks*(60/TOI)) * 82/GP |', '(Hits*(60/TOI)) * 82/GP |', 'TOI']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in file_lines:
            row = row.split(",")
            if row[3] == 'DET':
                GP = int(row[5])
                points = int(row[8])
                blocks = int(row[23])
                hits = int(row[24])
                TOI = int(row[21])
                approx_points_82 = (points * (60//TOI)) * (82//GP)
                approx_blocks_82 = (blocks * (60//TOI)) * (82//GP)
                approx_hits_82 = (hits * (60//TOI)) * (82//GP)

                writer.writerow({'Player Name |': row[1], 'Games Played |': row[5], '(Points*(60/TOI))*(82/GP) |': approx_points_82 , '(Blocks*(60/TOI)) * 82/GP |': approx_blocks_82 , '(Hits*(60/TOI)) * 82/GP |': approx_hits_82,  'TOI':row[21]})

# * There are 82 games in the season, so to pretend everyone played a 
# full season, we'll need to multiply all of these our statistics by 82/GP 
# to get each player's theoretical production

# * Once we have that number, we also need to account for limited time 
# (in hockey, players play parts of a whole game, not the entire 60 minutes). To do this we'll have to take the TOI column (written as a string of minutes:seconds) and find it's percentage of a full game (60 minutes). 
# Then we multiply that number by each stat to get a player's 
# approximate stats over a full 60 minute game for the whole season.

# * Lastly, we need to clean up the names. 
# Each player's name will look like `"Firstname Lastname\Firstla01"`, 
#     we'll want to clean these up to get rid of the extra characters.

# The returned CSV should have rows that look like:




print(new_csv())

