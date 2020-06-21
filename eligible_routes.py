from flask import Blueprint,request
eligible_routes= Blueprint('serving this as to verify assign marks item for principal', __name__, template_folder='templates')




import dbconnection
import json


@eligible_routes.route('/verify/eligible',methods=['GET'])
def is_eligible():
    pass