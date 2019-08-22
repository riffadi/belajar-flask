from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# dinamic url with string
@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def show_login():
	if request.method == 'POST':
		return 'Email kamu adalah ' + request.form['email']

	return render_template('login.html')


if __name__ == '__main__':
   app.run(debug=True)
