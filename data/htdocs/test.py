#!C:\Users\1371851\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: cp1251 -*-
print ("Content-type: text/html\n\n")
print
print ("<html><head>")
print ("")
print ("</head><body>")
print ("Hello.")

import cgi  
import json
import datetime
import vk_api 

print("test2")

form = cgi.FieldStorage() 
f = open("C:/login.txt", "r")
vk_session = vk_api.VkApi(f.readline(), f.readline())
vk_session.auth()
vk = vk_session.get_api()

name = form.getvalue("name")
surName = form.getvalue("surName")
bdate = form.getvalue("bdate")
if form.getvalue("bdate") != None:
    byear = bdate[0:4]
    bmonth = bdate[5:7]
    bday = bdate[8:10]
else:
    bdate = None
    bday = None
    bmonth = None
    byear = None
sex = form.getvalue("user_sex")
country = form.getvalue("country")
if form.getvalue("city") !=None and country != None :
    city = vk.database.getCities(country_id = country, q= form.getvalue("city"))["items"][0]["id"]
else:
    city = None

searchResults=vk.users.search(q = name + ' ' + surName,  birth_day = bday, birth_month = bmonth,  birth_year = byear, sex = sex,  country = country, city = city, count = 100, fields='bdate, city, photo_50, screen_name')
#,  age_from = int(form.getvalue("")), age_to = int(form.getvalue(""))
#,  company = form.getvalue("")

#print(searchResults)
#print(searchResults["items"][0]["id"])
#print(searchResults["items"][0]["first_name"] + " " + searchResults["items"][0]["last_name"])
#print(searchResults["items"][0]["photo_50"])
#if "city" in searchResults["items"][0]:
#    print(searchResults["items"][0]["city"]["title"])
#print(searchResults["items"][0]["bdate"])


print(searchResults)
print("test3")
returnResults = list()

for i in range(int(searchResults['count'])):
    g = []
    id = searchResults['items'][i]['id']
    name = searchResults['items'][i]['first_name']
    surname = searchResults['items'][i]['last_name']
    bdate = searchResults['items'][i]['bdate']
    href = 'vk.com/' + searchResults['items'][i]['screen_name']
    photo = searchResults['items'][i]['photo_50']
    city = searchResults['items'][i]['city']['title']
    g = [id, name, surname, bdate, href, photo, city]
    returnResults.append(g)
# print(returnResults)
 
print("test4")
print ("</body></html>")




# for i in range(int(searchResults["count"])):
#     id = searchResults["items"][i]["id"]
#     name = searchResults["items"][i]["first_name"] + " " + searchResults["items"][i]["last_name"]
#     photo = searchResults["items"][i]["photo_50"]
#     if "city" in searchResults["items"][i]:
#         city = searchResults["items"][i]["city"]["title"]
#     else:
#         city = ""
#     if "bdate" in searchResults["items"][i]:
#         bday = searchResults["items"][i]["bdate"]
#     else:
#         bday = ""
#     print(id + "\n" + photo + "\n" + name + "\n" + city + "\n" + bday + "\n")