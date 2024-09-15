import multiprocessing

bind = "unix:/run/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "info"
