from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hola mundo</h1>"

@app.route('/user/<username>')
def user(username):
    return render_template("template.html", username=username)
@app.route('/persona/')
def persona():
    return render_template("new.html", nombre="Jaime")
if __name__ == "__main__":
	app.run(debug=True)
