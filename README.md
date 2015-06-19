# server_notes
Server app for send json answers and get them
Have rest_django_framework for that
# note
Client app for use information from send app
# How to use?
First-step : Start server_notes (python manage.py runserver) 
Second-step : Start note (python manage.py runserver 8001)
Third-step : Start worker (celery -A config worker -l info)
Fourth-step : use browser on url : localhost:80001
Then you can sign up and use this app