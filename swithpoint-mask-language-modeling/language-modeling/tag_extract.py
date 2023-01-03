path ='/home/zhangchunkang/det/cs_pretrain/data/es/es_clean.txt'
write_path='/home/zhangchunkang/det/cs_pretrain/data/es/es_tag.txt'
with open(path,'r') as file:
    for line in file:
        b=[]
        a = line.strip().split(' ')
        for i in a:
           b.append(i[-2:])
        file_write = open(write_path,'a')
        file_write.write(' '.join(b)+'\n')
        file_write.close()