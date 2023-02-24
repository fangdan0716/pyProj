# 体测： 排行榜
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
header = {"Authorization": logindict["data"]["authorization"], "Content-Type": "application/json"}
uid = str(get_uuid())

parm = {
  "itemId": 17,                                  #// [必填] 项目id
  "rankType": "month",                            #// [必填] 排行榜类型 day-日排行,week-周排行,month-月排行,year-年排行
  #"gradeNumber": 5,
  # "gradeId": 11230,                                 #// [非必填] 年级ID
  # "clazzId": 11253                                  #// [非必填] 班级ID
    }

rank_reg = BaseInterface().baseInterface('result/rank', parm, header, "post")
print(rank_reg.json())
