from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'contact': '1234567890',
        'name': 'Andrew',
        'done': False
    },
    {
        'id': 2,
        'contact': '0987654321',
        'name': 'Tom',
        'done': False
    }
]

@app.route('/add-data', methods = ['POST'])
#post - user can send some data

def addTask():
    if not request.json: 
        return jsonify({
            'status': 'error',
            'message': 'Please provide the data.'
        },400)
    
    task = {
        #automatically generating the id for the person.
        'id': tasks[-1]['id']+1,
        'contact': request.json['contact'],
        'name': request.json['name'],
        'done': False
    }

    tasks.append(task)

    return jsonify({
        'status': 'success',
        'message': 'Details have been added successfully.'
    },200)

@app.route('/get-data')

def getTask():
    return jsonify({
        'data': tasks
    })


if __name__ == '__main__':
    app.run(debug=True)
    #helps to reload the server if you make a change in the code