from flask import Flask,render_template,request
import requests
import smtplib
my_email="------@gmail.com"
password=********


# https://www.npoint.io/docs/0fb369ee701f10b666ae

app = Flask(__name__)

@app.route("/")
def main_page():
    response=requests.get("https://api.npoint.io/0fb369ee701f10b666ae")
    data=response.json()
    return render_template("index.html",data=data)

@app.route("/<num>")
def single_blog(num):
    response=requests.get("https://api.npoint.io/0fb369ee701f10b666ae")
    data=response.json()
    newdata=data[int(num)-1]
    return render_template("post.html",datas=newdata)

@app.route("/login",methods=['GET','POST'])
def form():
    if request.method =='POST':
        name=request.form["contact_name"]
        email=request.form["contact_email"]
        message=request.form["contact_message"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="------@gmail.com",
                msg=f"Subject: Form message \n\n Name: {name} \n Email: {email} \n Message: \n {message}"
            )
            return f"Hey {name},Thanks for your message"
    return "This is a get Page"
if __name__=="__main__":
    app.run(debug=True)