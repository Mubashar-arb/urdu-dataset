"""Dump Bathak Data"""

from urduhack.utils.io import pickle_dump
from smart_open import smart_open

RAW_WIKI_DATA_FILE = ""
wiki_posts = []
wiki_ur = "wiki.ur.text"
for line_no, line in enumerate(smart_open(wiki_ur)):
    # line = any2unicode(line)
    wiki_posts.append(line)

print(wiki_posts[0])
print(wiki_posts[1])
print(wiki_posts[2])

# last post
print(wiki_posts[-3])
print(wiki_posts[-2])
print(wiki_posts[-1])

print(len(wiki_posts))

pickle_dump(RAW_WIKI_DATA_FILE, wiki_posts)
