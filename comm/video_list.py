# 视频模块 -视频列表
import time
from comm.get_uuid import get_uuid
from comm.base_interface import BaseInterface

login_header = {"Content-Type": "application/json"}
login_parm = {
        "username": "yunnan1",
        "deviceUnicode": "16afe5c0-bdfe-3110-9698-0cc33122dd4e",
        "password": "dabai521"
    }
login_res = BaseInterface().baseInterface("user/login",login_parm,login_header,"post")
print(login_res.json())
logindict = dict(login_res.json())
# print(logindict)
print(logindict["data"]["authorization"])
startDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
header = {"Authorization": logindict["data"]["authorization"]}
uid = str(get_uuid())

parm = {}
rank_reg = BaseInterface().baseInterface('/admin/video/list', parm, header, "get")
print(rank_reg.json())
