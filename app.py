from flask import Flask, render_template,request, redirect
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
        if len(data)>0:
            # Access the last dictionary in the 'data' list
            last_dict = data[-1]

            # Extract and print the value associated with the key 'id'
            last_id = last_dict['id']
        else:
            last_id = 0
        new_model = {
            'id': last_id+1,
            'model_name': title
        }
        data.append(new_model)
    return render_template('index.html',data = data)

@app.route('/remove/<int:model_id>')
def remove(model_id):
    for key in data:
        if key['id'] == model_id:
            data.remove(key)
    return redirect('/')

@app.route('/update/<int:model_id>')
def update(model_id):
    for model in data:
        if model['id']== model_id:
            return render_template('update.html', model = model)
    return redirect('/')

@app.route("/update_model",methods = ['POST'])
def update_model():
    name = request.form['model_name']
    id = request.form['id']
    for model in data:
        if model['id'] == int(id):
            model["model_name"] = name
            return redirect('/')
    return redirect('/')

if __name__ == "__main__":
    app.run()