import json
import sent_files.sentiment as sentiment
import nltk
import re
import numpy as np

# nltk.download('punkt')

"""
Reads the json data for the movie

"""

# file_name = 'full_data.json'

# with open(file_name) as data_file:
#     data = json.load(data_file)


sentiment_scores = {}

# with open('sent_scores999.txt', 'r') as infile:
# 	dic = json.load(infile)
# 	sentiment_scores.update(dic)

# with open('sent_scores1999.txt', 'r') as infile:
# 	dic = json.load(infile)
# 	sentiment_scores.update(dic)

# with open('sent_scores2999.txt', 'r') as infile:
# 	dic = json.load(infile)
# 	sentiment_scores.update(dic)

# with open('sent_scores3999.txt', 'r') as infile:
# 	dic = json.load(infile)
# 	sentiment_scores.update(dic)

# with open('sent_scores9034.txt', 'r') as infile:
# 	dic = json.load(infile)
# 	sentiment_scores.update(dic)

# with open('sent_scores5999.txt', 'r') as infile:
# 	dic = json.load(infile)
# 	sentiment_scores.update(dic)

# with open('sent_scores6999.txt', 'r') as infile:
# 	dic = json.load(infile)
# 	sentiment_scores.update(dic)

# with open('sent_scores7999.txt', 'r') as infile:
# 	dic = json.load(infile)
# 	sentiment_scores.update(dic)

# # print(len(sentiment_scores))
# # print(sentiment_scores.keys())
# b = range(9035)
# left = [a for a in b if str(a) not in sentiment_scores.keys()]

# print(left)
# for i in left:
# 	for char in data:
# 		if int(char['character_id'][1:]) == i:
# 			c = char
# 	print "Computing character %d" % i
# 	lines = re.split('[.!?]', c['lines'])
# 	lines = [l for l in lines if l != "" and l != " "]
# 	scores = []
# 	for line in lines:
# 		scores.append(sentiment.sentiment_score(line))
# 	sentiment_scores[int(c['character_id'][1:])] = np.mean(scores)

# with open('sentiment_scores.txt', 'w') as outfile:
# 	json.dump(sentiment_scores, outfile)



# with open('sentiment_scores.txt', 'rb') as infile:
# 	sentiment_scores = json.load(infile)

# sentiment_scores = sentiment_scores.items()
# sentiment_scores = [(int(k), v) for (k, v) in sentiment_scores]
# sentiment_scores = sorted(sentiment_scores, key= lambda x: x[0])
# sentiment_scores = [v for (k, v) in sentiment_scores]
# sent_score_similarity_matrix = np.empty((9035, 9035), dtype=np.float16)
# np.outer(sentiment_scores, sentiment_scores, out=sent_score_similarity_matrix)

# with open('sent_matrix.npy', 'w') as outfile:
# 	np.save(outfile, sent_score_similarity_matrix)

