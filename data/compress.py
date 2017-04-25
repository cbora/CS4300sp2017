import numpy as np
import json


file_name = 'data.json'

with open(file_name) as data_file:
    data = json.load(data_file)


def most_similar(index, scores):
    row = scores[index]

    t = []
    for i, v in enumerate(row):
        if v < 0:
            # do not add it this score (either from same movie or same character)
            continue
        t.append((v, i))

    t = sorted(t)
    indexes = [x[1] for x in t]
    r = []
    for i in reversed(indexes):
        r.append(i)
    return r[:20]

def reduce_matrix(s):
    sims = np.load(s)
    results = np.empty([len(data), 20], dtype=np.float16)
    for i in range(0, len(sims)):
        #results.append(most_similar(i, sims))
        r = most_similar(i, sims)
        results[i] = r
    return results



s = 'svd_sims_array.npy'


hash_matrix = reduce_matrix(s)

np.save('hash_top20_sims_array.npy', hash_matrix)
