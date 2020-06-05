#####Configure daemon

```
[Unit]
Description=gunicorn daemon
After=network.target

#[Service]
#User=webbfu
#Group=nginx
#WorkingDirectory=/var/www/html/ai2flow/app/ai2flowengine
#ExecStart=/var/www/html/ai2flow/venv/bin/gunicorn --workers 3 --bind unix:/var/www/html/ai2flow/app/ai2flowengine/ai2flowengine.sock app.wsgi:application

[Service]
User=webbfu
Group=nginx
WorkingDirectory=/var/www/html/ai2flow/app
ExecStart=/var/www/html/ai2flow/venv/bin/gunicorn --graceful-timeout 1000000 --timeout 1000000  --access-logfile - --workers 3 --bind unix:/var/www/html/ai2flow/app/ai2flowengine/ai2flowengine.sock ai2flowengine.wsgi:application


[Install]
WantedBy=multi-user.target
```
