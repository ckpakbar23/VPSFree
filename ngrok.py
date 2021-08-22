import os
from pyngrok import ngrok, conf
filename = "/root/.ngrok2/ngrok.yml"
if os.path.exists(filename):
    fp = open(filename, "r")
    content = fp.read()
    data = content.split(": ")
    authtoken = data[1]
    ngrok.set_auth_token(authtoken)
    conf.get_default().auth_token = authtoken
    connection_string = ngrok.connect(22, "tcp").public_url
    ssh_url, port = connection_string.strip("tcp://").split(":")
    print(f" **ssh root@{ssh_url} -p{port}**")
    fp.close()
