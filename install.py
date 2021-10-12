import sys
import os
from pathlib import Path
BASE_DIR = str(Path(__file__).resolve().parent).replace('\\','/')

TEMP1 = """
server {
	listen 80;
	server_name HOME_NAS;
	charset utf-8;
	client_max_body_size 75000M;
	location /media {
    """
		# alias D:/potable_python/WPy32-3901/HOME_NAS/media;
TEMP2="""
	}
	location /static {
    """
		# alias D:/potable_python/WPy32-3901/HOME_NAS/static;
TEMP3 = """
	}
	location / {
		proxy_pass http://127.0.0.1:8080;
	}

}

"""
IMP1 = f"alias {BASE_DIR}/HOME_NAS/media;"
IMP2 = f"alias {BASE_DIR}/HOME_NAS/static;"

SRVER_CONFIG_ADDON = TEMP1+ IMP1 + TEMP2 +IMP2 +TEMP3
del(TEMP1)
del(TEMP2)
del(TEMP3)
del(IMP1)
del(IMP2)

TEMP1 = """

#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
"""
IMP1 =  f"include     {BASE_DIR}/nginx-1.20.1/sites-enabled/webproject_nginc.conf;"
TEMP2 = """
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;
    
    server {
        listen       10;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            index  index.html index.htm;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}

"""
SRVER_CONFIG = TEMP1 + IMP1 + TEMP2
del(TEMP1)
del(TEMP2)
del(IMP1)



if __name__ == '__main__':
    with open(BASE_DIR + '/nginx-1.20.1/sites-enabled/webproject_nginc.conf','w') as file:
        file.writelines(SRVER_CONFIG_ADDON)
    with open(BASE_DIR + '/nginx-1.20.1/sites-available/webproject_nginc.conf','w') as file:
        file.writelines(SRVER_CONFIG_ADDON)
    with open(BASE_DIR + '/nginx-1.20.1/conf/nginx.conf','w') as file:
        file.writelines(SRVER_CONFIG)
    BASE_DIR = BASE_DIR.replace('/','\\')
    IMP_WRITE = BASE_DIR + "\n" + BASE_DIR + "\\python-3.9.0rc1\\python.exe" + "\n" + BASE_DIR + "\\HOME_NAS\\runserver.py" + "\n" + BASE_DIR + "\\nginx-1.20.1\\nginx.exe"
    try:
        with open('BASE_DIR.txt','x') as file:
            file.write(IMP_WRITE)
    except:
        with open('BASE_DIR.txt','w') as file:
            file.write(IMP_WRITE)
   