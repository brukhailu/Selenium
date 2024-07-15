from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/')
def registration_form():
    return '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Agent Registration Form</title>
    </head>
    <body>
        <h1>Register Agent</h1>
        <form method="post" action="/register">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br><br>
            <label for="phone">Phone Number:</label>
            <input type="text" id="phone" name="phone" required><br><br>
            <label for="address">Address:</label>
            <input type="text" id="address" name="address" required><br><br>
            <input type="submit" id="submit"  value="Register">
        </form>
    </body>
    </html>
    '''


@app.route('/register', methods=['POST'])
def register_agent():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']

    # Process the form data as needed
    # For this example, we'll just return a confirmation message
    return f'''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registration Confirmation</title>
    </head>
    <body>
        <h1>Registration Confirmation</h1>
        <p>Name: {name}</p>
        <p>Email: {email}</p>
        <p>Phone Number: {phone}</p>
        <p>Address: {address}</p>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
    app.run(debug=True)
