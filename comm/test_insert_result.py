import json
import unittest
from comm.http_requestExcel import HttpRequest
from comm.do_excel_new3 import DoExcel
from ddt import ddt,data
from comm.read_conf import ReadConfig
from comm.my_log import MyLog
from conf import project_path

path = project_path.do_excel_new3_path
write = DoExcel(path, "Parm")
write.writeParmtoExcel(2)
test_data=DoExcel(path,"Parm").readParmfromExcel()
print(test_data)
logger=MyLog()
COOKIE=None  #全局变量
IP = ReadConfig().read_config(project_path.http_conf_path, "HTTP", 'ip')
header_login = {"Content-Type": "application/json"}
login_parm = {
            "username": "yunnan1",
            "deviceUnicode": "7b9654d9-1efc-3d25-9425-b544ea2d66cb",
            "password": "dabai521"
        }
logger.info("执行登录接口获取cookies")
login_reg = HttpRequest(IP+"/user/login", param=json.dumps(login_parm)).http_request('post', headers=header_login)
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        self.write=DoExcel(project_path.do_excel_new3_path, "Parm")
        logger.info("登录接口返回消息体"+str(login_reg.json()))
        logindict = dict(login_reg.json())
        logger.info("response转dict"+str(logindict))
        self.result_header = {"Authorization": logindict["data"]["authorization"], "Content-Type": "application/json"}
        logger.info("开始执行测试用例!!!")

    @data(*test_data)
    def test_http_request(self,a):
        logger.info("测试数据是:%s"%a[0])
        print(a[4])
        print(type(eval(a[5])))
        print(a[3])
        res=HttpRequest(IP + a[4],eval(a[5])).http_request(a[3],headers=self.result_header)
        logger.info("接口调用返回结果"+str(res.json()))
        logger.info("接口调用返回结果")
        self.write.writeResponsetoExcel(2,str(res.json()))


    def  tearDown(self):
        logger.info("结束执行result/insert")




