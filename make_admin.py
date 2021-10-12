import os

with open("BASE_DIR.txt",'r') as file:
    data = (file.read()).split('\n')
with open("cred.txt",'r') as cred:
    Cred = (cred.read()).split('\n')
os.remove("cred.txt")
os.system(f"echo from django.contrib.auth.models import User; User.objects.create_superuser(\"{Cred[0]}\",\"temp@mail.com\",\"{Cred[1]}\") | {data[1]} {data[0]}\\HOME_NAS\\manage.py shell")
with open("cred.txt",'x') as file:
    pass