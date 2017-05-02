from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import json
from scipy.sparse.linalg import svds
from sklearn.preprocessing import normalize


def closest_words(word_in, k=50):
    if word_in not in word_to_index: return "Not in vocab."
    sims = words_compressed.dot(words_compressed[word_to_index[word_in],:])
    asort = np.argsort(-sims)[:k+1]
    return [(index_to_word[i],sims[i]/sims[asort[0]]) for i in asort[1:]]


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
                            ngram_range=(1, 3),
                            vocabulary=None)

scripts = [x['lines'] for x in data]
doc_by_vocab = tfidf_vec.fit_transform(scripts)
first, _, third = svds(doc_by_vocab, k=50)
third = third.transpose()


# character_id to index mapping
character_to_index_map = {}
for i, v in enumerate(data):
    character_to_index_map[v['character_id']] = i
    
word_to_index = tfidf_vec.vocabulary_
word_to_index = character_to_index_map
print first.shape
print third.shape
#print third
#word_to_index = [ x for x in data['chara

index_to_word = {i:t for t,i in word_to_index.iteritems()}

words_compressed = normalize(first, axis=1)


# character_id to character_name mapping
id_to_name_map = {}
for i, v in enumerate(data):
    id_to_name_map[v['character_id']] = v['character_name']

print index_to_word
#print closest_words(character_to_index_map[
l =  closest_words(data[0]['character_id'])


# character_id to movie_id mapping
character_to_movie_map = {}
for i, v in enumerate(data):
    character_to_movie_map[v['character_id']] = v['movie_id']

print data[0]['character_id']
for im in range(len(l)):
    print id_to_name_map[l[im][0]], "\t ", character_to_movie_map[l[im][0]]
#print word_to_index
print "***"*100


# Construct an inverted map from feature index to feature value (word) for later use
#index_to_vocab = {i:v for i, v in enumerate(tfidf_vec.get_feature_names())}
index_to_vocab = index_to_word

# Convert doc_by_vocab to numpy array
doc_by_vocab = doc_by_vocab.toarray()




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

    charac_sims = np.empty([len(data), len(data)], dtype=np.float16)

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
    results = []
    for i in reversed(indexes):
        results.append(data[i])

    # return results in sorted order
    return results[:20]


def reduce_matrix(s):
    sims = np.load(s)
    results = np.empty([len(data), 20], dtype=np.float16)
    for i in range(0, len(sims)):
        #results.append(most_similar(i, sims))
        results[i] = most_similar(i, sims)
    return results

sims = compute_similarities()
s = 'ngram_svd_sims_array.npy'
np.save(s, sims)

#hash_matrix = reduce_matrix(s)

#np.save('hash_top20_sims_array.npy', hash_matrix)
