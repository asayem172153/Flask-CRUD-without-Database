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
# Access the last dictionary in the 'data' list
last_dict = data[-1]

# Extract and print the value associated with the key 'id'
last_id = last_dict['id']
print(last_id)