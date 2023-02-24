# 需同步的数据量

import time
from comm.get_uuid import get_uuid
from comm.base_interface import BaseInterface

header = {"Content-Type": "application/json"}
parm = {
        "username": "qwe123",
        "deviceUnicode": "16afe5c0-bdfe-3110-9698-0cc33122dd4e",
        "password": "qwe123456"
    }
login_res = BaseInterface().baseInterface("user/login",parm,header,"post")
print(login_res.json())
login_res_dict = dict(login_res.json())
header = {"Content-Type": "application/json","Authorization": login_res_dict["data"]["authorization"]}
# parm= {
#     "dateTime": time.time(),          #// 非必填，时间戳（精确到毫秒）
#     "pageNo": 1,                        #// 页数，从1开始
#     "pageSize": 100                     #// 每页同步数量
# }
#data_sync_tester_res = BaseInterface().baseInterface("tester/sync/data",parm,header,"post")
# print(data_sync_tester_res.json())
parm = {}
data_count_res = BaseInterface().baseInterface("tester/sync/need", parm, header, "get")
print(data_count_res.json())