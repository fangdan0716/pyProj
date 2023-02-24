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

    # 体锻
    login_header = {"Content-Type": "application/json"}
    login_url = 'https://yuntiyu-api.dream-sports.cn/exercise/user/exerciseLogin'
    login_parm = {
        "username": "rongmengkeji",
        "deviceId": "16afe5c0-bdfe-3110-9698-0cc33122dd4e",
        "password": "88888888"
        }
    # login_parm = {
    #     "username": "fangdan",
    #     "deviceUnicode": "16afe5c0-bdfe-3110-9698-0cc33122dd4e",
    #     "password": "fangdan2022"
    # }


    login_reg = HttpRequest(login_url, param=json.dumps(login_parm)).http_request('post', headers=login_header)
    print(login_reg.json())
    logindict = dict(login_reg.json())
    startDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    header = {"Authorization": logindict["data"]["authorization"], "Content-Type": "application/json","device-info":"test-0fb3-3e05-a320-1ed7068b4a52","build":"3"}
    print(header)
    insert_url = 'https://yuntiyu-api.dream-sports.cn/exercise/score/insertExercise'
    faceUnicode = ["2242_1234561_2014_2班_M",
        "2244_11223344556677900000_2015_1班_M",
        "70ce1fed5c6b497280f479d331de8880",
        "2257_2021123456_2015_1班_M",
        "4394_11223344556677800000_2014_1班_M",
        "4552_122451_2015_1班_M",
        "1072fcb0aac540998e48814fdc1debe7",
        "5012_20210423140205_2014_1班_M",
        "5013_20210423140744_2015_1班_M",
        "9ad710511fb5471ea73483306ff561cd",
        "5015_654321_2015_1班_F",
        "5021_225637_2015_2班_F",
        "5022_88895_2015_1班_M",
        "5023_52574_2015_1班_M",
        "5053_256989_2015_1班_M",
        "16571_20210527193220_2015_1班_M",
        "16572_20210527193758_2015_1班_M",
        "16573_20210527195245_2015_1班_M",
        "16574_20210527203244_2015_1班_M",
        "16895_20210616181515_2015_1班_M",
        "16899_20210617201919_2014_1班_M",
        "16900_20210617214545_2015_1班_M",
        "16902_88888888_2015_1班_M",
        "17044_20210706144141_2014_2班_M",
        "17045_20210706144215_2015_4班_M",
        "17046_20210706144949_2015_1班_M",
        "17082_20210714144630_2015_6班_M",
        "17088_20210716000000_2015_1班_F",
        "17116_20210209_2015_1班_M",
        "17117_20200123_2015_1班_F",
        "17136_20210901_2014_1班_M",
        "17137_20210902_2014_1班_F",
        "17139_20210904_2015_1班_M",
        "17140_20210905_2015_1班_M",
        "17141_20210906_2015_1班_M",
        "17142_20210907_2015_1班_M",
        "17145_20210910_2015_1班_M",
        "17146_20210911_2015_1班_M",
        "17147_20210912_2015_1班_M",
        "17148_20210913_2015_1班_M",
        "17149_20210914_2015_1班_M",
        "17150_20210915_2015_1班_M",
        "32814_191054_2015_1班_M",
        "33758_202110151140_2015_2班_M",
        "33759_202110151141_2015_1班_M",
        "33760_202110151142_2013_1班_M",
        "34049_202110151143_2014_1班_M",
        "35866_20210333_2014_1班_M"]
    itemids =[
12,
17,
21,
27,
28,
29,
30,
31,
32,
43,
51,
83,
84,
87,
88,
100,
114,
116,
118,
119,
120,
121,
122,
123,
125,
126,
127,
148,
149,
152,
153,
35,
36,
37,
38,
39,
40,
42,
114,
91,
96,
98,
99,
103,
111,
112,
124,
131]
    for i in faceUnicode:
        for j in itemids:
            score = random.randrange(3, 100)
            print(score)
            uid = str(get_uuid())
            insert_parm1 = {
                      "uuid" : uid,
                     "faceUnicode": i,
                     "itemId": j,
                     "itemModel": "single",
                     "itemAttr": "60",
                     "score": score,
                     "testDuration":60,
                     "hasBest": 1
                    }

            res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
            #score = score + 1
            print(res_reg.json())
