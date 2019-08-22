from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Halo BosQuu!!'

# static url 
@app.route('/setting')
def show_setting():
    return 'Halo kamu di halaman setting!!'

# dinamic url with string
@app.route('/profile/<username>')
def show_profile(username):
    return 'Halo kamu di halaman profile %s' % username

# dinamic url with integer
@app.route('/blog/<int:blog_id>')
def show_blog(blog_id):
    return 'Halo kamu di halaman blog nomer %d' %blog_id

if __name__ == '__main__':
   app.run(debug=True)
