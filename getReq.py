import requests
r = requests.get("http://10.144.114.114:31924/errorcode/getErrorCodeMapping?applicationID=RIL4G&componentID=EWalletInformationManagement")
print(r.content)