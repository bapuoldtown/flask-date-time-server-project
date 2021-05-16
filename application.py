from flask import Flask
from datetime import date,datetime
application = Flask(__name__)

@application.route('/<string:name>')
def hello_world(name):
   return "<h1>Hello {}, The Time now is {} , and Today is {}  </h1>".format(name.title(),datetime.now().strftime("%H:%M"),date.today().strftime("%A %d %B %Y"))


@application.route('/greet/<string:name>')
def greet_HelloWorl(name):
    return "<h1>Hello, {} Time now is {} , and Today is {}  </h1>".format(name.title(),datetime.now().strftime("%H:%M"),date.today().strftime("%A %d %B %Y"))

if __name__ == '__main__':
   application.run(host='0.0.0.0',debug=False)