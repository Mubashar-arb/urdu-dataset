"""Dump Bathak Data"""

import json

from urduhack.utils.io import pickle_dump

new_training_data = []
data = "/Users/ikramali/Projects/Python/Xplore/data/125-172908_bathak_51986_posts-raw.pkl"
data_dump = f"86686_arynews_posts-raw.pkl"
json_data = "/Users/ikram/WorkPlace/projects/urdu-dataset/urdudataste/express/express/posts.json"

# with open(data, 'rb') as f:
#     training_data = pickle.load(f)
#
# print("Old training data Count:{}".format(len(training_data)))
#
# for data_tuple in training_data:
#     new_training_data.append(data_tuple)
#
# print("New training data Count:{}".format(len(new_training_data)))
#
# new_training_data = sorted(new_training_data, key=lambda x: int(x[0]))
#
# print(new_training_data[-3])
# print(new_training_data[-2])
# print(new_training_data[-1])

json_data = json.load(open(json_data))
json_data_list = []
for item in json_data:
    data = (item['url'], item['data'])
    print(item['url'])
    print(item['data'])
    json_data_list.append(data)
exit()
print("Json training data Count:{}".format(len(json_data_list)))

print(json_data_list[0])
print(json_data_list[1])
print(json_data_list[2])

# last post
print(json_data_list[-3])
print(json_data_list[-2])
print(json_data_list[-1])

for data_tuple in json_data_list:
    new_training_data.append(data_tuple)

print("New training data Count:{}".format(len(new_training_data)))

print(new_training_data[0])
print(new_training_data[-2])
print(new_training_data[-1])

pickle_dump(data_dump, new_training_data)
