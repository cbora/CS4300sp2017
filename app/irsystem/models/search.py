import numpy as np
import json
import os
import requests
from StringIO import StringIO
# Load some data into memory


print os.getcwd()

data_file_name = 'data/data.json'
with open(data_file_name) as data_file:
    data = json.load(data_file)

url = "https://s3.amazonaws.com/cs4300/sims_array.npy"
r = requests.get(url)
#scores = np.load('data/sims_array.npy')
scores = np.load(StringIO(r.content))

# character_id to index mapping
character_to_index_map = {}
for i, v in enumerate(data):
    character_to_index_map[v['character_id']] = i


# Load characters in memory
character_file_name = 'data/characters.json'
with open(character_file_name) as ch:
    chars = json.load(ch)

# used for auto fill on the frontend
auto_fill = []
auto_fill_id_map = {}
for x in chars:
    auto_fill.append(x['display'])
    auto_fill_id_map[x['display']] = x['id']

def query_info(query):
    tmp = auto_fill_id_map[query]
    index = character_to_index_map[tmp]
    return data[index]

def process_query(query):
    """
     Function to process query and assumes query is the character id

    """
    tmp= auto_fill_id_map[query]
    index = character_to_index_map[tmp]
    row = scores[index]

    t = []
    for i, v in enumerate(row):
        if v < 0:
            # do not add it this score (either from same movie or same character)
            continue
        t.append((v, i))

    t = sorted(t)
    indexes = [x[1] for x in t]
    results = []
    for i in reversed(indexes):
        results.append(data[i])

    # return results in sorted order
    return results[:20]
