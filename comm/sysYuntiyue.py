import time

from comm.get_uuid import get_uuid
from comm.base_interface import BaseInterface

login_header = {"Content-Type": "application/json"}
login_parm = {
    "username": "fangdantest",
    "deviceUnicode": "16afe5c0-bdfe-3110-9698-0cc33122dd4e",
    "password": "dabai521"
}


login_reg =  BaseInterface().baseInterface('user/login', login_parm, login_header ,"post")
print(login_reg)
logindict = dict(login_reg.json())
startDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
header = {"Authorization": logindict["data"]["authorization"], "Content-Type": "application/json"}
uid = str(get_uuid())
tester_ids = 202798
# score = random.randrange(3, 15)
score = 131
item = 17
evaType = 1
parm = {
    "uuid": uid,  # [必填] 测试记录唯一 ID
    "testType": 1,  # [非必需] 测试类型，0: 日常测试，1: 体育考试
    # "evaType": evaType,  # [非必需] 评分标准ID

    "testerId": tester_ids,  # [必填] 测试人员id
    "itemId": item,  # [必填] 项目id
    "score": score,  # 成绩
    "startDate": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),  # [必填] 开始测试时间
    "endDate": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # [必填] 结束测试时间
}
insert_res = BaseInterface().baseInterface("result/insert", parm, header,"post")
print(insert_res.json())