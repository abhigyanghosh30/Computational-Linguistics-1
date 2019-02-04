#!/bin/python3
import nltk,sys

def main():
    file = open('testing.txt','r')
    for line in file:
        list_of_POS = nltk.pos_tag(nltk.word_tokenize(line))
        for (x,y) in list_of_POS:
            sys.stdout.write(x+','+y+'\n')
        sys.stdout.write('\n')
main()