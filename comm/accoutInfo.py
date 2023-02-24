import time

from comm.get_uuid import get_uuid
from comm.base_interface import BaseInterface

header = {"Content-Type": "application/json"}
parm = {
    "mobile" : "18302123929",  #// 手机号码
    "function" : "login"       #// 短信功能:login ｜ forgotPassword
    }
sms_res = BaseInterface().baseInterface("/sms/getValidCode",parm,header,"post")

parm ={
    "type" : "mobile",          #// 类型：mobile | account
    "mobile" : "18302123929",   #// 手机号码
    "code" : "278566"           #// 验证码，6 位数
}
login_res = BaseInterface().baseInterface("/admin/login",parm,header,"post")

login_res_dict = dict(login_res.json())
print(login_res_dict)
header = {"Content-Type": "application/json","x-auth-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI5MCIsImNyZWF0ZWQiOjE2NzEwOTgwNjcwNDAsImV4cCI6MTY3MTE4NDQ2N30.41SW1Pn0icQVk8riWx19EIIS4nL6NW04YceCbtZTbtT7urH2vQQHtm-hcvkTN26ol-72ElQrRvWpTlofIglklg"}

parm = {
        }
accout_get_reg =  BaseInterface().baseInterface('/school/device/account/list?pageNo=1&pageSize=10', parm,header ,"get")
print(accout_get_reg.json())