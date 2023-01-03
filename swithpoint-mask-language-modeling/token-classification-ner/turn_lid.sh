#!/usr/bin/env bash
# -*- coding:utf-8 -*-
language=es
fold=Spanish
touch /home/zhangchunkang/data/mul_pos/ud-treebanks-v2.9/pos_dataset/UD_${fold}-GSD/${language}_train.conll /home/zhangchunkang/data/mul_pos/ud-treebanks-v2.9/pos_dataset/UD_${fold}-GSD/${language}_dev.conll /home/zhangchunkang/data/mul_pos/ud-treebanks-v2.9/pos_dataset/UD_${fold}-GSD/${language}_test.conll

python turn_lid.py \
  --language ${language} \
  --folder ${fold}



