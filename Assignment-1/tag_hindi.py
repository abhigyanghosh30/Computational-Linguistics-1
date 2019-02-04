from nltk.corpus import indian
from nltk.tag import tnt
import nltk
import sys
def main():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)

    file = open('HindiTrainingData.txt','r')
    for line in file:
        
        list_of_POS = tnt_pos_tagger.tag(nltk.word_tokenize(line))
        for (x,y) in list_of_POS:
            sys.stdout.write(x+','+y+'\n')
        sys.stdout.write('\n')
main()