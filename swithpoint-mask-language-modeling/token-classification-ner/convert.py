import json
FILENAME = '/home/zhangchunkang/data/mul_lid/lid/dev.conll'
SAVE_FILENAME = '/home/zhangchunkang/data/mul_lid/lid/dev.json'
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
            if is_number(k[1]) or k[1] in SUBSENTENCE_BOUNDARY_TOKEN_REGEX:
                token.append(k[1])
                ner_tag.append('xx')
            else:
                token.append(k[1])
                ner_tag.append(k[-1])
        d['id'] = str(count)
        d['tokens'] = token
        d['lid_tags'] = ner_tag
        count = count+1
        token = []
        lid = []
        # for m in ner_tag:
        #     oo.write(m+'\n')
        # oo.write('\n')
        ner_tag = []
        write(d,SAVE_FILENAME)
        d.clear()
    # oo.close()

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