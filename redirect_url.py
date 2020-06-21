
from flask import Blueprint,request,make_response,redirect,Response
redirect_url=Blueprint('serving this as request redirect api', __name__, template_folder='templates')
"""
All reditects at one place
"""




@redirect_url.route('/redirect/path',methods=['GET'])
def redirectto():

    return redirect('/redirect/new/path')





