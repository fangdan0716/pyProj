# 体测：单个记录插入
import time
from comm.get_uuid import get_uuid
from comm.base_interface import BaseInterface

header = {"Content-Type": "application/json"}
parm = {
        "username": "yunnan1",
        "deviceUnicode": "16afe5c0-bdfe-3110-9698-0cc33122dd4e",
        "password": "dabai521"
    }
login_res = BaseInterface().baseInterface("user/login",parm,header,"post")
print(login_res.json())
login_res_dict = dict(login_res.json())
header = {"Content-Type": "application/json","Authorization": login_res_dict["data"]["authorization"]}
    # parm = {}
    # getGrade_res = BaseInterface().baseInterface("organizes/getGrade", parm, header)
    # print(getGrade_res.json())
uid = str(get_uuid())
    # score = random.randrange(3, 15)
score = 123
item = 17
evaType = 1
parm = {
            "uuid": uid,  # [必填] 测试记录唯一 ID
            "testType": 1,  # [非必需] 测试类型，0: 日常测试，1: 体育考试
            #"evaType": evaType,  # [非必需] 评分标准ID

            "testerId": 73592,  # [必填] 测试人员id
            "itemId": item,  # [必填] 项目id
            "score": score,  # 成绩
            "startDate": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),  # [必填] 开始测试时间
            "endDate": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # [必填] 结束测试时间
        }
insert_res = BaseInterface().baseInterface("result/insert", parm, header, "post")
print(insert_res.json())


"""
    76544 于亚丽 女 九年级 7班  
    76800 李坤龙 男 九年级 7班
    73292 st701 男 八年级 1班
    73293 st702 女 八年级 1班
    =Sheet1!$F$49:$H$102
    =Sheet1!$Q$49:$S$102
    """
"801"