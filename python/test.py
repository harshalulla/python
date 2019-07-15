import requests
url ='http://10.144.16.161:30100/MediaEwalletManagement/mediagetewalletbalance'
payload = {"merchant":{"merchantCode":"0660090000"}}
r = requests.post(url,json=payload)
print(r.content)