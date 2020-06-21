

from flask import Blueprint,request,send_file,make_response,redirect,Response,render_template
static_content=Blueprint('serving this as static content api', __name__, template_folder='templates')
"""
You can use this route as some static content used in function instead of html file
Frequent modification of dynamic server side content can be used here.
"""






@static_content.route('/',methods=['GET'])
def this_is_the_root():

    # return render_template("index.html")

    # return "<h1>Powered By YesTeacher.App</h1>"
    pass





  