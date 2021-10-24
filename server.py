from re import S
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html') 

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name) 

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         name = data['name']
#         email = data['email']
#         subject = data['subject']
#         category = data['category']
#         message = data['message']
#         file = database.write(f'\n{name}, {email}, {subject}, {category}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline=' ') as database2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        category = data['category']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, category, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')    
        except:
            return 'This did not save to the database'
    else:
        return 'something went wrong, try again!'

# @app.route('/thankyou', methods=['POST', 'GET'])
# def thankyou():
#     return render_template('thankyou.html', request.form['name'])

if __name__ == "__main__":
    app.run()




