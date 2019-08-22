from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# dinamic url with string
@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html', username=username)

if __name__ == '__main__':
   app.run(debug=True)
