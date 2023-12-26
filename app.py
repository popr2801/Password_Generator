from flask import Flask, render_template,request
import string, random

app = Flask(__name__)

def generate_password(length,mode):
    if(mode=="letters"):
        characters = string.ascii_letters
    elif(mode=="digits"):
        characters = string.digits
    else:
        characters = string.ascii_letters + string.digits
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password



@app.route('/',methods=['GET','POST'])
def index():
    radio = None
    password=""
    message=""
    if request.method == 'POST':
        radio = request.form.get("option")
        length = int(request.form.get("length"))
        password = generate_password(length,radio)
        message="Here's your new password:"
    return render_template('index2.html',message=message,password=password)

if __name__ == "__main__":
    app.run(debug=True)
