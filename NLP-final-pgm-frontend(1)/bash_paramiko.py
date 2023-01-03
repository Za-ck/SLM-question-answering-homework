import paramiko
import do_json

def run_bash():

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 与服务器建立连接，分别用于控制与文件传输
    ssh.connect(hostname="", port=22, username='', password='')
    t = paramiko.Transport(("", 22))
    t.connect(username="", password='')
    sftp = paramiko.SFTPClient.from_transport(t)

    # 将前端接收到的输入上传到服务器
    sftp.put("{FILE_PATH}/docs/test_input.json", "{REMOTE_PATH}/test_input.json")

    # 运行脚本，调用模型
    # ssh.exec_command("source activate lince")
    stdin, stdout, stderr = ssh.exec_command("cd {REMOTE_PATH}; \
                     bash run_ner_test.sh")

    print(str(stdout.read()))
    print(str(stderr.read()))

    # 下载运行结果到本地
    sftp.get("{REMOTE_PATH}/predictions.txt", "{LOCAL_PATH}/predictions.txt")

    f_re = open("{LOCAL_PATH}/predictions.txt", "r")

    result = str(f_re.readline()).strip().split()
        
    return result
    # 关闭连接
    ssh.close()