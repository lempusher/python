#count words, returns words in order of most frequent words first
#my first program that works in command prompt / bash :)
#instructions: countwords.py filename.txt
import sys
import re

def countWords(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
    d = {}
    for word in words:
        word = re.sub('\W','',word).lower()
        if word not in d.keys():
            d[word] = 1
        else: d[word] += 1
    freq = sorted(d, key=d.get, reverse=True)
    for i in freq:
        print(f'{i}: >>> {d[i]} time(s)')

def main():
    countWords(sys.argv[1])
    
if __name__ == '__main__':
    main()
