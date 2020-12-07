from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from .models import Destination
from django.db import connection
from datetime import datetime
# Create your views here.
def index(request):
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM tbl_users")

    myresult = mycursor.fetchall()
    #print("Total number of rows in Laptop is: ", mycursor.rowcount)
    # for users in myresult:
    #     print(users)
    args = {}
    args['result'] = myresult
    #bookdata = { 'success':'true', "details" : myresult }
    
    dest1= Destination()
    
    dest1.name='mumbai'
    dest1.desc='city never sleeps'
    dest1.img='destination_1.jpg'
    dest1.price='508'

    dest2= Destination()
    dest2.name='Hyderabad'
    dest2.desc='city never sleeps'
    dest2.img='destination_2.jpg'
    dest2.price='508'

    dests = [dest1,dest2]

    
    return render(request,'index.html',args)
    #return render(request,'index.html',{'dests':dests,'users':users})
    #return JsonResponse(bookdata)

def get_all_users(request):
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM tbl_users")

    myresult = mycursor.fetchall()
    #print("Total number of rows in Laptop is: ", mycursor.rowcount)
    # for users in myresult:
    #     print(users)
    args = {}
    args['result'] = myresult
    return render(request,'users.html',args)

def get_user(request):
    userid = request.GET['id']
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM tbl_users where id='"+userid+"'")

    myresult = mycursor.fetchone()
    data ={
        'userdata':myresult
    }
    return JsonResponse(data)

def submit_user(request):
    #d4    = today.strftime("%b-%d-%Y")
    now = datetime.now()
    name  = request.POST['name']
    email = request.POST['email']
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")

    mycursor = connection.cursor()
    sql = "INSERT INTO tbl_users (name, email,created_at,updated_at) VALUES (%s, %s, %s, %s)"
    val = (name, email,dt_string,dt_string)
    mycursor.execute(sql, val)
    lastid = mycursor.lastrowid
    data ={
        'lastid':lastid
    }
    #mycursor.commit()
    #print("1 record inserted, ID:", mycursor.lastrowid)
    return JsonResponse(data)

    
