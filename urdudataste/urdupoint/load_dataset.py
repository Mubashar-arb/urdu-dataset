"""Generate all urdu words list"""

from urduhack.utils.io import pickle_load

RAW_DATA_FILE = "836520-1480025_urdupoint_599376_posts-raw-clean.pkl"
training_data = pickle_load(RAW_DATA_FILE)

# print(training_data[-1])
# print(training_data[0])
#
# print(len(training_data))

for _tuple in training_data:
    post_data = _tuple[1]
    print(post_data)

# for data in training_data:
#     print(data)
#
# print(len(training_data))

# for data in training_data:
#     for match in re.finditer("باہر", data):
#         print(data[match.start() - 5: match.end() + 5])
