



from flask import Flask, render_template
app = Flask(__name__)



@app.route('/play')
def a_list():
    return render_template('index.html', times = 3, color = 'aqua') 


@app.route('/play/<int:num>')
def b_list(num):
    return render_template('index.html', times = num, color = 'aqua')

@app.route('/play/<int:num>/<string:color>')
def c_list(num, color):
    return render_template('index.html', times = num, color = color ) 




if __name__ == "__main__":   
    app.run(debug=True)    
