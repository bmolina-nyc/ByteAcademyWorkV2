import csv

def new_csv():
    with open('NHL_2018.csv', newline="") as file_object:
        file_lines = file_object.readlines()

    with open('updated_csv.csv', 'w', newline="") as csvfile:
        fieldnames = ['Player Name |', 'Games Played |', '(Points*(60/TOI))*(82/GP) |', '(Blocks*(60/TOI)) * 82/GP |', '(Hits*(60/TOI)) * 82/GP |']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in file_lines:
            row = row.split(",")
            row[1] = row[1].split("\\")[0]
            if row[3] == 'DET':
                GP = int(row[5])
                points = int(row[8])
                blocks = int(row[23])
                hits = int(row[24])
                TOI = int(row[21])
                approx_points_82 = (points * (60//TOI)) * (82//GP)
                approx_blocks_82 = (blocks * (60//TOI)) * (82//GP)
                approx_hits_82 = (hits * (60//TOI)) * (82//GP)

                writer.writerow({'Player Name |': row[1], 'Games Played |': row[5], '(Points*(60/TOI))*(82/GP) |': approx_points_82 , '(Blocks*(60/TOI)) * 82/GP |': approx_blocks_82 , '(Hits*(60/TOI)) * 82/GP |': approx_hits_82})


print(new_csv())

