"""接口基类"""
from comm import http_request1
from comm import read_conf
import json
from comm.get_uuid import get_uuid
import random
import time
class BaseInterface():

    def baseInterface(self,url,parm,header,mothod):
        self.url = read_conf.ReadConfig().read_config("../conf/http.conf","HTTP", 'ip') + url
        self.parm = parm
        self.headers = header
        self.mothod = mothod
        if self.mothod.upper() == "GET":
            res = http_request1.HttpRequest(self.url,param=json.dumps(self.parm)).http_request("get",headers=self.headers)
        if self.mothod.upper() == "POST":
            res = http_request1.HttpRequest(self.url,param=json.dumps(self.parm)).http_request("post",headers=self.headers)
        return res
