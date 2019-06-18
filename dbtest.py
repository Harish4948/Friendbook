from mongoengine import connect
import pymongo
from mongoengine import *
import datetime
conn = pymongo.MongoClient("mongodb+srv://admin:d3ku123@mydb-lurns.mongodb.net/test?retryWrites=true&w=majority")
database=conn['mydb']
# collection=database['users']

# INSERT
# u=input("USERNAME: ")
# p=input("\npassword: ")
# data={"username":u,"password":p}
# collection.insert_one(data)

# FIND
# r=collection.find_one({'username':"d3ku1"})
# if(r==None):
#     print("Not registered")
#print(r["password"])


# UPDATE
# data={"NAme":"HARISH"}
# r=collection.update_one({'NAme':'Hari'},{"$set":data})
# print(r)

# DELETE
# data={"Name":"HARISH"}
# r=collection.delete_one(data)
# print(r)


#w=10
# with open("no_of_posts.txt","r") as p:
#     s=int(p.read())
#     print(s)
#     w=s+1
# with open("no_of_posts.txt","w") as p:
#     p.write(str(w))
# w=0
# f=open("no_of_posts.txt","r")
# no_of_posts=int(f.readline())
# w=no_of_posts+1
# print(no_of_posts)
# f.close()
# print(w)
# l=open("no_of_posts.txt","w")
# l.write(str(w))
# l.close()



collection=database['posts']
db_posts=list(collection.find())
print(type(db_posts))
print(db_posts)
for i in db_posts:
    print(type(i))