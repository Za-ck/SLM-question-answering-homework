import json
path = '/home/zhangchunkang/data/All-CS/All-CS.json'
MONO_FILENAME='/home/zhangchunkang/data/All-CS/mono_test.json'
CS_FILENAME='/home/zhangchunkang/data/All-CS/cs_test_2.json'

def load_mono(path):
    mono=[]
    with open(path, 'r') as f:
        data = json.load(f)
    for i in data:
        mono.append(i["mono_raw"].strip().split(' '))
    return mono

def load_cs(path):
    cs=[]
    with open(path, 'r') as f:
        data = json.load(f)
    for i in data:
        if len(i["mturk"]) > 0:
            cs.append(i["mturk"][0].strip().split(' '))
        elif len(i["mturk"])==0:
            cs.append(i["mono_raw"].strip().split(' '))
    return cs

def todic(data):
    token = []
    lid = []
    ner_tag = []
    count = 1
    d = {}
    lentoken = 0
    for i in data:
        d['id'] = str(count)
        d['tokens'] = i
        d['lid'] = ['hi']*len(i)
        d['ner_tags'] = ['O']*len(i)
        count = count+1
        lentoken = lentoken+len(i)
        write(d,CS_FILENAME)
        d.clear()
    print(lentoken)

def write(a,save_filename):
    js = json.dumps(a)
    file = open(save_filename, 'a')
    file.write(js)
    file.write('\n')
    file.close()

def main():
    todic(load_cs(path))

if __name__ == "__main__":
    main()