import jsonlines
import json
event=['筛查', '管控', '接触', '风险升级', '风险降级', '确诊', '到访', '隔离']
filename='/home/zhangchunkang/liudiao/filtered_news_v6.json'
outputfile='/home/zhangchunkang/liudiao/filtered_news_v7.json'
wrong_example=["朱某某的父亲、姐姐、表哥", "病例6", "病例30", "病例34", "感染者159", "感染者160、161、162、179", "感染者163、165", "感染者164", "感染者166", "感染者167、170", "感染者168、169", "感染者171", "感染者172", "感染者173", "感染者174、175", "感染者176", "感染者177", "感染者178", "感染者514", "感染者516、517", "感染者518", "感染者519", "感染者520", "感染者521", "感染者522", "感染者523至526、528至531", "感染者523、529、530", "感染者527", "感染者496", "感染者497", "感染者498", "感染者499", "500", "感染者501", "感染者502、515", "感染者504", "感染者510", "感染者513", "感染者537", "感染者538", "感染者492", "感染者493", "感染者495", "感染者505", "感染者512", "感染者532", "感染者533", "感染者489", "感染者494", "感染者503", "感染者506", "感染者507", "感染者534", "感染者491", "感染者511", "感染者535", "感染者536", "感染者490", "508", "509", "病例1", "病例2", "病例3", "病例4", "病例5", "病例7"]
right_example=["诊断", "确诊", "新增", "检测结果阳性", "阳性", "无症状", "无症", "感染中招", "呈阳性", "确定"]
words=["感染者","密切接触者","密接","阳性"]
rightone=["通报","疫情","感染","新冠肺炎","无症状"]
true_words=["核酸","感染者","密切接触者","密接","阳性","病例","风险地区","隔离"]
CHINESE_PUNCTUATIONS = u"！？｡。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."
SENTENCE_BOUNDARY_TOKEN_REGEX = r'[。]|[!?！？\n]+'
SUBSENTENCE_BOUNDARY_TOKEN_REGEX = r'[。，；;]|[!?！？]+'
e=[]
c=[]
event=[]
d={}
new_offset=[]
sentence_item=[]
segment_item=[]
count=0
around_sentence=0
around_piece=0
position=[]
number=4
def filter(file,outputfile):
    with open(file,'r') as f:
        data = json.load(f)
    for item in data:
        flag=0
        for word in words:
            if word in item["title"]:
                flag=1
        if flag==1:
            with open(outputfile,'a') as f:
                json.dump(item,f,indent=4,ensure_ascii=False)
                f.write(',')
                f.write('\n')

def segment_filter(file,outputfile):
    d={}
    qualified=[]
    with open(file,'r') as f:
        data = json.load(f)
    for item in data:
        d["time"]=item["time"]
        d["title"]=item["title"]
        for k in item["content_segment"]:
            for word in true_words:
                if word in k["text"]:
                    qualified.append(k)
                    break
        if len(qualified)!=0:
            d["content_segment"]=qualified
            with open(outputfile,"a") as f:
                json.dump(d,f,indent=4,ensure_ascii=False)
                f.write(',')
                f.write('\n')
        d={}
        qualified=[]

def only(file,outputfile):
    count=0
    d = {}
    qualified = []
    flag=0
    with open(file, 'r') as f:
        data = json.load(f)
    for i in range(1,len(data)):
        for k in range(1,10):
            c=i-k
            e=i+k
            if i-k<0:
                c=0
            if i+k>len(data)-1:
                e=len(data)-1
            if data[i]["title"] == data[c]["title"] or data[i]["title"] == data[e]["title"]:
                flag=1
        if flag==0:
            d["time"] = data[i]["time"]
            d["title"] = data[i]["title"]
            for k in data[i]["content_segment"]:
                for word in words:
                    if word in k["text"]:
                        qualified.append(k)
                        break
        if len(qualified) >= 4:
            d["content_segment"] = qualified
            with open(outputfile, "a") as f:
                count=count+1
                json.dump(d, f, indent=4, ensure_ascii=False)
                f.write(',')
                f.write('\n')
        d = {}
        flag=0
        qualified = []
    print(count)

def read(file):
    with open(file,'r+') as f:
        l = open(outputfile, 'a')
        for item in jsonlines.Reader(f):
            l.write('[')
            for i in item["event"]:
                d["type"]=i['type']
                d["text"]=i["text"]
                d["offset"]=i["offset"]
                l.write(str(d))
                l.write(',')
            l.write(']')
            l.write('\n')
        l.close

def calculate_cross(file,outputfile,number):
    with open(file,'r+') as f:
        outfile = open(outputfile, 'a')
        for item in jsonlines.Reader(f):
            for i in item["event"]:
                if event[number] in i["type"]:
                    count=count+1
                    for k in range(1,len(i["args"])):
                        q=i["offset"][-1]
                        w=i["args"][0]["offset"][0]
                        e=i["args"][k-1]["offset"][-1]
                        r=i["args"][k]["offset"][0]
                        if "\n" in item["text"][q:w]:
                            segment_item.append(i["args"][0]["type"]+":"+i["args"][0]["text"])
                            around_sentence=around_sentence+1
                            break
                        elif "。" in item["text"][q:w]:
                            sentence_item.append(i["args"][0]["type"]+":"+i["args"][0]["text"])
                            around_piece=around_piece+1
                            break
                        if "\n" in item["text"][e:r]:
                            segment_item.append(i["args"][k]["type"]+":"+i["args"][k]["text"])
                            around_sentence = around_sentence+1
                            break
                        elif "。" in item["text"][e: r]:
                            sentence_item.append(i["args"][k]["type"]+":"+i["args"][k]["text"])
                            around_piece = around_piece+1
                            break
        d["event"]=event[number]
        d["cross_segment"]=around_sentence/count
        d["cross_sentence"]=around_piece/count
        d["cross_segment_item"]=segment_item
        d["cross_sentence_item"]=sentence_item
        outfile=open(outputfile,'a')
        outfile.write(str(d))
        outfile.write('\n')
        outfile.close()

def alternation(file,outputfile):
    with open(file,'r+') as f:
        outfile = open(outputfile, 'a')
        for item in jsonlines.Reader(f):
            for i in item["event"]:
                change_lines=[]
                for ll in range(len(item["text"])):
                    if item["text"][ll] in "\n":
                        change_lines.append(ll)
                if i["type"]=="确诊" and i["text"] in wrong_example:
                    new_offset=[]
                    for m in right_example:
                        for kk in range(len(change_lines)):
                            if i["offset"][0]>change_lines[kk] and i["offset"][-1]<change_lines[kk+1]:
                                position_before=change_lines[kk]
                                position_after=change_lines[kk+1]
                                break
                        if m in item["text"][position_before:position_after]:
                            i["text"]=m
                            for k in range(0,len(m)):
                                new_offset.append(item["text"].index(m[k],position_before,position_after))
                            break
                    i["offset"]=new_offset
                    event.append(i)
                else:
                    event.append(i)
            d["text"]=item["text"]
            d["event"]=item["event"]
            outfile.write(str(d))
            outfile.write('\n')
        outfile.close()

def delete_cross(file,outputfile):
    outfile = open(outputfile, 'a')
    with open(file,'r+') as f:
        for item in jsonlines.Reader(f):
            for i in item["event"]:
                for k in range(1,len(i["args"])):
                    q=i["offset"][-1]
                    w=i["args"][0]["offset"][0]
                    e=i["args"][k-1]["offset"][-1]
                    r=i["args"][k]["offset"][0]
                    if "\n" in item["text"][q:w]:
                        item["text"]=item["text"].replace(item["text"][q:w],item["text"][q:w].replace('\n',''))
                    elif "。" in item["text"][q:w]:
                        item["text"]=item["text"].replace(item["text"][q:w],item["text"][q:w].replace('。',','))
                    if "\n" in item["text"][e:r]:
                        item["text"]=item["text"].replace(item["text"][e:r],item["text"][e:r].replace('\n',''))
                    elif "。" in item["text"][e:r]:
                        item["text"]=item["text"].replace(item["text"][e:r],item["text"][e:r].replace('。',','))
            outfile=open(outputfile,'a')
            outfile.write(str(item))
            outfile.write('\n')
    outfile.close()

# def test(file,outputfile):
#     with open(file,'r+') as f:
#         for item in jsonlines.Reader(f):
#             for i in item["event"]

def str_split(text, target=SENTENCE_BOUNDARY_TOKEN_REGEX):
    """
    :param text:
    :param target:
    :return:
        [(start1, end1),
         (start2, end2),
         (start3, end3),
         ]
    """
    assert target is not None
    import re
    ret = [(m.start(), m.end()) for m in re.finditer(target, text)]
    if len(ret) == 0:
        return [(0, len(text))]
    sentence_list = list()
    pre_end = 0
    for start, end in ret:
        sentence_list += [{'start': pre_end, 'length': start - pre_end + 1}]
        pre_end = end
    if pre_end != len(text):
        sentence_list += [{'start': pre_end, 'length':  len(text)}]
    return sentence_list

def cut(file,outputfile):
    event_number=[]
    new_offset=[]
    d={}
    new_event=[]
    head=0
    kk=open(outputfile,'a')
    with open(file,'r+') as f:
        for item in jsonlines.Reader(f):
            for i in range(1,len(item["text"])):
                if item["text"][i]=='\n':
                    new_text=item["text"][head:i]
                    pre_head=head
                    head=i+1
                    d["text_segment"]=new_text
                    for k in item["event"]:
                        event_number.append(k["offset"][-1])
                        for mm in k["args"]:
                            event_number.append(mm["offset"][-1])
                        event_number.sort()
                        event_max=event_number[-1]
                        event_min=event_number[0]
                        event_number=[]
                        if i >= event_max and pre_head <= event_min:
                            for ll in k["offset"]:
                                new_offset.append(ll-pre_head)
                            k["offset"]=new_offset
                            new_offset=[]
                            for mm in k["args"]:
                                for ll in mm["offset"]:
                                    new_offset.append(ll-pre_head)
                                mm["offset"]=new_offset
                                new_offset=[]
                            new_event.append(k)
                        d["event"]=new_event
                    new_event=[]
                    kk.write(str(d))
                    kk.write('\n')
                    d={}
            head=0
    kk.close()


def align(file,outputfile):
    qq=open(outputfile,'a')
    new_offset=[]
    with open(file,'r+') as f:
        for item in jsonlines.Reader(f):
            for i in item["event"]:
                position_before=i["offset"][0]-3
                if position_before <= 0:
                    position_before=0
                position_after=i["offset"][-1]+3
                m=i["text"]
                for k in range(0, len(m)):
                    new_offset.append(item["text_segment"].index(m[k], position_before, position_after))
                i["offset"]=new_offset
                new_offset=[]
                for ll in i["args"]:
                    m=ll["text"]
                    position_before=ll["offset"][0]-3
                    if position_before<=0:
                        position_before=0
                    position_after=ll["offset"][-1]+3
                    for k in range(0, len(m)):
                        new_offset.append(item["text_segment"].index(m[k], position_before, position_after))
                    ll["offset"]=new_offset
                    new_offset=[]
            d["text"]=item["text_segment"]
            d["event"]=item["event"]
            qq.write(str(d))
            qq.write('\n')
    qq.close()

def max(file):
    qq = open(outputfile, 'a')
    new_offset = []
    index=[]
    with open(file, 'r+') as f:
        for item in jsonlines.Reader(f):
            new_offset.append(len(item["text"]))
    for i in range(len(new_offset)):
        if new_offset[i]>512:
            index.append(i+1)
    print(index)

only(filename,outputfile)
#事件信息集中到一个句子里面了现在就是要把他们分割开看