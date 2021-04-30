
rqscheduler --host redis-server --port 6379 &
rqworker --url redis://redis-server:6379 &
gunicorn --bind 0.0.0.0:5000 -w 3 startApp:app

