"""test"""
from smart_open import smart_open

# Displaying the Results
questions_file = "wiki.en.text"
for line_no, line in enumerate(smart_open(questions_file, encoding="utf8")):
    print(line)
    print(line_no)
