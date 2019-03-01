"""Generate all urdu words list"""

from urduhack.utils.io import pickle_load

RAW_DATA_FILE = "6000-40442_urdupoint_32847_posts-raw.pkl"
training_data = pickle_load(RAW_DATA_FILE)

print(training_data[-1])
print(training_data[0])

print(len(training_data))

# for _tuple in training_data:
#     post_data = _tuple[1]
#     if len(post_data) < 10:
#         print(_tuple)

# for data in training_data:
#     print(data)
#
# print(len(training_data))

# for data in training_data:
#     for match in re.finditer("باہر", data):
#         print(data[match.start() - 5: match.end() + 5])
