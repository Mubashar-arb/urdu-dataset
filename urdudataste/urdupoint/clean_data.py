# coding: utf8
"""Generate all urdu words list"""

from urduhack.preprocess import normalize_whitespace
from urduhack.utils.io import pickle_load

RAW_DATA_FILE = "6000-372218_urdupoint_315316_posts-raw.pkl"
training_data = pickle_load(RAW_DATA_FILE)

for data in training_data:
    post_list = data[1]
    data = []
    print("=" * 100)
    post = ''.join(post_list)
    post = normalize_whitespace(post.strip())
    print(post)
    post = post.replace("googletag.cmd.push(function() { googletag.display('div-gpt-ad-1450742420834-2'); });", '')
    post = post.replace("googletag.cmd.push(function() { googletag.display('div-gpt-ad-1x1'); });", '')
    post = post.replace("googletag.cmd.push(function() { googletag.display('div-gpt-ad-outstream'); });", '')
    post = post.replace("googletag.cmd.push(function() { googletag.display('div-gpt-ad-1531947055150-0'); });", '')
    post = post.replace("googletag.defineSlot('/21678054/up-v2/center', [[336, 280], [300, 250]], "
                        "'div-gpt-ad-1531947055150-0').addService(googletag.pubads());", '')
    post = post.replace("googletag.cmd.push(function() {;", '')
    post = post.replace("(جاری ہے)", '')
    post = post.replace("googletag.cmd.push(function() {", '')
    post = post.replace("});", '')
    post = post.replace("googletag.cmd.push(function() {", '')
    print("#" * 100)
    print(normalize_whitespace(post))

