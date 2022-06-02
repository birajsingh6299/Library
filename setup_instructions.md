# Library
eLibrary Project

**Software Applications Required:**
a. XAMPP Control Panel
b. Django Framework 3.0 or above.

**Steps to run the project**
1. Create a Folder eLibrary in your virtual environment (where Django framework is installed)
2. Download all the folders and files from the github repository Library and add it inside the newly created eLibrary Folder
3. Go to the eLibrary Folder in your cmd and give the following commands.
    a. pip install mysqlclient
    b. pip install djangorestframework 
    c. pip install djangorestframework-simplejwt

4. In the PHPMyAdmin Page create a new database with elibrary_db
5. Go to the eLibrary Folder in your cmd and give the following commands.
    a. python manage.py makemigrations
    b. python manage.py sqlmigrate Library 0001
    c. python manage.py migrate

6. Now to are all set to run the project. Just run the below command and paste [http](http://127.0.0.1:8000/) in the address bar of your browser.
    a. python manage.py runserver 
    
    
