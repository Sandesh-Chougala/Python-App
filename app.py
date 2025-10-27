from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_admin():
    name = request.form['name']
    pin = int(request.form['pin'])

    admin=['sandesh','Sandesh','SANDESH','Sandesh Chougala']

    if name in admin and pin == 1234:
        message = "Hello Sandesh, You're admin"
    else:
        message = "You're not admin, access denied."
    
    return render_template('index.html', result=message)

if __name__ == '__main__':
    app.run(debug=True)
