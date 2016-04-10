# Automate data cleaning process
# - Creating separate rows for sites with multiple days (EX: A site with
# operations on Tuesday and Thursday will have two rows: one for Tuesday and one
# for Thursday)
# _Caveat_ This cleaning is imperfect and the JSON schema is very tentative.
# There are a number of data issues which might favor alternative or similar
# data schemas.

import csv
import json

# don't just make a dict because order matters for csv reader
json_keys = ["Agency Name", "Site Address", "Phone Number",
             "Food Distribution Day(s)", "Food Distribution Time", "Zip Code",
             "Neighborhood", "Notes"]
json_values = ["name", "address", "phone", "days", "all_times", "zip",
               "neighborhood", "raw_notes"]
json_mapping = dict(zip(json_keys, json_values))

# currently unused
split_mapping = {"days": ["daycode",  # a coded day (0-6 for python days)
                          "interval"],  # (week of the month; 5 is every week)
                 "all_times": ["times",
                               "timecode"],  # the starting hour
                 "raw_notes": ["notes",
                               "Requirements"]}


jsonfile = open('tabula-processed.json', 'wt')
pretty = True

with open('tabula-food-neighborhood.csv', 'rt') as csvfile:
    stripped = (line.replace('\r', '') for line in csvfile)

    for row in csv.DictReader(stripped, json_keys):
        mutated_row = {}
        for k in row.keys():
            try:
                v = str(row[k])  # should catch an error here...
                mutated_row[json_mapping[k]] = v
            except:
                # print(v)
                # print(k)
                pass

        for i in xrange(len(mutated_row["days"].replace('&', ',').split(','))):
            json.dump(mutated_row, jsonfile)
            if pretty:
                jsonfile.write('\n')

    csvfile.close()
    jsonfile.close()
