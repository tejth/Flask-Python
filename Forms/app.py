from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The person is passed , score and marks is </h1></body></html>"+str(score) #you can also return html file

@app.route('/fail/<int:score>')
def fail(score):
    return "The person score and marks is "+str(score)

@app.route('/results/<int:marks>')
def results(marks):
     result =""
     if marks<50:
         result='fail'
     else:
         result="success"
     return redirect(url_for(result,score=marks)) #displaying different pages
 

if __name__ == '__main__':
    app.run(debug=True)