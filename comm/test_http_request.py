import unittest
from comm.http_request1 import HttpRequest
from comm.do_excel_new import DoExcel
from ddt import ddt,data
from comm.read_conf import ReadConfig
from comm.my_log import MyLog
from conf import project_path


test_data=DoExcel(project_path.test_data_path,"Sheet1").read_excel()

logger=MyLog()
COOKIE=None  #全局变量
IP = ReadConfig().read_config(project_path.http_conf_path, "HTTP", 'ip')
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        self.write=DoExcel(project_path.test_data_path, "Sheet1")
        # print("开始执行测试用例!!!")
        logger.info("开始执行测试用例!!!")
        self.header = {"client-key": "mini-yunketang-dev-b", "api-version": "6", "Content-Type": "application/json"}

    @data(*test_data)
    def test_http_request(self,a):
        # print("测试数据是",a)
        # print("目前正在执行第%s条用例"%a[0])
        logger.info("测试数据是:{0}".format(a))
        logger.info("目前正在执行第%s条用例"%a[0])
        #global COOKIE
        res=HttpRequest(IP + a[4],(a[5])).http_request(a[3],headers=self.header)
        #参数


        from comm.do_mysql import DbInfo
        config = eval(ReadConfig().read_config(project_path.datebae_conf_path, "DATABASE", 'config'))
        t = DbInfo(config)
        sql = 'select * from member where MobilePhone ="%s"; '%mobilePhone

        res = t.get_data(sql, 1)
        print(res)
        expect = eval(a[6])
        try:
            self.assertEqual(expect['code'], res.json()['code'])
            result = 'pass'

        except AssertionError as e:
            print("报错信息是%s" %e)
            result = 'fail'

            raise e
            # 写入数据
        finally:
            self.write.write_excel(a[0] + 1, str(res.json()), result)



    def  tearDown(self):
        # print("结束执行测试用例!!!")
        logger.info("结束执行测试用例!!!")



