# coding: utf8
import os
from flask import Flask
from flask import request
from werkzeug import secure_filename
from view.simple_page import simple_page

app = Flask(__name__)
    
app.register_blueprint(simple_page)
app.register_blueprint(simple_page, url_prefix='/pages')
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))

    

if __name__=='__main__':
  app.run(debug=True)