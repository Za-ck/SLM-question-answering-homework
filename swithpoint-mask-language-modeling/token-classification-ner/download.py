from transformers import AutoTokenizer, AutoModelForSequenceClassification
model_name = "xlm-roberta-base"
pt_model = AutoModelForSequenceClassification.from_pretrained(model_name,cache_dir ='/home/zhangchunkang/pretrained_model')
