from pathlib import Path
import os
import sys
BASE_DIR = str(Path(__file__).resolve().parent.parent)
command = sys.argv
maincom = command[1]
 
if maincom.lower() == "-run" or maincom.lower() == "-r":
    os.system(f"{BASE_DIR}\\RUN.bat")
elif maincom.lower() == "-stop" or maincom.lower() == "-stop":
    os.system(f"{BASE_DIR}\\STOP.bat")
elif  maincom.lower() == "-install" or maincom.lower() == "-i":
    os.system(f"setx PATH \"{Path(__file__).resolve()};%PATH%\"")
    
    

    # run install
    com1 = f"cd .. && {BASE_DIR}\\install.exe"
    os.system(com1)

    #getting script ready
    os.system(f"cd .. && cd application && RUN_SCRIPT.exe")

    #get checking output of install
    with open(f"{BASE_DIR}//BASE_DIR.txt",'r') as paths:
        Paths =paths.read().split('\n')

    #make admin account
    python = Paths[1]
    username = command[2]
    password = command[3]
    # print(Paths)
    with open(f"{BASE_DIR}//cred.txt",'w') as paths:
        Paths =paths.write(f"{username}\n{password}")
    com2 = f"cd .. && {python} make_admin.py"
    # print(com2)
    os.system(com2)
    