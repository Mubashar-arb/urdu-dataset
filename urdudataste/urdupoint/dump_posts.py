"""Dump Bathak Data"""

import json

from urduhack.utils.io import pickle_dump, pickle_load

new_training_data = []
data = f"6000-53171_urdupoint_45172_posts-raw.pkl"
data_dump = f"6000-199185_urdupoint_146220_posts-raw.pkl"
json_data = "/Users/ikram/WorkPlace/projects/urdu-dataset/urdudataste/urdupoint/urdupoint/posts.json"

training_data = pickle_load(data)

print("Old training data Count:{}".format(len(training_data)))

for data_tuple in training_data:
    new_training_data.append(data_tuple)

print("New training data Count:{}".format(len(new_training_data)))

print(new_training_data[-3])
print(new_training_data[-2])
print(new_training_data[-1])

json_data = json.load(open(json_data))
json_data_list = []
for item in json_data:
    post_data = item['data']
    if len(post_data) < 15:
        print(item)
        continue
    data = (item['url'], post_data)
    json_data_list.append(data)

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
