from flask import Flask, render_template,request
app = Flask(__name__)

data = [
    {
        'id' : 1,
        'model_name' : 'KNN',
    },
    {
        'id' : 2,
        'model_name' : 'RNN',
    },
    {
        'id' : 3,
        'model_name' : 'Random Forest',
    },
    {
        'id' : 4,
        'model_name' : 'LR',
    },
    {
        'id' : 5,
        'model_name' : 'Logistic R',
    },
]

@app.route('/home',methods = ['GET','POST'])
@app.route('/')
def home():
    if request.method == 'POST':
        title = request.form['model']
    return render_template('index.html',data = data)

if __name__ == "__main__":
    app.run()