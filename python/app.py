import json
path= 'C:\\Users\\harsha.lulla\\Desktop\\config.json'
f=open(path,encoding = 'utf-8-sig')
#print(f.read)
json_data=json.load(f)
print(json_data)