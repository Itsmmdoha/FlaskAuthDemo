from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# JSON file to store user data
USER_DATA_FILE = 'users.json'

# Helper function to load users from JSON file
def load_users():
  if os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, 'r') as file:
      return json.load(file)
  return []

# Helper function to save users to JSON file
def save_users(users):
  with open(USER_DATA_FILE, 'w') as file:
    json.dump(users, file)

@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')

    # Load existing users
    users = load_users()

    # Validate user credentials
    for user in users:
      if user['username'] == username and user['password'] == password:
        # Render user info in a template
        return render_template('user_info.html', user=user)

    return 'Invalid credentials', 401

  return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    # Get form data
    name = request.form.get('name')
    age = request.form.get('age')
    experience = request.form.get('experience')
    username = request.form.get('username')
    password = request.form.get('password')

    # Load existing users
    users = load_users()

    # Check if username already exists
    if any(user['username'] == username for user in users):
      return 'Username already exists', 400

    # Create a new user
    new_user = {
      'name': name,
      'age': age,
      'experience': experience,
      'username': username,
      'password': password
    }

    # Append new user to the users list and save
    users.append(new_user)
    save_users(users)

    return 'Signup successful!', 201

  return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
