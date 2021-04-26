
rqscheduler --host redis-server --port 6379 &
rqworker --url redis://redis-server:6379 &
python3 /startApp.py