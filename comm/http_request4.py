import random
import time
from conf import project_path
import requests
import json
from  comm import do_excel_new2
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
    score = random.randint(1,100)
    login_header ={"Content-Type": "application/json"}
    login_url ='http://yuntiyu-test.dream-sports.cn/tice/user/login'
    login_parm ={
                "username": "yunnan1",
              "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb",
              "password": "dabai521"
            }
    login_reg = HttpRequest(login_url, param=json.dumps(login_parm)).http_request('post', headers=login_header)
    logindict =dict(login_reg.json())
    #print(logindict)
    #print(logindict["data"]["authorization"])
    startDate =time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    header = {"Authorization": logindict["data"]["authorization"],"Content-Type": "application/json"}
    insert_url = 'http://yuntiyu-test.dream-sports.cn/tice/result/insert'
    path = project_path.id_data_path
    testers_id_F = do_excel_new2.DoExcel(path, "Sheet1").read_excel1()
    print(testers_id_F)
    items_id = do_excel_new2.DoExcel(path, "Sheet2").read_excel1()
    print(items_id)
    scores_3 = "8.8";       # 50米
    scores_5 = "-1.4";       # 坐位体前屈
    scores_9 = "181";       # 立定跳远
    scores_12 = "32";       # 仰卧起坐
    scores_11 = "3";      # 引体向上
    scores_14 = "315";      # 1000米
    scores_15 = "300";      # 800米
    scores_16 = "9.1";      # 实心球
    scores_17 = "169";      # 双脚跳绳
    scores_92 = "16.8";      # 100米跑
    scores_108 = "302";     # 200米自由泳
    scores_22 = "179";     # 身高
    scores_85 = "41";     # 体重
    scores_24 = "2690";     # 肺活量
    scores_106 = "10";     # 15米x4往返跑
    types_test_eva = do_excel_new2.DoExcel(path, "Sheet4").read_excel1()
    print(types_test_eva)
    # 测试模式： 0：训练模式，1：测试模式
    test_type = 1
    # 评分标准
    eva_Type = 1

    startDate = time.strftime("%Y-%m-%d %H:%M:%S")
    endDate = time.strftime("%Y-%m-%d %H:%M:%S")
    for tester_id in testers_id_F:
        print(tester_id)
        for item_id in items_id:
            uuid = time.time()
            # 15米x4往返跑
            if (item_id == 106):
                insert_parm1 = {
                    "testType": test_type,
                    "score": scores_106,
                    "itemId": item_id,
                    "testUnicode": "",
                    "testerId": tester_id,
                    "keyNum": "1",
                    "evaType": eva_Type,
                    "uuid": uuid,
                    "faceUnicode": "",
                    "startDate": startDate,
                    "endDate": endDate,
                    "deviceUnicode": ""
                }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
                print(res_reg.json())
            # 肺活量
            if (item_id == 24):
                insert_parm1 = {
                    "testType": test_type,
                    "score": scores_24,
                    "itemId": item_id,
                    "testUnicode": "",
                    "testerId": tester_id,
                    "keyNum": "1",
                    "evaType": eva_Type,
                    "uuid": uuid,
                    "faceUnicode": "",
                    "startDate": startDate,
                    "endDate": endDate,
                    "deviceUnicode": ""
                }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
                print(res_reg.json())
            # 身高
            if (item_id == 22):
                insert_parm1 = {
                    "testType": test_type,
                    "score": scores_22,
                    "itemId": item_id,
                    "testUnicode": "",
                    "testerId": tester_id,
                    "keyNum": "1",
                    "evaType": eva_Type,
                    "uuid": uuid,
                    "faceUnicode": "",
                    "startDate": startDate,
                    "endDate": endDate,
                    "deviceUnicode": ""
                }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
                print(res_reg.json())
                # 体重
            if (item_id == 85):
                insert_parm1 = {
                    "testType": test_type,
                    "score": scores_85,
                    "itemId": item_id,
                    "testUnicode": "",
                    "testerId": tester_id,
                    "keyNum": "1",
                    "evaType": eva_Type,
                    "uuid": uuid,
                    "faceUnicode": "",
                    "startDate": startDate,
                    "endDate": endDate,
                    "deviceUnicode": ""
                }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
                print(res_reg.json())
            # 50米
            if(item_id==3):
                print(item_id)
                insert_parm1 = {
                    "testType": test_type,
                    "score": scores_3,
                    "itemId": item_id,
                    "testUnicode": "",
                    "testerId": tester_id,
                    "keyNum": "1",
                    "evaType": eva_Type,
                    "uuid": uuid,
                    "faceUnicode": "",
                    "startDate": startDate,
                    "endDate": endDate,
                    "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb"
                }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
                print(res_reg.json())

            #1000米
            if(item_id == 14):
                insert_parm1 = {
                    "testType": test_type,
                    "score": scores_14,
                    "itemId": item_id,
                    "testUnicode": "",
                    "testerId": tester_id,
                    "keyNum": "1",
                    "evaType": eva_Type,
                    "uuid": uuid,
                    "faceUnicode": "",
                    "startDate": startDate,
                    "endDate": endDate,
                    "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb"
                }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
                print(res_reg.json())
            #800米
            if(item_id==15):
                insert_parm1 = {
                    "testType": test_type,
                    "score": scores_15,
                    "itemId": item_id,
                    "testUnicode": "",
                    "testerId": tester_id,
                    "keyNum": "1",
                    "evaType": eva_Type,
                    "uuid": uuid,
                    "faceUnicode": "",
                    "startDate": startDate,
                    "endDate": endDate,
                    "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb"
                }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
                print(res_reg.json())
            # 坐位体前屈
            if (item_id == 5):
                insert_parm1 = {
                    "testType": test_type,
                    "score": scores_5,
                    "itemId": item_id,
                    "testUnicode": "",
                    "testerId": tester_id,
                    "keyNum": "1",
                    "evaType": eva_Type,
                    "uuid": uuid,
                    "faceUnicode": "",
                    "startDate": startDate,
                    "endDate": endDate,
                    "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb"
                }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
                print(res_reg.json())
            #立定跳远
            if(item_id == 9):
                insert_parm1 = {
                    "testType": test_type,
                    "score": scores_9,
                    "itemId": item_id,
                    "testUnicode": "",
                    "testerId": tester_id,
                    "keyNum": "1",
                    "evaType": eva_Type,
                    "uuid": uuid,
                    "faceUnicode": "",
                    "startDate": startDate,
                    "endDate": endDate,
                    "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb"
                }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
                print(res_reg.json())
            # 引体向上
            if (item_id == 11):
                    insert_parm1 = {
                        "testType": test_type,
                        "score": scores_11,
                        "itemId": item_id,
                        "testUnicode": "",
                        "testerId": tester_id,
                        "keyNum": "1",
                        "evaType": eva_Type,
                        "uuid": uuid,
                        "faceUnicode": "",
                        "startDate": startDate,
                        "endDate": endDate,
                        "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb"
                    }
                    res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post',headers=header)
                    print(res_reg.json())
            # 仰卧起坐
            if (item_id == 12):
                insert_parm1 = {
                            "testType": test_type,
                            "score": scores_12,
                            "itemId": item_id,
                            "testUnicode": "",
                            "testerId": tester_id,
                            "keyNum": "1",
                            "evaType": eva_Type,
                            "uuid": uuid,
                            "faceUnicode": "",
                            "startDate": startDate,
                            "endDate": endDate,
                            "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb"
                        }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post',headers=header)
                print(res_reg.json())
            # 实心球
            if (item_id == 16):
                insert_parm1 = {
                        "testType": test_type,
                        "score": scores_16,
                        "itemId": item_id,
                        "testUnicode": "",
                        "testerId": tester_id,
                        "keyNum": "1",
                        "evaType": eva_Type,
                        "uuid": uuid,
                        "faceUnicode": "",
                        "startDate": startDate,
                        "endDate": endDate,
                        "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb"
                    }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
                print(res_reg.json())
            # 双脚跳绳
            if (item_id == 17):
                insert_parm1 = {
                        "testType": test_type,
                        "score": scores_17,
                        "itemId": item_id,
                        "testUnicode": "",
                        "testerId": tester_id,
                        "keyNum": "1",
                        "evaType": eva_Type,
                        "uuid": uuid,
                        "faceUnicode": "",
                        "startDate": startDate,
                        "endDate": endDate,
                        "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb"
                    }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post',headers=header)
                print(res_reg.json())
            # 100米跑
            if (item_id == 92):
                insert_parm1 = {
                        "testType": test_type,
                        "score": scores_92,
                        "itemId": item_id,
                        "testUnicode": "",
                        "testerId": tester_id,
                        "keyNum": "1",
                        "evaType": eva_Type,
                        "uuid": uuid,
                        "faceUnicode": "",
                        "startDate": startDate,
                        "endDate": endDate,
                        "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb"
                    }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
                print(res_reg.json())

            # 200米自由泳
            if (item_id == 108):
                insert_parm1 = {
                        "testType":test_type,
                        "score": scores_108,
                        "itemId": item_id,
                        "testUnicode": "",
                        "testerId": tester_id,
                        "keyNum": "1",
                        "evaType": eva_Type,
                        "uuid": uuid,
                        "faceUnicode": "",
                        "startDate": startDate,
                        "endDate": endDate,
                        "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb"
                    }
                res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
                print(res_reg.json())
    # for i in  range(1,2):
    #     res_reg = HttpRequest(insert_url, param=json.dumps(insert_parm1)).http_request('post', headers=header)
    #     print(res_reg.json())

