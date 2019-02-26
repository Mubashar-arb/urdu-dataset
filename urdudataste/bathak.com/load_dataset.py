"""Generate all urdu words list"""

import pickle

RAW_DATA_FILE = ""
with open(RAW_DATA_FILE, 'rb') as f:
    training_data = pickle.load(f)

print(training_data[-1])
print(training_data[0])

# for data in training_data:
#     print(data)
#
# print(len(training_data))

# for data in training_data:
#     for match in re.finditer("باہر", data):
#         print(data[match.start() - 5: match.end() + 5])
