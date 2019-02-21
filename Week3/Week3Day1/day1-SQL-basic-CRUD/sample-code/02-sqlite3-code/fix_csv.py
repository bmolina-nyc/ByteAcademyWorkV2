import csv

INCSV = 'hurricanes.csv'
OUTCSV = 'hurricanes_fixed.csv'

with open(INCSV, 'r') as ifil, open(OUTCSV, 'w') as ofil:
    inread = csv.DictReader(ifil)
    outwrite = csv.DictWriter(ofil,
            ('month',
            'average',
            'num2005',
            'num2006',
            'num2007',
            'num2008',
            'num2009',
            'num2010',
            'num2011',
            'num2012',
            'num2013',
            'num2014',
            'num2015'))
    outwrite.writeheader()
    for dictline in inread:
        newdict = {
                'month': dictline['Month'],
                'average': dictline[' "Average"'],
                'num2005': dictline[' "2005"'],
                'num2006': dictline[' "2006"'],
                'num2007': dictline[' "2007"'],
                'num2008': dictline[' "2008"'],
                'num2009': dictline[' "2009"'],
                'num2010': dictline[' "2010"'],
                'num2011': dictline[' "2011"'],
                'num2012': dictline[' "2012"'],
                'num2013': dictline[' "2013"'],
                'num2014': dictline[' "2014"'],
                'num2015': dictline[' "2015"']
                }
        outwrite.writerow(newdict)
