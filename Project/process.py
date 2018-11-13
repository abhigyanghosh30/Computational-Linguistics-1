#!/usr/bin/python3

# Imports. NLTK is a mistake

# Global variables
pos=[]

def noun_rules():
    for i in range(0,len(pos)):
        if pos[i-1] == 'PSP' and pos[i+1][:2] == 'N_NN':
            pos[i] = 'PR_PRF'

def verb_rules():
    for i in range(0,len(pos)):
        if pos[i] == 'V_VM':
            if pos[i-1] == 'V_VAUX' or pos[i-1] == 'V_VM':
                pos[i] = 'V_VAUX'


def tryassign(word):
    if len(word) > 2:
        if word[-2:]=="या":
            return 'N_NN'
    if len(word) > 3:
        if word[-3]=="याँ":
            return 'N_NN'
    if len(word) > 1:
        if word[-1]=="े":
            return 'N_NN'

def search(word):
    with open('word_tag_sorted_hindi.txt') as file:
        lines = file.readlines()
        for line in lines:
            pairs=line.replace('|',' ').split(' ')
            if word==pairs[1]:
                return pairs[2]
            # print(pairs)
            
def main():
    print("Enter a sentence in Hindi")
    sentence=input()
    words=sentence.split(' ')
    for word in words:
        search_pos = search(word)
        if search_pos == None:
            search_pos = tryassign(word)
        pos.append(search_pos)
    verb_rules()
    noun_rules()
    for i in range(0, len(words)):
        print("%s/%s "%(words[i], pos[i]), end="")
    print()

main()