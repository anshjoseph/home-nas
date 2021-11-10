import subprocess

try:
    p=  subprocess.Popen(["start","cmd","/k","cd .. && cd home-nas"],shell=True)
    p.wait()
   
except Exception as e:
    print(e)
