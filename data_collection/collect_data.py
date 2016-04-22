import csv
import os
import urllib.request
from datetime import date

today = date.today().isoformat()

with open('/app/tweetbot/raw_data/linksDB.csv') as csvfile:
    websiteDB = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in websiteDB:
        print(row)
        directory = '/app/tweetbot/raw_data/' + row[0] + '/' + today + '/'
        print(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)
        html = urllib.request.urlopen(row[1]).read()
        f = open(directory + 'index.html', 'w')
        print(html, file = f)

print('Done.')


