from flask import Flask, request, jsonify
app = Flask(__name__)
messages = []

@app.route('/', methods=['GET'])
def home():
    return '''
        <form action="/submit" method="post">
            <input name="msg" />
            <input type="submit" />
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    msg = request.form['msg']
    messages.append(msg)
    return "<br>".join(messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
