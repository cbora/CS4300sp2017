import json

"""
Reads the json data for the movie

"""

file_name = 'data.json'

with open(file_name) as data_file:
    data = json.load(data_file)
