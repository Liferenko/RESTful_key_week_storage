# coding: utf8
import os
from flask import Flask
from view.simple_page import simple_page

app = Flask(__name__)
    
    
app.register_blueprint(simple_page)
app.register_blueprint(simple_page, url_prefix='/pages')
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
# getenv only for cloud9 environment

if __name__=='__main__':
  app.run(debug=True)
  