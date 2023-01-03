#!/usr/bin/env bash
# -*- coding:utf-8 -*-
task=ner
num=2
model=cs-roberta-large-hi
language=hineng
lr=5e-5
epoch=10
seed1=17
seed2=45
seed3=36

CUDA_VISIBLE_DEVICES=${num} python run_ner.py \
  --task_name ${task} \
  --model_name_or_path  /home1/zhangchunkang/pretrained_model/${model} \
  --train_file /home1/zhangchunkang/data/lince_v2/${task}_${language}/train.json \
  --validation_file /home1/zhangchunkang/data/lince_v2/${task}_${language}/dev.json \
  --test_file /home1/zhangchunkang/data/lince_v2/${task}_${language}/test.json \
  --output_dir ./main_result/${task}_${language}_${lr}_${seed1}_result_${model}_${epoch} \
  --learning_rate  ${lr} \
  --num_train_epochs ${epoch} \
  --seed ${seed1} \
  --do_train \
  --do_eval \
  --do_predict
cd main_result/${task}_${language}_${lr}_${seed1}_result_${model}_${epoch}
rm -r checkpoint-*
cd ../..

CUDA_VISIBLE_DEVICES=${num} python run_ner.py \
  --task_name ${task} \
  --model_name_or_path  /home1/zhangchunkang/pretrained_model/${model} \
  --train_file /home1/zhangchunkang/data/lince_v2/${task}_${language}/train.json \
  --validation_file /home1/zhangchunkang/data/lince_v2/${task}_${language}/dev.json \
  --test_file /home1/zhangchunkang/data/lince_v2/${task}_${language}/test.json \
  --output_dir ./main_result/${task}_${language}_${lr}_${seed2}_result_${model}_${epoch} \
  --learning_rate  ${lr} \
  --num_train_epochs ${epoch} \
  --seed ${seed2} \
  --do_train \
  --do_eval \
  --do_predict

cd main_result/${task}_${language}_${lr}_${seed2}_result_${model}_${epoch}
rm -r checkpoint-*
cd ../..

CUDA_VISIBLE_DEVICES=${num} python run_ner.py \
  --task_name ${task} \
  --model_name_or_path  /home1/zhangchunkang/pretrained_model/${model} \
  --train_file /home1/zhangchunkang/data/lince_v2/${task}_${language}/train.json \
  --validation_file /home1/zhangchunkang/data/lince_v2/${task}_${language}/dev.json \
  --test_file /home1/zhangchunkang/data/lince_v2/${task}_${language}/test.json \
  --output_dir ./main_result/${task}_${language}_${lr}_${seed3}_result_${model}_${epoch} \
  --learning_rate  ${lr} \
  --num_train_epochs ${epoch} \
  --seed ${seed3} \
  --do_train \
  --do_eval \
  --do_predict
cd main_result/${task}_${language}_${lr}_${seed3}_result_${model}_${epoch}
rm -r checkpoint-*
cd ../../true_results
mkdir ${task}_${language}_${model}_${lr}_${epoch}
cd ../main_result
cd ${task}_${language}_${lr}_${seed1}_result_${model}_${epoch}
sed -n '4p' eval_results.json > /home1/zhangchunkang/ner/true_results/${task}_${language}_${model}_${lr}_${epoch}/eval.txt
cd ../${task}_${language}_${lr}_${seed2}_result_${model}_${epoch}
sed -n '4p' eval_results.json >> /home1/zhangchunkang/ner/true_results/${task}_${language}_${model}_${lr}_${epoch}/eval.txt
cd ../${task}_${language}_${lr}_${seed3}_result_${model}_${epoch}
sed -n '4p' eval_results.json >> /home1/zhangchunkang/ner/true_results/${task}_${language}_${model}_${lr}_${epoch}/eval.txt
cd ../../
python calculate.py --input_path true_results/${task}_${language}_${model}_${lr}_${epoch}/eval.txt
