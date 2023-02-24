import random
import time
from conf import project_path
import requests
import json
from  comm import do_excel_new3
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
    # 体测：批量插入
    # 读取excel 和 把 parm 拼接插入excel 读excel的数据执行insert 接口
    login_header ={"Content-Type": "application/json"}
    login_url ='http://yuntiyu-test.dream-sports.cn/tice/user/login'
    login_parm ={
                "username": "yunnan1",
                "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb",
                "password": "dabai521"
            }
    #print(type(login_parm))
    login_reg = HttpRequest(login_url, param=json.dumps(login_parm)).http_request('post', headers=login_header)
    logindict =dict(login_reg.json())
    header = {"Authorization": logindict["data"]["authorization"],"Content-Type": "application/json"}
    insert_url = 'http://yuntiyu-test.dream-sports.cn/tice/result/insert'
    parmDataWrite = do_excel_new3.DoExcel(project_path.do_excel_new3_path,"Parm").writeParmtoExcel(2)
    parmDataRead = do_excel_new3.DoExcel(project_path.do_excel_new3_path,"Parm").readParmfromExcel()
#     req_body1={}
    for req_body in parmDataRead:
        res_reg = HttpRequest(insert_url, param=json.dumps(eval(req_body))).http_request('post', headers=header)
        print(res_reg.json())
        do_excel_new3.DoExcel(project_path.do_excel_new3_path, "Parm").writeResponsetoExcel(2, str(res_reg.json()))
