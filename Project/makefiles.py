import codecs
import os

def generatefile():
    with open('hindi_sentences_with_pos.txt') as file:
        lines = file.read().split('\n')
        for line in lines:
            pairs = line.split(' ')
            for pair in pairs:
                f = codecs.open("word_tag_pair.txt", mode="a",encoding="utf-8")
                word_tag_pair = pair.split('/')
                word=word_tag_pair[0]
                tag=word_tag_pair[1]
                print(word)
                f.write("%s|%s\n"%(word,tag))

def makesentences():
    f = codecs.open("hindi_test_sentences.txt", mode="a",encoding="utf-8")
    with open('hindi_sentences_with_pos.txt') as file:
        lines = file.read().split('\n')
        for line in lines:
            pairs = line.split(' ')
            for pair in pairs:
                word_tag_pair = pair.split('/')
                word=word_tag_pair[0]
                if(word!='NULL' or word!='null'):
                    f.write("%s "%(word))
            f.write("\n")
    f.close()

def test_sentences():
    with open('hindi_test_sentences.txt') as file:
        lines = file.read().split('\n')
        for line in lines:
            os.system('python3 process.py < echo '+line)

def countlines():
    f = open('word_tag_count_hindi.txt','w',encoding='utf-8')
    with open('word_tag_pair.txt') as file:
        lines = file.readlines()
        for line in lines:
            count_lines = 0
            for new_line in lines:
                if line == new_line:
                    count_lines+=1
            f.write("%s|%s"%(count_lines,line))


def numerically(element):
    return int(element.split('|')[0])

def sortlines():
    with open('word_tag_count_hindi.txt') as file:
        lines = file.readlines()
        lines.sort(reverse=True,key=numerically)
        f = open('word_tag_sort_hindi.txt','w',encoding='utf-8')
        for line in lines:
            f.write(line)

