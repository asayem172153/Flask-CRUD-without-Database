from flask import Flask, render_template
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

@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()