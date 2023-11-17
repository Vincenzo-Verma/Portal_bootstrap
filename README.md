# PortalVerson_2 with bootstrap

This is an alternate version of the Scholarship Redressal Prtal

# Project Setup
## Depeldencies and programs Required are 
- Django
- Bootstrap v5
- pip
- pipenv
- MySQL
    

    ## Steps Required

    1. clone the repo
        `git clone https://github.com/the-chaos-0/Portal_bootstrap.git`
    
    2. Create a virtual environment 
        `pipenv shell`
    
    3. Installing required dependencies
        `
        pipenv install django
        pipenv install mysqlclient
        pipenv install django-bootstrap5
        `
        ## Mysql Setup

        1. Install mysql community server
        2. Setup the server with password "MyPAssword"
            or
            Edit settings.py file to setup your password of mysql 
        3. Create a database named Students
    
    4. Run Migrations
        `python manage.py migrate`
    
    5. Run server
        `python manage.py runserver {port number}`



