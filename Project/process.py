#!/usr/bin/python3

# Imports. NLTK is a mistake



def noun_rules(pos):
    for i in range(0,len(pos)):
        if pos[i]=='N_NN' and (pos[i-1] == 'N_NNP' or pos[i+1] == 'N_NNP'):
            pos[i] = 'N_NNP'
    return pos

def verb_rules(pos):
    print(len(pos))
    for i in range(0,len(pos)):
        # print(i)
        if pos[i] == 'V_VM':
            if pos[i-1] == 'V_VAUX' or pos[i-1] == 'V_VM':
                pos[i] = 'V_VAUX'
        # if pos[i-1]=='V_VM' and pos[i+1]=='V_VAUX':
        #     pos[i]='V_VAUX'

    return pos


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

def search_pos(word):
    with open('hindi_data_sorted.txt') as file:
        lines = file.readlines()
        for line in lines:
            pairs=line.replace('|',' ').split(' ')
            if word==pairs[1]:
                return pairs[2][:-1]
            # print(pairs)
            
def search(line):
    pos=[]
    words=line.split(' ')
    for word in words:
        temp_pos = search_pos(word)
        if temp_pos == None:
            temp_pos = tryassign(word)
        pos.append(temp_pos)
    print(pos)
    pos = verb_rules(pos)
    # pos = noun_rules(pos)
    return pos


# def main():
#     print("Enter a sentence in Hindi")
#     sentence=input()
#     print(search(sentence))

#         if search_pos == None:
#             search_pos = tryassign(word)
#         pos.append(search_pos)
#     verb_rules()
#     noun_rules()
#     for i in range(0, len(words)):
#         print("%s/%s "%(words[i], pos[i]), end="")
#     print()

# main()