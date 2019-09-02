from flask import Flask,render_template,url_for,redirect,request
import json
import requests

appl=Flask(__name__)
searches=[]
@appl.route("/")
def fun1():
    l=[]
    response = requests.get("https://uflixit.p.rapidapi.com/movies/wanted",
    headers={
    "X-RapidAPI-Host": "uflixit.p.rapidapi.com",
    "X-RapidAPI-Key": "***************************************"  # sign up for rapid api then subscribe uflixir api and use alloted key to fetch data from api
  }).json()
    for x in response['result']:
        response1 = requests.get(f"https://uflixit.p.rapidapi.com/movie/details/{x}",
        headers={
          "X-RapidAPI-Host": "uflixit.p.rapidapi.com",
          "X-RapidAPI-Key": "***************************************88"
        }).json()
        l.append(response1)
    f=open("details.txt","r")
    sd=json.load(f)
    f.close()
    f=open("top.txt","r")
    sds=json.load(f)
    f.close()    

    

   
    
    return render_template("prodigy.html",file2=l,file3=sd,file4=sds)

@appl.route("/query" ,methods=['POST','GET'])
def fun2():
    if request.method=='POST':
        movie_name=request.form['search']
        data = requests.get(f"https://uflixit.p.rapidapi.com/movies/search?query={movie_name}",headers={
    "X-RapidAPI-Host": "uflixit.p.rapidapi.com",
    "X-RapidAPI-Key": "*****************************************************888"
        })
        data=data.json()
        response = requests.get(f"https://uflixit.p.rapidapi.com/movie/details/{data['result']['imdb_id']}",
        headers={
          "X-RapidAPI-Host": "uflixit.p.rapidapi.com",
          "X-RapidAPI-Key": "*******************************************8"
        })
        
        data1=response.json()
        
        f=open("details.txt","r")
        sd=json.load(f)
        f.close()
        for x in sd:
          if x['result']['title']==data1['result']['title']:
            flag=1
          else:
            flag=0
        if flag==0:
          sd.append(data1)
          f=open("details.txt","w")
          json.dump(sd,f)
          f.close()
    return render_template("annoying.html",file=data1)
         
@appl.route("/query/<var>" ,methods=['POST','GET'])
def fun3(var):
    if request.method=='POST':
        movie_name=request.form['search']
        data = requests.get(f"https://uflixit.p.rapidapi.com/movies/search?query={movie_name}",headers={
    "X-RapidAPI-Host": "uflixit.p.rapidapi.com",
    "X-RapidAPI-Key": "******************************************"
        })
        data=data.json()
        response = requests.get(f"https://uflixit.p.rapidapi.com/movie/details/{data['result']['imdb_id']}",
        headers={
          "X-RapidAPI-Host": "uflixit.p.rapidapi.com",
          "X-RapidAPI-Key": "************************************************88"
        })
        
        data1=response.json()
        
        f=open("details.txt","r")
        sd=json.load(f)
        f.close()
        for x in sd:
          if x['result']['title']==data1['result']['title']:
            flag=1
          else:
            flag=0
        if flag==0:
          sd.append(data1)
          f=open("details.txt","w")
          json.dump(sd,f)
          f.close()
          return render_template("annoying.html",file)
       
    else:
       
    
        response = requests.get(f"https://uflixit.p.rapidapi.com/movie/details/{var}",
        headers={
          "X-RapidAPI-Host": "uflixit.p.rapidapi.com",
          "X-RapidAPI-Key": "**************************************************************8"
        })
        
        data1=response.json()
        return render_template("annoying.html",file=data1)


if __name__=='__main__':
    appl.run(port=80,debug=True)