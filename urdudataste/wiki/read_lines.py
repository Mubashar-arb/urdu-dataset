"""test"""
from smart_open import smart_open
from xplore.utils.text import any2unicode

# Displaying the Results
questions_file = "wiki.en.text"
for line_no, line in enumerate(smart_open(questions_file)):
    line = any2unicode(line)
    print(line)
    print(line_no)
