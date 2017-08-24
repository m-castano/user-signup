from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

def empty_field(field):
    if field=="":
        return False
    else:
        return True

def entry_chars(entry):
    i=len(entry)
    if i < 3 or i > 20:
        return False
    else:
        return True

def entry_space(entry):
    for i in entry:
        if i == " ":
            return True
        i+=i

@app.route("/", methods=["POST"])
def print_form_values():
        
    username = request.form["username"]
    username_error = ""
    password = request.form ["password"]
    password_error=""
    verify_password = request.form["verify_password"]
    verify_password_error=""
    email_address = request.form["email_address"]
    email_address_error=""
    
    if not empty_field(username):
        username_error="No blanks."
    else:
        if not entry_chars(username):
            username=username
            username_error="Entry must be from 3 to 20 characters."
        else:
            if entry_space(username)==True:
                username=username
                username_error="No spaces."
        
    if not empty_field(password):
        password=""
        password_error="No blanks."
    else:
        if not entry_chars(password):
            password=""
            password_error="Entry must be from 3 to 20 characters."
        else:
            if entry_space(password) == True:
                password=""
                password_error="No spaces."

    if not empty_field(verify_password):
        verify_password_error="No blanks."

    if verify_password != password:
        verify_password=""
        verify_password_error="Password does not match."

    if email_address=="":
        email_address=email_address
    else:
        i=len(email_address)
        if i < 3 or i > 20:
            email_address=email_address
            email_address_error="Email must have from 3 to 20 characters"
        else:
            if entry_space(email_address)==True:
                email_address=email_address
                email_address_error="No blanks."
            else:
                if "@" not in email_address or "." not in email_address:
                    email_address=email_address
                    email_address_error="Email must have an '@' and a '.'."
                else:
                    if email_address.count("@") > 1 or email_address.count(".") > 1:
                        email_address=email_address
                        email_address_error="Email must have only one '@' and only one '.'."
                    else:
                        email_address=email_address
                        email_address_error=""
    
    if not username_error and not password_error and not email_address_error:
        return render_template("welcome.html", username=username)
    else:
        return render_template("index.html", username=username, username_error=username_error,
        password=password, password_error=password_error, verify_password=verify_password,
        verify_password_error=verify_password_error, email_address=email_address,
        email_address_error=email_address_error)




                
                
                
   

app.run()
