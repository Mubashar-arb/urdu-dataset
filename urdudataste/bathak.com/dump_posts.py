"""Dump Bathak Data"""

import json
import pickle

from urduhack.utils.io import pickle_dump

new_training_data = []
data = "/Users/ikramali/Projects/Python/Xplore/data/125-172908_bathak_51986_posts-raw.pkl"
data_dump = f"/Users/ikram/WorkPlace/dataset/Urdu/bathak/125-192971_bathak_57219_posts-raw.pkl"
json_data = "/Users/ikram/WorkPlace/projects/scrapy-crawlers/bathak.com/posts/posts/posts.json"

with open(data, 'rb') as f:
    training_data = pickle.load(f)

print("Old training data Count:{}".format(len(training_data)))

for data_tuple in training_data:
    new_training_data.append(data_tuple)

print("New training data Count:{}".format(len(new_training_data)))

new_training_data = sorted(new_training_data, key=lambda x: int(x[0]))

print(new_training_data[-3])
print(new_training_data[-2])
print(new_training_data[-1])

json_data = json.load(open(json_data))
json_data_list = []
for item in json_data:
    text = item['text']
    try:
        data = (int(item['id']), item['category'], text)
    except ValueError as e:
        print(e)
    json_data_list.append(data)

print("Json training data Count:{}".format(len(json_data_list)))

json_data_list = sorted(json_data_list, key=lambda x: int(x[0]))

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

new_training_data = sorted(new_training_data, key=lambda x: int(x[0]))

print(new_training_data[0])
print(new_training_data[-2])
print(new_training_data[-1])

pickle_dump(data_dump, new_training_data)
