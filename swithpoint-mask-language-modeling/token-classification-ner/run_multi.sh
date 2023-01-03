#!/usr/bin/env bash
# -*- coding:utf-8 -*-
task=ner
language=MULTI_Multilingual
lr=5e-5
epoch=5
model=xlm-roberta-base
seed=17
python run_ner.py \
  --task_name ${task} \
  --model_name_or_path  /home/zhangchunkang/pretrained_model/${model} \
  --train_file /home/zhangchunkang/data/mul_ner/MULTI_Multilingual/train.json \
  --validation_file /home/zhangchunkang/data/mul_ner/MULTI_Multilingual/dev.json \
  --output_dir ./devition_result/${task}_${language}_${lr}_${epoch}_result_${model}_${seed} \
  --do_train \
  --do_eval \
  --learning_rate  ${lr} \
  --num_train_epochs ${epoch} \
  --seed ${seed}
