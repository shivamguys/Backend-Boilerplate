<img src="https://yesteacher.app/img/yesteacher.png" width="50%"/>

>  # BoilerPlate From YesTeacher.App

##### Following dependencies are mentioned in the [requirements.txt](requirements.txt) file
**pip3** should be installed to install all the dependencies

`sudo apt install python3-pip`

`pip3 install -r requirements.txt`

`python3 application.py` will create a server on port 5002


With Deployment Configuration Elastic BeanStalk Production Ready Check 
[.ebextensions](.ebextensions) Folder


For Pushing updates to Elastic Beanstalk Check [deployment.py](deployment.py) 


# Linking Multiple Repo

Define a git remote which will point to multiple git remotes.

Say, we call it **multiple**: `git remote add multiple REMOTE-URL-1`.

Register 1st push URL: `git remote set-url --add --push all REMOTE-URL-1`.
Register 2nd push URL: `git remote set-url --add --push all REMOTE-URL-2`.

Push a branch to all the remotes with `git push multiple origin`
