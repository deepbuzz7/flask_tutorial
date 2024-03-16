from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def index():
    return "dsjhfdjfdlk"

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route("/with_parms")
def with_parms():
    name=request.args.get('name')
    return f"{request.args.getlist('name')}"

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)


