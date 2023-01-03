FILENAME ='/home1/zhangchunkang/transformers/examples/pytorch/token-classification/main_result/ner_hineng_5e-5_45_result_xlm-roberta-large-code-hi-switch_10/predictions.txt'
SAVE_FIILENAME = '/home1/zhangchunkang/transformers/examples/pytorch/token-classification/main_result/ner_hineng_5e-5_45_result_xlm-roberta-large-code-hi-switch_10/ner_hin_eng.txt'

def load(filename):
    data = []
    store = []
    with open(filename, 'r') as fin:
        for line in fin:
            line = line.strip('\n')
            line = line.split(' ')
            store.append(line)
    return store

def write(list_data,file_name):
    count = 0
    file = open(file_name, 'a')
    for a in list_data:
        for i in a:
            count = count+1
            file.write(i)
            file.write('\n')
        file.write('\n')
    file.close()
    print(count)
    print(len(list_data))
write(load(FILENAME),SAVE_FIILENAME)

