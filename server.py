from flask import Flask,render_template,url_for,request,redirect
import csv
#We instantiate a class
app = Flask(__name__)
print(__name__)
#Variable Rules



#decorator
#root route
#with <> you can pass parameters directly
#example; username
#filters specifi for url

@app.route('/')
def index():
	return render_template('index.html')

#dynamically pass page name into server
@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)


def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]

		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	#mode='a' that means append mode
	with open('database.csv', newline='',mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		#csv.writer takes parameter where to write
		#different options
		#be separated by the comma
		csv_writer = csv.writer(database2,delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		#retrieve data as a dict
		data = request.form.to_dict()
		#use created function to store dict in txt
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'something went wrong try again'



