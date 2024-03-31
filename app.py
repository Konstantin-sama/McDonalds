import redis

red = redis.Redis(host='localhost', port=6379)

# (virtualenv) $ pip3 install redis
# (virtualenv) $ pip3 install -U "celery[redis]"

# 1)
# python3 manage.py runserver
# 2)
# celery -A proj_name worker -l INFO