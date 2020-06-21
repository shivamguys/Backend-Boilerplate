

from flask import Blueprint,request,send_file,make_response,redirect,Response,render_template
static_content=Blueprint('serving this as static content api', __name__, template_folder='templates')







@static_content.route('/',methods=['GET'])
def this_is_the_root():

    # return render_template("index.html")

    # return "<h1>Powered By YesTeacher.App</h1>"
    pass





  