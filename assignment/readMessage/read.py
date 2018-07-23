from flask import Flask ,redirect, url_for, render_template , request

app = Flask("read")


@app.route("/")
def index():
	file = open("../readwrite/text.txt","r")
	s=file.read()
	file.close()
	return "<h2>Messages added to file</h2> <p> "+s+"</p>"
	
app.run(host="0.0.0.0",port=5100,debug=True)
