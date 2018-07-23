from flask import Flask ,redirect, url_for, render_template , request

app = Flask("read")

@app.route("/")
def index():
	return "<form action=/action method=post ><input placeholder='enter message' type=text name=msg /><input type=submit value=send></form>"


@app.route("/action",methods=["GET","POST"])
def action():
	if request.method == 'POST':
		file = open("../readwrite/text.txt","a")
		file.write(request.form["msg"]+"<br>")
		file.close()
		return redirect(url_for('index'))
	return "failed to write"
	
app.run(host="0.0.0.0",port=5200,debug=True)
