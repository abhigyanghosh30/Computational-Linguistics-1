def main():
    file = open('HindiTrainingData.txt','r')
    for line in file:
        for word in line:
            for char in word:
                if char == '।':
                    print('\n')
            print (word)
main()
