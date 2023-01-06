from itertools import count
from flask import Flask,   render_template, redirect, session
app = Flask(__name__)    
app.secret_key = "secwet kwey"

@app.route('/')          
def index():
    if 'count' not in session:
        session ['count']=0
    session ['count']+=1    
    return render_template ("index.html", count= session['count'])

@app.route('/addtwo')          
def addtwo():
    session['count']+=1
    return redirect('/')

@app.route('/reset')          
def reset():
    session['count']=0
    return redirect('/')

@app.route('/destroy')          
def destroy_session():
    session.destory()
    return redirect('/')








if __name__=="__main__":      
    app.run(debug=True)    