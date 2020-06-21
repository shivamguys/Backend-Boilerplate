import os
"""
Configure your secure connection variable here, to be used with microservices

"""

host=os.environ.get('db_host')
port=os.environ.get('db_port')
username=os.environ.get('db_username')
password=os.environ.get('db_pa')
