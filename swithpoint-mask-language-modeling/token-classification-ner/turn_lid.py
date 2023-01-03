import argparse

parser = argparse.ArgumentParser(description='Test')
parser.add_argument('--language','-n',help='语言')
parser.add_argument('--folder','-f',help='文件夹')
args = parser.parse_args()

set = ['train','test','dev']
for i in range(len(set)):
    filein = open('/home/zhangchunkang/data/mul_pos/ud-treebanks-v2.9/pos_dataset/UD_'+args.folder+'-GSD/'+args.language+'_gsd-ud-'+set[i]+'.conllu','r')
    fileout = open('/home/zhangchunkang/data/mul_pos/ud-treebanks-v2.9/pos_dataset/UD_'+args.folder+'-GSD/'+args.language+'_'+set[i]+'.conll','a')
    for line in filein:
        if line!='\n':
            fileout.write(line.strip()+'\t'+args.language+'\n')
        elif line=='\n':
            fileout.write(line)
    filein.close()
    fileout.close()