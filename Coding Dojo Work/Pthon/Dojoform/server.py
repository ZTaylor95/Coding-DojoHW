
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)    
app.secret_key="uwu"

@app.route('/')          
def index():
    return render_template ("index.html")

@app.route('/thanks')          
def thanks():
    return render_template ("results.html")


@app.route('/processform', methods=['POST'])          
def processform():
    
    
    print(request.form['name'])
    print(request.form['dojo_location'])
    print(request.form['fav_waifu'])
    print(request.form['bad_opinions'])

    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['fav_waifu'] = request.form['fav_waifu']
    session['bad_opinions'] = request.form['bad_opinions']
    return redirect("/thanks")

if __name__=="__main__":      
    app.run(debug=True)    