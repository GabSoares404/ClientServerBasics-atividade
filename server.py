import threading
from socket import *
from constCS import *

# ==========================================
# CONFIGURAÇÃO DO EXPERIMENTO
# Cenários:
# A: client MODE = "SINGLE", server MODE = "SINGLE"
# B: client MODE = "SINGLE", server MODE = "MULTI"
# C: client MODE = "MULTI",  server MODE = "MULTI"
# ==========================================
MODE = "MULTI"  # Mude para "SINGLE" para testar o cenário single-thread

def process_uppercase(text):
    return text.upper()

def process_reverse(text):
    return text[::-1]

def process_and_reply(conn, data):
    decoded_data = bytes.decode(data)
    
    # Parse request
    parts = decoded_data.split(' ', 1)
    if len(parts) >= 2:
        command = parts[0]
        text_data = parts[1]
        
        # Process based on command
        if command == OP_UPPERCASE:
            response = process_uppercase(text_data)
        elif command == OP_REVERSE:
            response = process_reverse(text_data)
        else:
            response = "ERROR: Unknown command."
    else:
        response = "ERROR: Invalid format. Expected 'COMMAND data'."
        
    conn.send(str.encode(response))
    conn.close()

s = socket(AF_INET, SOCK_STREAM) 
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(100) # Fila maior para suportar testes de carga
print(f"Servidor escutando em {HOST}:{PORT} (Modo: {MODE})...")

while True:
    try:
        (conn, addr) = s.accept()
        data = conn.recv(1024)
        
        if not data: 
            conn.close()
            continue
            
        if MODE == "MULTI":
            # Dispara nova thread exclusivamente para processar e retornar a resposta
            t = threading.Thread(target=process_and_reply, args=(conn, data))
            t.start()
        else:
            # Processa na própria thread (sequencial)
            process_and_reply(conn, data)
            
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
        break
    except Exception as e:
        print(f"Erro: {e}")

s.close()
