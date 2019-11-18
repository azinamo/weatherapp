# Weather App    

Project uses the Django Framework.

Install the required dependencies as listed in the composer.json file.

```bash
pip install -r requirements.txt
```
### Database Configuration and Migrations

The project is using sqllite database system

Populate the database tables. 
```bash
python manage.py migrate
```

Weather api can be accessed using following url 
```bash
/api/weather
```
Use registered email and password to get access to the api
