"""
to maintain the readability and arrange the project in a given structure,
i am using Blueprint with the help of blueprint it is not necessary to write
all route function in the main file, so it overcomes by creating blueprint where each file will serve as
route to some url
"""
import json
from flask import jsonify
from flask_cors import CORS,cross_origin
from flask import Blueprint,request
"""
the reason i am using login_page is because it was throwing error when i used loginpage
but when added an underscore in between it worked

And this was the error AttributeError: 'function' object has no attribute 'name'
solved in later release
"""
login_page = Blueprint('serving this as loginpage', __name__, template_folder='templates')




@login_page.route('/api/loginverify',methods=['POST'])
def verify():
        pass