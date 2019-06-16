from db import users
import datetime
import time
creds=["USER","pass"]
u=users()
r=u.login(creds)
print(r)
