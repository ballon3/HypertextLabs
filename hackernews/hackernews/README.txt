Hypertext Labs 
Date: 12/29/2018
Author:Ryan Brown 

This is a test implementation to merge three major stacks I have been working on,
consisting of Graphql Django Backend, with JupyterLab development integration and Podio API generation for
the graphql schema and django model infrastructure.

Notes on workspace setup...

https://gist.github.com/akimriparian/cc40effdd14c6eb148917e3bc2b31123

** Instructions**

to get jupyter lab set up in your django api environment https://github.com/jupyterlab/jupyterlab

in your pipenv shell run:

pip install django-extensions
pip install ipython
pip install jupyter
In you django-api/conf/settings.py add to the INSTALLED_APPS list

'django_extensions'
Back in your pipenv shell

# do this once to get the django kernel setup
./django-api/manage.py shell_plus --notebook
# then exit out of the running process
pip install jupyterlab
jupyter serverextension enable --py jupyterlab --sys-prefix

# this is for google drive support
jupyter labextension install @jupyterlab/google-drive
To run jupyter lab:

export DJANGO_SETTINGS_MODULE=conf.settings
jupyter lab


  
    """Podio COntacts Model."""
'''
TODO: 
Label	Type	External ID	Field ID	Sample JSON value
-	calculation	field-2	174703882	
-First Name	text	name	171818192	
-Last Name	text	last-name	174494763	
-Photo	image	photo	171818193	
-- Type	category	type	171818194	
Company(s)	tag	organization	171818196	
Job Title	text	job-title	171818195	
Phone	phone	phone-number	171818197	
-Email	email	email-address	171818198	
Action :	category	field	171818202	
Follow Up	category	follow-up	171818203	
-- Call History	calculation	call-history	173296379	
-- SMS History	calculation	sms-history	173296380	
-Address	location	address	171818199	
-DOB	date	dob	177430982	
-Website	embed	website	171818200	
-Notes	text	notes	171818201	
--Last Date Contacted	date	last-date-contacted	171818204

Categorical fields --

FOLLOW_UP 
ACTION 
TYPE 

'''
