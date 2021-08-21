import getpass
from pyngrok import ngrok, conf
authtoken = getpass.getpass()
ngrok.set_auth_token(authtoken)
conf.get_default().auth_token = authtoken
connection_string = ngrok.connect(22, "tcp").public_url
ssh_url, port = connection_string.strip("tcp://").split(":")
print(f" **ssh root@{ssh_url} -p{port}**")
