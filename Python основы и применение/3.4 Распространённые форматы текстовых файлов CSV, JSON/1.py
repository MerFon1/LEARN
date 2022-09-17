import csv
import time
with open('Crimes.csv') as f:
    keys = f.readline().split(',')
    f.seek(0)
    file = csv.reader(f)
    data = [dict(zip(keys, i)) for i in file]
    data = list(filter(lambda x: x['Date'][6:10]=='2015',data))
    print(max([i['Primary Type'] for i in data]))

