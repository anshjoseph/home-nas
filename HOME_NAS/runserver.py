from waitress import serve
from HOME_NAS.wsgi import application


#inbuf_overflow = 1073741824 *6
if __name__ == '__main__':
	serve(application,host='localhost',port=8080,max_request_body_size = 1073741824 * 6)
