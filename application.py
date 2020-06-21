#root level imports
#----------------------------------------------------
import os

# from flask_socketio import *
#importing scoket io
from flask_cors import CORS,cross_origin
from flask import Flask,render_template,request,make_response,redirect

from login import login_page #I have imported the blueprint registered in login.py file

from redirect_url import redirect_url

from static_content import static_content

#---------------------------------------------------------

application = Flask(__name__, instance_relative_config=True)
application.config.from_mapping(
        SECRET_KEY='dev',
        
    )


#application.config['CORS_HEADERS'] = 'Content-Type'


#----------------------------------------------------
# Registration of all blueprints goes here
application.register_blueprint(login_page)
application.register_blueprint(redirect_url)

application.register_blueprint(static_content)



#<----------------------------------------------------

CORS(application,resources={r"/*": {"origins": "*"}},supports_credentials=True);
# socketio = SocketIO(application)

from flask import abort,Response



# @cross_origin()
@application.before_request
def beforeeach():
    # print(request.environ)
    

    """
    print(request.headers,request.path)

    """
    pass





@application.after_request
def add_header(r):
    # print("""after""")
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,

    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r



if '__main__'==__name__:
    # create and configure the app

    """
    the main object is application as it is registered with flask
    application = Flask(__name__, instance_relative_config=True)

    """
    
    """
    Now registering that blueprint with main object application
    We have to do this every time when we register a new blueprint
    """
    
    #adding middle ware to the application so that socket io can work as a context between flask
   
   
   
    # for socket server
    # socketio.run(application,debug=True,host='0.0.0.0');



    # for web server
    application.run(host='0.0.0.0',port=5002,threaded=True)


