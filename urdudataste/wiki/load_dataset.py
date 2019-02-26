"""Generate all urdu words list"""

import pickle

from xplore.config.data import RAW_WIKI_DATA_FILE

with open(RAW_WIKI_DATA_FILE, 'rb') as f:
    training_data = pickle.load(f)

print(training_data[-1])

for data in training_data:
    print(data)
    break

print(len(training_data))
