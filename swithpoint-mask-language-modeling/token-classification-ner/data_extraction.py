import json
# from simhash import Simhash, SimhashIndex
# import jieba
import jionlp as jio
# hanlp.pretrained.tok.ALL
# tok_fine = hanlp.load(hanlp.pretrained.tok.FINE_ELECTRA_SMALL_ZH)
# HanLP = hanlp.pipeline() \
#     .append(hanlp.utils.rules.split_sentence) \
#     .append(tok_fine)
# import hanlp
# tok = hanlp.load(hanlp.pretrained.tok.COARSE_ELECTRA_SMALL_ZH)
# HanLP.append(lambda sents: sum(sents, []))
file = '/home/zhangchunkang/news/beijing_news/beijing.json'
output_file='/home/zhangchunkang/news/beijing_news/beijing_news.json'
# state=["河北","山西","辽宁","吉林","黑龙江","江苏","浙江","安徽","福建","江西","山东","河南","湖北","湖南","广东","海南","四川","贵州","云南","陕西","甘肃","青海","台湾","内蒙古","广西","西藏","宁夏","新疆","北京","天津","上海","重庆","香港","澳门"]
f = open(file)
# 升级 降级 隔离 到访 诊断 筛查 排查 感染者
data = json.load(f)
# news=['观察者网', '中国记协网', '今日头条', '科普网', '中国台湾网', '新京报', '凤凰网', '新浪网', '中国青年网', '虎嗅网', '中国经济网', '人民网', '搜狐网', '中国网', '央广网', '腾讯网', '央视网', '中国新闻周刊', 'kk中国军网', '微信公众号']

key_word1='无症状感染者'
key_word2='密切接触者'
key_word3='密接'
key_word4='阳性'
key_word5='轻型'
key_word6='感染者'
key_word7='确诊病例'
key_word8="核酸筛查"
key_word9='升级'
key_word10='降级'
key_word11="排查"
key_word12="隔离"
key_word=['无症状感染者','密切接触者','密接','阳性','轻型','确诊病例',"核酸筛查",'升级','降级',"排查","隔离"]
flag=0
d={}
for i in data:
    if "北京" in i["title"] :
        for m in key_word:
            if m in i["content"]:
                d["title"]=i["title"]
                d["time"] = i["publish_time"][0:10]
                d["content_segment"]=i["content_segment"]
                break
        with open(output_file, 'a', encoding='utf-8') as output:
            output.write(json.dumps(d, indent=4, ensure_ascii=False) + ',' + '\n')
            d={}

# for i in data:
#     d["time"] = i["publish_time"][0:10]
#     d["province"] = jio.parse_location(i["title"])["province"]
#     d["city"] = jio.parse_location(i["title"])["city"]
#     if "content_segment" in i.keys():
#         for k in range(len(i["content_segment"])):
#             for m in key_word:
#                 if m in i["content_segment"][k]["text"]:
#                     flag=1
#             if flag==0 and k!=len(i["content_segment"])-1:
#                 d["content_segment"] = i["content_segment"][0:k]+i["content_segment"][k+1:]
#             flag=0
#     with open(output_file, 'a', encoding='utf-8') as output:
#         output.write(json.dumps(d, indent=4, ensure_ascii=False) + ',' + '\n')
#         d={}
# for i in data:
#     k=2
#     word = Simhash(tok(i["content"]))
#     if len(index.get_near_dups(word)) == 0:
#         index.add(str(k),word)
#         k=k+1
#         with open(output_file, 'a', encoding='utf-8') as output:
#             output.write(json.dumps(i, indent=4, ensure_ascii=False) + ',' + '\n')
    # if key_word7 in i["content"][0:3] or key_word6 in i["content"][0:2]:
    #     with open(output_file, 'a', encoding='utf-8') as output:
    #         output.write(json.dumps(i, indent=4, ensure_ascii=False) + ',' + '\n')
#感染者 确诊病例
#只保留k[text] 和 i[publish_time][0:10]
# for i in data:
#     if 'content_segment' in i:
#         for k in i["content_segment"]:
#             d={}
#             if key_word6 in k["text"] or key_word7 in k["text"]:
#                 d["province"]=jio.parse_location(i["title"])["province"]
#                 d["city"]=jio.parse_location(i["title"])["city"]
#                 d["date"]=i["publish_time"][0:10]
#                 d["content"]=k["text"]
#                 with open(output_file, 'a', encoding='utf-8') as output:
#                     output.write(json.dumps(d, indent=4, ensure_ascii=False) + ',' + '\n')
    # if i["source"] in news and key_word1 in i["content"] and (key_word2 in i["content"] or key_word3 in i["content"]) and key_word4 in i["content"]:
    # if key_word6 and key_word7 and key_word8 in i["content"]:
    #     with open(output_file,'a',encoding='utf-8') as output:
    #         output.write(json.dumps(i,indent=4,ensure_ascii=False)+','+'\n')
#去重
#模糊schema
#两类信息：带有轨迹的和只有全市综合描述的
#不同地点的定义不同：感染者 病例

#schema模式：
# 1.总体疫情情况:"感染者866、887、888、893、895、896、897、900至913：\
# 为一起聚集性疫情，共21例。5月7日感染者866、887、896、903、907通过社区核酸筛查发现，其余感染者通过密切接触者排查发现。5月9日感染者895诊断为无症状感染者，\
# 5月8日、9日其余感染者诊>断为确诊病例，临床分型均为轻型

#具体感染内容：感染者867、868、871：通过社区核酸筛查发现，为同一家庭成员，现住朝阳区王四营乡燕保百湾家园。5月7日参加社区核酸筛查，\
# 5月8日报告检测结果为阳性，当日感染者867、868诊断为无症状感染者，感染者871诊断为确诊病例，临床分型为普通型。
# 感染者886：通过社区核酸筛查发现，现住朝阳区南磨房乡双龙南里。自述5月6日出现嗓子干痒、咳嗽等症状，5月7日参加社区核酸筛查，5月8日报告检测结果为阳性，当日诊断为确诊病例，临床分型为轻型。

# "感染者108：为感染者101的家人，现住址同感染者101，工作地点为朝阳区八里庄产业园陈家林甲2号联信国际大厦B座。4月4日作为感染者92的次密切接触者进行集中隔离，其间两次核酸检测结果均为阴性，4月7日报告核酸检测结果为阳性，已转至定点医院，
# 综合流行病史、临床表现、实验室检测和影像学检查等结果，当日诊断为确诊病例，临床分型为轻型。
# 2.具体轨迹信息


#北京疫情关键词：通报 北京 庞星火

#基本信息就是：谁（感染者编号）住哪（住址）何时查出（时间）临床分型（）