from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score,'res':res}
    return render_template('result.html',result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed , score and marks is "+str(score)

# ///////////////////////////////
@app.route('/results/<int:marks>')
def results(marks):
     result =""
     if marks<50:
         result='fail'
     else:
         result="success"
     return redirect(url_for(result,score=marks)) #displaying different pages
 
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['math'])
        english=float(request.form['english'])
        history=float(request.form['history'])
        total_score = (science+maths+english+history)/4
    res=""
    if total_score>=50:
        res="success"
    else:
        res="fail"
    return redirect(url_for(res,score=total_score))
        
    

if __name__ == '__main__':
    app.run(debug=True)