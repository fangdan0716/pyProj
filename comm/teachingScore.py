# 体测： 课堂教学接口
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


parm = {
      "uuid": str(get_uuid()),  #【必填】数据唯一id
      "teachingId": 142,        #【必填】 资源包id
      "duration": 230,         #//【必填】 运动时长
      "count": 1,             #//【必填】 运动人数
      "standard" : 112,       #//【必填】 运动标准分
      "tester": [            # //【必填】 人员集合
        {
         "testerId": 72598,           #//【必填】 人员id
         "startDate": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), #// 【必填】 开始测试时间
         "endDate": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),   #// 【必填】 结束测试时间
          "score": 145,             #//【必填】 每个人的运动成绩
          "group": [                #//【必填】 每组运动集合
            {
              "groupId": 1192,         #//【必填】 每组id
              "sportId": 22,         #//【必填】 运动项目id
              "score": 102          #//【必填】 单个项目运动成绩
            },
            {
              "groupId": 1193,
              "sportId": 22,
              "score": 132
            },
            {
              "groupId": 1194,
              "sportId": 15,
              "score": 0
            },
            {
              "groupId": 1195,
              "sportId": 22,
              "score": 102
            },
            {
              "groupId": 1196,
              "sportId": 22,
              "score": 102
            },
            {
              "groupId": 1197,
              "sportId": 15,
              "score": 0
            },
            {
              "groupId": 1208,
              "sportId": 22,
              "score": 90
            },
            {
              "groupId": 1209,
              "sportId": 22,
              "score": 100
            },
            {
              "groupId": 1210,
              "sportId": 15,
              "score": 0
            },
          ]
         }
        #,
        # {
        #   "testerId": 72597,
        #   "score": 1405,
        #   "group": [
        #     {
        #       "groupId": 1,
        #       "sportId": 1,
        #       "score": 102
        #     },
        #     {
        #       "groupId": 1,
        #       "sportId": 2,
        #       "score": 102
        #     },
        #     {
        #       "groupId": 2,
        #       "sportId": 3,
        #       "score": 102
        #     },
        #     {
        #       "groupId": 2,
        #       "sportId": 4,
        #       "score": 102
        #     }
        #  ]
        #}
      ]
    }
teaching_score_res = BaseInterface().baseInterface("teaching/score", parm, header,"post")
print(teaching_score_res.json())