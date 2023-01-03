import json


def form_test_json(input_list):
    count = len(input_list)
    jsontext = {"id":"1", "tokens":[], "lid":[], "ner_tags":[]}
    lid_list = ["en" for _ in range(count)]
    ner_tags_list = ["O" for _ in range(count)]
    jsontext["tokens"] = input_list
    jsontext["lid"] = lid_list
    jsontext["ner_tags"] = ner_tags_list

    jsondata = json.dumps(jsontext)

    f = open("./test_input.json", "w")
    f.write(jsondata)
    f.close()


def form_result_txt():
    f = open("./test_result.json", "r")
    context = f.read()
    data = json.loads(context)
    text = data["tokens"]
    tags = data["ner_tags"]

    f_o = open("../res1.txt", "a+")

    for i in range(len(text)):
        if tags[i] != "O":
            f_o.write(str(text[i]) + "<" + str(tags[i]).split('-')[1] + ">" + " ")
        else:
            f_o.write(str(text[i]) + " ")

    f_o.close()