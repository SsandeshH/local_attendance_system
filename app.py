from flask import Flask, render_template,request
from data_handle import append_user_details
from data_export import export_data
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit',methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        semester = request.form.get('semester')
        if name and email and phone and semester:
            data = append_user_details(name, email, phone, semester)
            export_data(data)
            return f"Thank you, {name}! Your attendance has been recorded."
        else:
            return "Please fill out all fields.", 400
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)