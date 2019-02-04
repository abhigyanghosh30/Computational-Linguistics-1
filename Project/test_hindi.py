#! /usr/bin/python3
import process

file_to_write=open("test_hindi_9.txt","w")
with open('hindi_test_sentences.txt') as file:
    lines = file.readlines()
    for line in lines:
        words = line.split(' ')
        words.remove('\n')
        pos_list = process.search(line)
        for i in range(0,len(pos_list)-1):
            file_to_write.write(words[i]+"|"+pos_list[i]+"\n")