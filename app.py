from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        return render_template('index.html', message="Attendance submitted successfully!")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0', port=5000)