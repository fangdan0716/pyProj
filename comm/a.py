import time
import json
print(time.time())
str = "\\u5f6d\\u51ef"
print (json.loads('"%s"' %str))

list1  = ['{"testerName": "\\u5f6d\\u51ef", "testerNumber": "680202101077", "gender": "\\u7537", "grade": 7, "clazz": 1}']
json.loads()



