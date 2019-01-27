import requests
import json
import csv
import pandas as pd
import time

j = 0
check = True
for i in range(530457, 2, -1):
    print(i)
    rcomp = requests.get(
        "https://api.themoviedb.org/3/movie/{0}?api_key=d38fad0520bad759ea1c10ff92ee3e98".format(i))
    if rcomp.status_code != 404:
        data = rcomp.json()
        with open('mycsvfile.csv', 'a', encoding="utf-8") as f:  # Just use 'w' mode in 3.x
            w = csv.writer(f, delimiter='\t')
            if check == False:
                w.writerow(data.keys())
                check = True
            w.writerow(data.values())

    j = j + 1
    if j == 39:
        time.sleep(10)
        j = 0
