from flask import Flask, render_template, request, redirect, url_for
from flask_assets import Bundle, Environment
import os

app = Flask('__name__')
app.config['SECRET_KEY'] = os.urandom(20)

assets = Environment(app)
js = Bundle('js/jquery.countdown.js','js/particles.js','js/main.js', output='js/generate/minified.js', filters='jsmin')
css = Bundle('css/style.css','css/font-awesome/css/font-awesome.css', output='css/generate/minified.css', filters='cssmin')
assets.register("minified-js", js)
assets.register("minified-css", css)

@app.route('/')
def index():
	if(request.args.get('alert')!=None):
		return render_template('index.html',alert=request.args.get('alert'))
	else:
		return render_template('index.html',alert=None)

@app.route('/subscribe', methods=['POST'])
def subscribe():
	file = open("subscribers.txt","a")
	file.write(request.form['subscribe-email']+"\n")
	file.close()
	return redirect(url_for('index',alert="You have been subscribed. We'll keep you notified."))

@app.route('/subscribers')
def subscribers():
	file = open('subscribers.txt').readlines()
	output = ""
	for line in file:
		output += line + "<br />"
	return output

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8000,debug=True)