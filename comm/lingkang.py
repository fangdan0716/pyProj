# 体测： 领康
import time

from comm.get_uuid import get_uuid
from comm.base_interface import BaseInterface
# startDate = time.strftime("%Y-%m-%d %H:%M:%S")

# print(startDate)
#
# uuid = get_uuid()
# print(str(uuid))
# print(type(str(uuid)))
#E011

uid = str(get_uuid())
header = {"Content-Type": "application/json"}
parm = [{
    "DeviceNo": "RM-TS-BH",  # 【必填】 设备编号
    "Score": 12,  # 【必填】 成绩
    "ExamEvent": "E028",  # // 【必填】 考试项目
    "examDate": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),  # // 【必填】 考试日期
    "IDNumber": "801",  # // 【必填】 学号
    "Remark": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),  # // 【必填】 备注（运动开始时间）
    "source": "RM",  # // 【非必填】 来源
    "itemId": 115,  # // 【非必填】 项目id
    "uuid": uid  # // 【非必填】 成绩唯一uuid
}]

linRes = BaseInterface().baseInterface("/exam-layout/ScoreSubmit?userId=441", parm, header,"post")

# linRes = BaseInterface().baseInterface("/exam-layout/ScoreSubmit?userId=11123", parm, header)
print(linRes.json())
# nines337  E001
"""sprint("E010",3L,"50米跑"),
sit("E009",5L,"坐位体前屈"),
jump("E005",9L,"立定跳远"),
chin("E011",11L,"引体向上"),
situp("E012",12L,"仰卧起坐"),
cross("",13L,"十字跳"),
run1000("E001",14L,"1000米跑"),
run800("E002",15L,"800米跑"),
run50x8("E014",50L,"50米×8往返跑"),
solidball("E006",16L,"实心球"),
ropeskip("E003",17L,"跳绳"),
basketball("E004",18L,"篮球"),
pressup("E026",21L,"俯卧撑"),
bmi("E016",22L,"身高体重"),
volleyball("",23L,"排球垫墙"),
vitalCapac("E007",24L,"肺活量"),
football("E013",25L,"足球"),
highknee("",27L,"高抬腿"),
jumpjack("",28L,"开合跳"),
jumpbackforth("",29L,"前后跳"),
squat("",30L,"深蹲"),
squatjump("",31L,"蹲跳"),
parallelbars("E028",32L,"双杠臂屈伸"),
wordGame("",34L,"单词大作战");
"""
