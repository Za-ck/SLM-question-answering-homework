import json
FILENAME = '/home/zhangchunkang/token-classification/devition_result/parallel_mono_ner_hineng_5e-5_5_result_xlm-roberta-base/mono.conll'
SAVE_FILENAME = '/home/zhangchunkang/token-classification/devition_result/parallel_mono_ner_hineng_5e-5_5_result_xlm-roberta-base/mono.json'
SUBSENTENCE_BOUNDARY_TOKEN_REGEX = '。，；;!?！？'

def load(filename):
    data = []
    store = []
    with open(filename, 'r') as fin:
        for line in fin:
            if line=='\n':
                store.append(data)
                data = []
            else:
                line = line.strip('\n')
                line = line.split('\t')
                data.append(line)
    return store

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def todic(data):
    token = []
    lid = []
    ner_tag = []
    count = 1
    d = {}
    # oo = open('try.txt', 'a')
    for i in data:
        for k in i:
            token.append(k[0])
        d['id'] = str(count)
        d['tokens'] = token
        count = count+1
        token = []
        write(d,SAVE_FILENAME)
        d.clear()


def write(a,save_filename):
    js = json.dumps(a)
    file = open(SAVE_FILENAME, 'a')
    file.write(js)
    file.write('\n')
    file.close()

def main():
    todic(load(FILENAME))

if __name__ == "__main__":
    main()