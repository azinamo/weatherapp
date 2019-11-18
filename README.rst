===========
Weather App
===========

WeatherApp is a simple Django app to display weather forecast.

Quick start
-----------

1. Add "weatherapp" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'weatherapp',
    ]

2. Include the weatherapp URLconf in your project urls.py like this::

    path('weatherapp/', include('weatherapp.urls')),

3. Run `python manage.py migrate` to create the weatherapp models.

3. Run `python manage.py fetch_forecast` to fetch Cape Town weather forecast.

4. Start the development server and visit http://127.0.0.1:8000/admin/
    (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/weather/ to access the app.