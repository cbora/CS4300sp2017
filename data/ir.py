from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import json

file_name = 'data.json'

with open(file_name) as data_file:
    data = json.load(data_file)

n_feats = 5000

# character by features 
doc_by_vocab = np.empty([len(data), n_feats])
tfidf_vec = TfidfVectorizer(stop_words='english',
                            max_features=n_feats,
                            min_df=10,
                            max_df=0.8,
                            norm='l2',
                            vocabulary=None)
scripts = [x['lines'] for x in data]
doc_by_vocab = tfidf_vec.fit_transform(scripts)

# Construct an inverted map from feature index to feature value (word) for later use
index_to_vocab = {i:v for i, v in enumerate(tfidf_vec.get_feature_names())}

# Convert doc_by_vocab to numpy array
doc_by_vocab = doc_by_vocab.toarray()

# character_id to index mapping
character_to_index_map = {}
for i, v in enumerate(data):
    character_to_index_map[v['character_id']] = i

# character_id to character_name mapping
id_to_name_map = {}
for i, v in enumerate(data):
    id_to_name_map[v['character_id']] = v['character_name']

# character_id to movie_id mapping
character_to_movie_map = {}
for i, v in enumerate(data):
    character_to_movie_map[v['character_id']] = v['movie_id']



def similarity(charac_id1, charac_id2):
    # Computes the simmilarity between two characters
    index1 = character_to_index_map[charac_id1]
    index2 = character_to_index_map[charac_id2]

    return (
        np.dot(doc_by_vocab[index1], doc_by_vocab[index2]) /
        np.linalg.norm(doc_by_vocab[index1])*np.linalg.norm(doc_by_vocab[index2])
        )

    
def get_n_largest(arr, k=10):
    return np.argpartition(arr, -k)[-k:]


def compute_similarities():
    """
      Computes similarities between pairs of characters
      assigns a score of -1 if a given pair is in the same pair
    """

    charac_sims = np.empty([len(data), len(data)], dtype=np.float32)

    for i, c1 in enumerate(data):
        for j, c2, in enumerate(data):
            if i == j:
                # same character
                charac_sims[i, j] = -2.0
            elif c1['movie_id'] == c2['movie_id']:
                # Same movie
                charac_sims[i, j] = -1.0
            else:
                charac_sims[i, j] = similarity(c1['character_id'], c2['character_id'])
    return charac_sims
    
    
    
def search(query, scores):
    """
     Main function to search for similar movies
     returns index in descending order of similarity scores
    
     :param: query: chacter_id
     :param: scores: 2d array containing similarity scores
     :return array of indexes most similar to the character
    """

    index = character_to_index_map[query]
    row = scores[index]

    t = []
    for i, v in enumerate(row):
        if v < 0:
            # Restrain from adding scores from same movie
            continue
        t.append((v, i))
    return sorted(t)


def pretty_data(indexes):
    """
       Takes indexes and returns corresponding dicts

       

    """

    results = []
    for i in indexes:
        results.append(data[i])
    return data


sims = compute_similarities()

