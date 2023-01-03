import json
FILENAME = '/home/zhangchunkang/data/mul_lid/lid/train.json'
SAVE_FILENAME = '/home/zhangchunkang/data/mul_lid/lid/train_new.json'

def load(filename):
    data = []
    store = []
    count = 0
    ka = open(SAVE_FILENAME,'a+')
    with open(filename, 'r') as fin:
        for line in fin:
            count = count+1
            if count==6:
                ka.write(line)
                count = 0
    return store



def main():
    load(FILENAME)

if __name__ == "__main__":
    main()