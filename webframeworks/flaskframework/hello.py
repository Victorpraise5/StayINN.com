from flask import Flask
from markupsafe import escape

app = Flask(__name__)

#Use the route() decorator to bind a function to a URL.
@app.route("/")
def index():
  return "Index Page"

@app.route('/hello')
def hello():
  return "<p>Hello, World!</p>"

# You can make parts of the URL dynamic and attach multiple rules to a function.
# Dynamic URL with one route
#@app.route('/user/<username>')
# Dynamic URL with another route
#@app.route('/profile/<username>')
#def show_user_profile(username):
#    return f'Profile page of {username}'

# Dynamic URL with integers
#@app.route('/post/<int:post_id>')
#def show_post(post_id):
#    return f'Post ID: {post_id}'

# Multiple routes for a single function
#@app.route('/about')
#@app.route('/info')
#def about():
#    return 'This is the About/Info page.'

#variable rules: using escape
#any user-provided values rendered in the output must be escaped to protect from injection attacks
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'