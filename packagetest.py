from db import *
import datetime
import time
creds=["USER","text1"]
u=posts()
r=u.post(creds)
print(r)
