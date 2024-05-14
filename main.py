from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# GET method is default
@app.route('/helloWorld', methods = ['GET'])
def helloWorld():
    return "Hello world!"

# Blah Blah gotta make a commit

# An endpoint that expects parameters
@app.route('/helloWorldParameters', methods = ['GET'])
def hello():
    name = request.args.get('name')

    if name is None or name == "":
        text = 'Hello world!'

    else:
        text = 'Hello ' + name + '!'

    return text

if __name__ == '__main__':
    app.run(debug=True, port=9670)

# A comment to test the pull_request workflow
