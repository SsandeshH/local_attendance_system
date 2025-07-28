from flask import Flask, render_template,request,session
from data_handle import append_user_details
from data_export import export_data
from qr_generator import generate_qr_code
from datetime import datetime
app = Flask(__name__)
# app.secret_key = '787898'
filename = ""

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit',methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        global filename
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        semester = request.form.get('semester')
        if name and email and phone and semester:
            data = append_user_details(name, email, phone, semester)
            export_data(data,filename)
            return f"Thank you, {name}! Your attendance has been recorded."
        else:
            return "Please fill out all fields.", 400
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    global filename
    app_url = request.form.get('appUrl')
    filename = request.form.get('filename')
    if app_url:
        print(f"Generating QR code for URL: {app_url}")
        qr_code_img = generate_qr_code(app_url)
        return render_template('admin.html', 
                         qr_code_img=qr_code_img,
                         current_prefix=filename,
                         date=datetime.now().strftime("%d-%m-%Y"),
                         current_url=app_url)    
    else:
        return "Please provide a valid application URL.", 400



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)