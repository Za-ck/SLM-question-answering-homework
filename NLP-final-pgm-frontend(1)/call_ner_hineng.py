import os
import bash_paramiko
import do_json

f_in = open("{LOCAL_PATH}/docs/input.txt", 'r')
text = f_in.readline().split()

# 调取本地模型时可用
# os.system("{PYTHON PATH}\python.exe run_ner.py \
#             --task_name ner \
#             --model_name_or_path {} \
#             --train_file {} \
#             --validation_file {} \
#             --test_file {} \
#             --output_dir {} \
#             --learning_rate {} \
#             --num_train_epochs {} \
#             --seed {} \
#             --do_eval \
#             --do_predict")

# f_pred = open("{YOUR_FILE_PATH}/predictions.txt", "r")
# res1_pred = f_pred.readline().split()


# 调取服务器上模型时可用

do_json.form_test_json(text)

res1_pred = bash_paramiko.run_bash()

# do_json.form_result_txt()

# 形成结果
f_res1 = open("{LOCAL_PATH}/docs/res1.txt", "w")
f_res1.write("NER Result\n \n")
f_res1.close()

f_res1 = open("{LOCAL_PATH}/docs/res1.txt", "a+")

for i in range(len(res1_pred)):
    if res1_pred[i] != "O":
        f_res1.write(text[i] + "<" + res1_pred[i] + ">" + " ")
    else:
        f_res1.write(text[i] + " ")

f_res1.close()
