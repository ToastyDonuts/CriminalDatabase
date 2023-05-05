import questionary
username = questionary.text("Enter your username").ask()
password = questionary.password("Enter your password").ask()


print(username + password)