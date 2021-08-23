import requests
import json
response = requests.get("http://localhost:4040/api/tunnels")
data = response.json()
connection_string = data["tunnels"][0]["public_url"]
ssh_url, port = connection_string.strip("tcp://").split(":")
print("######[VPS DATA INFO LOGIN]######")
print(f"HOST\t\t: {ssh_url}\nPORT\t\t: {port}\nUSERNAME\t: root\nPASSWORD\t: VPSFree1324\nCOMMAND\t\t: ssh root@{ssh_url} -p{port}")