import json
path2 = '/home/zhangchunkang/token-classification/devition_result/parallel_mono_ner_hineng_5e-5_5_result_xlm-roberta-base/right_mono.json'
path1 = '/home/zhangchunkang/token-classification/devition_result/parallel_mono_ner_hineng_5e-5_5_result_xlm-roberta-base/right_cs.json'
path3 = '/home/zhangchunkang/data/All-CS/new_cs.json'
path4 = '/home/zhangchunkang/data/All-CS/new_mono.json'
choose = ['all_cs.json','all_mono.json','same_len_cs.json','same_len_mono.json','dif_len_cs.json','dif_len_mono.json']
SAVE = '/home/zhangchunkang/token-classification/devition_result/parallel_mono_ner_hineng_5e-5_5_result_xlm-roberta-base/'
#抽出含有实体的三元组抽出不同的{id,tag,label}三元对，观察情况,将原三元对抽出替换掉token，输出形式是两个文件分别记录着与对方不同的含有实体的三元组
#token总数量改变和不改变两种情况

def load(path):
    with open(path,'r') as file:
        a = json.load(file)
    return a

def compare(a,b):
    for i in range(len(a)):
        if a[i]==b[i]:
            a[i]=0
            b[i]=0
    while 0 in a and 0 in b:
        a.remove(0)
        b.remove(0)
    return a,b

def new_trio(dataset,index,save_filename):
    for i in index:
        tt = int(i["id"])-1
        c = dataset[tt]
        i["language"] = c["tokens"]
    write(index,save_filename)
    return index

def write(a,save_filename):
    file = open(save_filename, 'a')
    for i in a:
        file.write(str(i))
        file.write('\n')
    file.close()

def same_length(cs,mono):
    c=[]
    d=[]
    e=[]
    f=[]
    for i in range(len(cs)):
        if len(cs[i]["tokens"])==len(mono[i]["tokens"]):
            c.append(cs[i])
            d.append(mono[i])
        elif len(cs[i]["tokens"])!=len(mono[i]["tokens"]):
            e.append(cs[i])
            f.append(mono[i])
    return(c,d,e,f)

def main():
    cs_data = load(path3)
    mono_data = load(path4)
    cs_index = load(path2)
    mono_index = load(path1)
    cs_index,mono_index=compare(cs_index,mono_index)
    new_trio(cs_data,cs_index,SAVE+choose[0])
    new_trio(mono_data,mono_index,SAVE+choose[1])
if __name__ == "__main__":
    main()