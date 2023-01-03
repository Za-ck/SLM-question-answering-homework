import json
path1 = '/home/zhangchunkang/token-classification/devition_result/parallel_mono_ner_hineng_5e-5_5_result_xlm-roberta-base/mono.json'
path2 = '/home/zhangchunkang/token-classification/devition_result/parallel_mono_ner_hineng_5e-5_5_result_xlm-roberta-base/cs.json'
path3 = '/home/zhangchunkang/token-classification/devition_result/parallel_mono_ner_hineng_5e-5_5_result_xlm-roberta-base/refined_cs.json'
path4 = '/home/zhangchunkang/token-classification/devition_result/parallel_mono_ner_hineng_5e-5_5_result_xlm-roberta-base/refined_mono.json'
SAVE = '/home/zhangchunkang/token-classification/devition_result/parallel_mono_ner_hineng_5e-5_5_result_xlm-roberta-base/id.txt'
#得到两遍都有B且不一致的id并提取
def load(path):
    store = []
    with open(path, 'r') as f:
        for line in f:
            if "B" in line:
                a = line.strip().split('"')
                store.append(a[3])
    return(store)

def write(a,save_filename):
    with open(save_filename,'a') as f:
        for i in a:
            f.write(str(i))
            f.write('\n')

def main():
    store1 = load(path1)
    store2 = load(path2)
    store1.extend(store2)
    store1 = list(map(int,store1))
    store1.sort()
    store = list(set(store1))
    l = open(path3,'a')
    o = open(path4,'a')
    with open(path1, 'r') as f:
        for line in f:
            a = line.strip().split('"')
            for i in store:
                if i==int(a[3]):
                    o.write(line)
                    break
    with open(path2, 'r') as f:
        for line in f:
            a = line.strip().split('"')
            for i in store:
                if i==int(a[3]):
                    l.write(line)
                    break
    o.close()
    l.close()
    write(store,SAVE)

if __name__ == "__main__":
    main()