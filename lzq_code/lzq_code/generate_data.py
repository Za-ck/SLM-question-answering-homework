import json
import copy
import random
import time

from transformers import AutoModelForTokenClassification, AutoTokenizer, XLMRobertaForMaskedLM
import torch
from collections import Counter
import openai
import os

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == '__main__':

    pairs = json.load(open('./tag_token_sentence_pairs.json', 'r'))
    random.shuffle(pairs)

    instruction = "predict <mask> in hindi or english\n\n"

    original_token_list = []
    generated_token_list = []
    extra_data_f = open('./extra_data.json', 'w')
    for i in range(1500, 3000):
        print('\n--', i)

        random.seed(i)
        random.shuffle(pairs)
        examples = ""
        examples += pairs[0]['sentence'] + ', the <mask> is ' + pairs[0]['token'] + '\n'
        examples += pairs[1]['sentence'] + ', the <mask> is ' + pairs[1]['token'] + '\n'
        examples += pairs[2]['sentence'] + ', the <mask> is ' + pairs[2]['token'] + '\n'

        input_str = instruction + examples + pairs[3]['sentence'] + ', the <mask> can be {0} or'.format(pairs[3]['token'])
        print(input_str)
        p = pairs[3]
        original_token_list.append(pairs[3]['token'])

        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=input_str,
            temperature=0.7,
            max_tokens=2,
            top_p=1,
            best_of=2,
            frequency_penalty=0,
            presence_penalty=0.8,
            stop=["\n"])

        result = response['choices'][0]['text'].strip()
        generated_token_list.append(result)

        print(p['tag'])
        print(result)

        data = {'tokens': json.dumps(pairs[3]['sentence'].split()), 'ner_tags': pairs[3]['ner_tags']}
        data['tokens'] = json.loads(data['tokens'].replace('<mask>', result))
        extra_data_f.write(json.dumps(data) + '\n')
        extra_data_f.flush()
        time.sleep(2)

    print()