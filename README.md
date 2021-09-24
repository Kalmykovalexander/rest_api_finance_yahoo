REST API for Web Scraping by company symbol

Create initial database sqlite:

docker-compose run web python manage.py migrate

Run the Server
$python manage.py runserver

Link API(only GET request) for historical data:
Add a symbol (ex. PD, ZUO, PINS ...) to the end of the url

- /api/history/<slug:company_symbol>/
