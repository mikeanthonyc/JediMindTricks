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


#**Lightweight and Easily Modifiable for Your Own Use**

This tool is designed primarily for local use on your own machine or private network as a hands-on learning, development, and testing platform. It offers realistic and practical applications such as:

Encryption Practice – Gain experience with secure symmetric key communication in real time.

Red Team Skill Building – Safely experiment with command execution, encrypted messaging, and basic persistence techniques without needing complex virtual labs or external infrastructure.

Single-Machine Simulations – Run both the server and client on the same system, or within virtual machines or containers, to simulate attack and defense scenarios effectively.
