from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    # Fetch blog posts from the database in reverse chronological order
    posts = fetch_posts()  # Replace with your database integration logic
    return render_template('index.html', posts=posts)

# Login route
@app.route('/login')
def login():
    # Render the login page
    return render_template('login.html')

# Login form submission route
@app.route('/login', methods=['POST'])
def login_submit():
    # Process the login form submission
    username = request.form['username']
    password = request.form['password']
    # Validate the credentials and handle authentication

    # If the login is successful, redirect to the admin dashboard
    return redirect(url_for('admin_dashboard'))

# Admin dashboard route
@app.route('/admin/dashboard')
def admin_dashboard():
    # Render the admin dashboard page
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Sample data for logged-in user's posts
sample_posts = [
    {
        'id': 1,
        'title': 'First Post',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    },
    {
        'id': 2,
        'title': 'Second Post',
        'content': 'Nulla facilisi. Sed at nisi nec felis pharetra feugiat.',
    }
]

# Home route
@app.route('/')
def home():
    # Fetch blog posts from the database in reverse chronological order
    posts = fetch_posts()  # Replace with your database integration logic
    return render_template('index.html', posts=posts)

# Login route
@app.route('/login')
def login():
    # Render the login page
    return render_template('login.html')

# Login form submission route
@app.route('/login', methods=['POST'])
def login_submit():
    # Process the login form submission
    username = request.form['username']
    password = request.form['password']
    # Validate the credentials and handle authentication

    # If the login is successful, redirect to the admin dashboard
    return redirect(url_for('admin_dashboard'))

# Admin dashboard route
@app.route('/admin/dashboard')
def admin_dashboard():
    # Render the admin dashboard page with the user's posts
    return render_template('dashboard.html', posts=sample_posts)

# Edit post route
@app.route('/admin/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    # Handle editing a specific post identified by post_id
    if request.method == 'POST':
        # Update the post in the database with the submitted data
        updated_title = request.form['title']
        updated_content = request.form['content']
        # Update the post in the database using post_id and the submitted data

        # Redirect to the dashboard after updating
        return redirect(url_for('admin_dashboard'))

    # Retrieve the post from the database using post_id
    post = get_post(post_id)  # Replace with your database integration logic

    # Render the edit post page with the retrieved post
    return render_template('edit_post.html', post=post)

# Delete post route
@app.route('/admin/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    # Handle deleting a specific post identified by post_id
    # Delete the post from the database using post_id

    # Redirect to the dashboard after deleting
    return redirect(url_for('admin_dashboard'))

# Add post route
@app.route('/admin/add', methods=['GET', 'POST'])
def add_post():
    # Handle adding a new post
    if request.method == 'POST':
        # Get the submitted data
        new_title = request.form['title']
        new_content = request.form['content']
        # Create a new post in the database with the submitted data

        # Redirect to the dashboard after adding
        return redirect(url_for('admin_dashboard'))

    # Render the add post page
    return render_template('add_post.html')

if __name__ == '__main__':
    app.run()

