# 视频模块 - 标签列表
import time
from comm.get_uuid import get_uuid
from comm.base_interface import BaseInterface
from comm.http_request1 import HttpRequest
login_header = {"Content-Type": "application/json"}
login_parm = {
        "username": "yunnan1",
        "deviceUnicode": "16afe5c0-bdfe-3110-9698-0cc33122dd4e",
        "password": "dabai521"
    }
login_res = HttpRequest("http://yuntiyu-test.dream-sports.cn/tice/user/login",login_parm).http_request("post", headers = login_header)
print(login_res.json())
logindict = dict(login_res.json())
# print(logindict)
print(logindict["data"]["authorization"])
startDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
header = {"Authorization": logindict["data"]["authorization"]}
uid = str(get_uuid())

parm = {}
rank_reg = BaseInterface().baseInterface('/admin/video/tag', parm, header, "get")
print(rank_reg.json())
