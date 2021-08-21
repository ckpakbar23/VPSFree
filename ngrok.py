import getpass
from pyngrok import ngrok, conf
connection_string = ngrok.connect(22, "tcp").public_url
ssh_url, port = connection_string.strip("tcp://").split(":")
print(f" **ssh root@{ssh_url} -p{port}**")