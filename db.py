import pymongo
import datetime
from collections import ChainMap

conn = pymongo.MongoClient("mongodb+srv://admin:d3ku123@mydb-lurns.mongodb.net/test?retryWrites=true&w=majority")
database=conn['mydb']

class users:
    #def __init__(self):
    collection=database['users']

    def register(self,creds):
        #creds[]=[email,username,password]  
        data={"email":creds[0],"username":creds[1],"password":creds[2]}
        email={"email":creds[0]}
        user={"user":creds[1]}
        if(self.collection.find_one(email)==None):
            if(self.collection.find_one(user)==None):
                self.collection.insert_one(data)
                return True
            else:
                #User already registered
                return False
        else:
            # EMAIL ALREADY REGISTERED
            return False

    def login(self,creds):
        data={"username":creds[0],"password":creds[1]}
        user={"username":creds[0]}
        result_of_query=self.collection.find_one(user)
        try:
            pass_actual=result_of_query["password"]
            if(result_of_query!=None):
                if(pass_actual==creds[1]):
                    return True
                else:
                    return False

            else:
                return False
        except:
            return False
class db_posts:

    collection=database['posts']
    def insert_post(self,creds):
        updated_val=0
        prev_val=0
        f=open("no_of_posts.txt","r")
        prev_val=int(f.readline())
        updated_val=prev_val+1
        print(prev_val)
        f.close()
        print(updated_val)
        l=open("no_of_posts.txt","w")
        l.write(str(updated_val))
        l.close()
        data={"_id":updated_val,"username":creds[0],"text":creds[1]}
        self.collection.insert_one(data)
    def get_post(self):
        db_posts=list(self.collection.find())
    # ?db_posts=dict(self.collection.find())
        return db_posts
        





    




