import sqlite3
import bcrypt
from questionary import prompt
import questionary

# Connect to the SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()
loggedin = False

# Create a table for storing user data
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL,
              password TEXT NOT NULL)''')

# Register function
def register():
    # Get the username and password from the user
    username = questionary.text("Enter your username").ask()
    password = questionary.password("Enter your password").ask()

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert the user data into the database
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()

    # Print a success message
    print('Registration successful!')

# Login function
def login():
    # Get the username and password from the user
    username = questionary.text("Enter your username").ask()
    password = questionary.password("Enter your password").ask()

    # Get the user data from the database
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()

    # Check if the user exists and the password is correct
    if user is not None and bcrypt.checkpw(password.encode('utf-8'), user[2]):
        # Print a success message
        global loggedin
        loggedin = True
        return loggedin   

    # Print an error message if the login fails
    else:
        print('Invalid username or password')
        login()

# Main loop
def loginsys():
    # Get the user's choice
    loginchoices = [

        {
            'type': 'select',
            'message': "Please Sign-In before accessing the database",
            'name': 'login',
            "choices": ["Login", "Register", "Quit"]
        }
    ]

    choice = prompt(loginchoices)

    # Call the appropriate function based on the user's choice
    if choice["login"] == 'Register':
        register()
    elif choice["login"] == 'Login':
        login()
    elif choice["login"] == 'Quit':
        exit()
    else:
        print('Invalid choice')
