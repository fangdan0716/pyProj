from comm.get_uuid import get_uuid
from comm.base_interface import BaseInterface
import time
import hashlib
t = int(time.time())*1000
t = str(t)
print(t)
signaturehash = "GET&/isport-data/sync-sport-result&"+t+"&w6WzFqYo23WBDt1P&asHUhKHdD21&"
# signature=hashlib.sha256(signaturehash.encode('utf-8')).hexdigest()
sha256 = hashlib.sha256()
sha256.update(signaturehash.encode('utf-8'))
signature = sha256.hexdigest()
print(signature)
parm = {"type": 1,"startTimestamp": int(time.time())*1000,"endTimestamp": int(time.time())*1000}
header= {"Content-Type": "application/x-www-form-urlencoded","signature": signature,"timestamp": t,"client-key": "rongmengappkey","nonce": "w6WzFqYo23WBDt1P","api-version": "v1.0.0"}

login_res = BaseInterface().baseInterface("/isport-data/sync-sport-result",parm,header,"GET")
print(header)
print(parm)
print(login_res.json())
