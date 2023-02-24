import random
import time
import requests
import json
from comm.do_excel_new import DoExcel
from comm.read_conf import ReadConfig
from comm.get_uuid import get_uuid


class HttpRequest:
    def __init__(self,url,param):
        self.url=url
        self.param=param


    def http_request(self,method,headers=None):
        if method.upper()=="GET":
            res=requests.get(self.url,self.param,headers=headers)

        elif method.upper()=="POST":
            res=requests.post(self.url,self.param,headers=headers)

        else:
            print("请求的方式不存在")

        return res


if __name__ == '__main__':
    """体测"""
    login_header = {"Content-Type": "application/json"}
    login_url = 'http://yuntiyu-test.dream-sports.cn/tice/user/login'
    login_parm = {
        "username": "yunnan1",
        "deviceUnicode": "16afe5c0-bdfe-3110-9698-0cc33122dd4e",
        "password": "dabai521"
    }
    # login_url = 'https://yuntiyu-api.dream-sports.cn/tice/user/login'
    # login_parm = {
    #     "username": "rongmengkeji",
    #     "deviceUnicode": "16afe5c0-bdfe-3110-9698-0cc33122dd4e",
    #     "password": "88888888"
    #     }
    # login_parm = {
    #     "username": "fangdan",
    #     "deviceUnicode": "16afe5c0-bdfe-3110-9698-0cc33122dd4e",
    #     "password": "fangdan2022"
    # }


    login_reg = HttpRequest(login_url, param=json.dumps(login_parm)).http_request('post', headers=login_header)
    print(login_reg)
    logindict = dict(login_reg.json())
    startDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    header = {"Authorization": logindict["data"]["authorization"], "Content-Type": "application/json"}
    insert_url = 'http://yuntiyu-test.dream-sports.cn/tice/result/insert'
    # insert_url = 'https://yuntiyu-api.dream-sports.cn/tice/result/insert'
    #tester_ids = [73394]

    #fangdan  T测试32
    tester_ids = [68288]
    #tester_ids = [73395,73396]
    #tester_ids = [73392]
    # sys  fangdantest
    #tester_ids = [191123]  #9年级 M  test01
    #tester_ids = [170952]  #8年级 F  st114
    #tester_ids = [187904]  #9年级 M  346张三
    #tester_ids = [187648]  #9年级 F  90张三
    #tester_ids = [159195]  #5年级 女  st017
    #tester_ids = [159195]  #5年级 女  st017

    # sys fangdan
    # tester_ids = [152418]  #5年级 男  st311
    """rongmengkeji"""
    # tester_ids = [139520,
                    # 186368,
                    # 129280,139521,
                    # 34049,
                    # 166401,
                    # 186369,
                    # 129281,
                    # 186370,
                    # 129282,
                    # 16899,
                    # 166403,
                    # 129283,
                    # 139524,
                    # 16900,
                    # 166404,
                    # 186372,
                    # 129284,
                    # 47109,
                    # 186373,
                    # 129285,
                    # 16902,
                    # 186374,
                    # 129286,
                    # 186375,
                    # 129287,
                    # 186376,
                    # 129288,
                    # 186377,
                    # 129289,
                    # 186378,
                    # 129290,
                    # 186379,
                    # 129291,
                    # 186380,
                    # 129292,
                    # 186381,
                    # 129293,
                    # 186382,
                    # 129294,
                    # 186383,
                    # 126991,
                    # 129295,
                    # 186384,
                    # 129296,
                    # 186385,
                    # 129297,
                    # 186386,
                    # 129298,
                    # 186387]

    # uid = str(get_uuid())
    # insert_parm1 ={
    #       "uuid": uid,   #[必填] 测试记录唯一 ID
    #       "testType" : 1,                               # [非必需] 测试类型，0: 日常测试，1: 体育考试
    #       "evaType": 7,                                 # [非必需] 评分标准ID
    #       "testerId": 73394,                               # [必填] 测试人员id
    #       "itemId": 17,                                 # [必填] 项目id  76800 李  76544 于  72592  生产：9年级：187904 男 ，187648：女
    #       "score": 145,                                 # 成绩a
    #       "startDate": startDate,           #[必填] 开始测试时间
    #       "endDate": startDate             #[必填] 结束测试时间
    #
    #     }
    # res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
    # print(res_reg.json())
    # 22
    # 身高
    # 178
    # 85
    # 体重
    # 42

    item = 11  #11    #21
    for i in tester_ids:
        score = random.randrange(3, 15)
        print(score)
        uid = str(get_uuid())
        insert_parm1 = {
            "uuid": uid,  # [必填] 测试记录唯一 ID
            "testType": 1,  # [非必需] 测试类型，0: 日常测试，1: 体育考试
            "evaType": 1,  # [非必需] 评分标准ID

            "testerId": i,  # [必填] 测试人员id
            "itemId": item,  # [必填] 项目id  76800 李  76544 于  72592  生产：9年级：187904 男 ，187648：女
            "score": score,  # 成绩a
            "startDate": startDate,  # [必填] 开始测试时间
            "endDate": startDate  # [必填] 结束测试时间

        }
        res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
        #score = score + 1
        print(res_reg.json())
