# SecureCTRL - Encrypted Command & Control Framework

SecureCTRL is a lightweight, encrypted command and control (C2) framework written in Python. It uses symmetric encryption (Fernet from the Cryptography library) to securely send commands from a controller (server) to a client agent and receive encrypted responses. 

## Features
- Encrypted communication using Fernet symmetric encryption
- Simple GUI controller built with Tkinter for command sending and output display
- Persistence capability to maintain client presence on Windows systems
- Cross-network communication via TCP sockets
- Modular code for easy expansion and customization

## How it Works
1. The server generates an encryption key and shares it with the client upon connection.
2. The server sends encrypted commands to the client.
3. The client decrypts the commands, executes them (or handles special commands like enabling persistence), then encrypts and sends back the result.
4. The server decrypts and displays the output in the GUI.

## Installation

1. Clone this repository:
