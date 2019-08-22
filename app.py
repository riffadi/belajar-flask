from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    search = request.args.get('search')
    return render_template('index.html', search=search)


# dinamic url with string
@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def show_login():
	if request.method == 'POST':
		resp = make_response('Email kamu adalah ' + request.form['email'])
		resp.set_cookie('email_user', request.form['email'])
		return resp

	return render_template('login.html')
@app.route('/getcookie')
def get_cookie():
	email = request.cookies.get('email_user')
	return 'Email yang tersimpan di cookie adalah ' + email
	

if __name__ == '__main__':
   app.run(debug=True)
