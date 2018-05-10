#HubspotPyTC

##Scripts:

	- getContacts.py - gets all contacts, then for each gets properties specified and writes json file
 	
	- parseJson.py - example parsing for json records

##How to run

	- Create project directory:
		'''mkdir HubspotPy'''

	- Create virtual environment:
		'''virtualenv --python python3 venv'''

	- Activate virtual environment:
		'''source venv/bin/activate''

	- Install requirements:
		'''pip install -r requirements.txt'''

	- Run getContacts.py:
		'''python3 getContacts.py'''

	- Run parseJson.py:
		'''python3 parseJson.py'''
 
