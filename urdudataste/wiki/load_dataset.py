"""Generate all urdu words list"""

import pickle

with open("wiki_84645_posts-08-Apr-2019-raw.pkl", 'rb') as f:
    training_data = pickle.load(f)

print(training_data[-1])

for data in training_data:
    print(data)
    break

print(len(training_data))
