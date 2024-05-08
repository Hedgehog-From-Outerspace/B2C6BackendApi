import json
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

# GET method is default
@app.route('/helloWorld', methods = ['GET'])
def helloWorld():
    return "Hello world!"

@app.route('/test')
def test():
    return "Test succesfull"

# An endpoint that expects parameters
@app.route('/helloWorldParameters', methods = ['GET'])
def hello():
    name = request.args.get('name')

    if name is None:
        text = 'Hello world!'

    else:
        text = 'Hello ' + name + '!'

    return text

if __name__ == '__main__':
    app.run(debug=True, port=9670)

# Theres 404 error handling, although this would probably be better
# to be handled in the front end
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404