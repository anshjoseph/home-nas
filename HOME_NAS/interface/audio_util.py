from interface.error import data_no_found
import requests
import os



def upload_file(ID,file_location,file_name,secret_key=None):
    try:
        os.system(f[\
            "main.exe {file_location}")
        with open(file_name,'rb') as file:
            files = {'file': (file_name, file, 'text/plain')}
            data = {'secret_key':secret_key,"id":ID}
            with requests.session() as client:
                client.get("http://localhost:8000/audio/")
                client.post(data=data,files=files)
        os.remove(file_name)
        return True
    except:
        return False