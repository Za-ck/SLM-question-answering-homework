import json
import copy
from transformers import AutoModelForTokenClassification, AutoTokenizer, XLMRobertaForMaskedLM
import torch
from collections import Counter
import openai
import os

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == '__main__':

    num = 0
    # extra_data_f = open('./extra_data.json', 'w')
    # original_token_list = []
    # generated_token_list = []
    pairs = []
    for str in open('../train.json', 'r'):
        str = json.loads(str)
        for i in range(1, len(str['ner_tags'])):
            # if '-' in str['ner_tags'][i]:
            if 'O' == str['ner_tags'][i] and len(str['tokens'][i]) >= 5:
                data = {}
                print()
                print("num: ", num)
                print(str['ner_tags'][i])
                data['tag'] = str['ner_tags'][i]
                l = copy.deepcopy(str)

                tokens = l['tokens']
                print(tokens[i])
                data['token'] = tokens[i]
                tokens[i] = '<mask>'
                sentence = ' '.join(tokens)
                print(sentence)
                data['sentence'] = sentence

                data['ner_tags'] = str['ner_tags']

                pairs.append(data)
                num += 1
    json.dump(pairs, open('./tag_token_sentence_pairs.json', 'w'))

    # print(Counter(original_token_list))
    # print(Counter(generated_token_list))
