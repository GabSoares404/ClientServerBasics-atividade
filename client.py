import time
import random
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
NUM_REQUESTS = 1000

def make_request(request_id):
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
    except Exception as e:
        print(f"Req {request_id} - Erro de conexão: {e}")
        return
        
    commands = [OP_UPPERCASE, OP_REVERSE]
    cmd = random.choice(commands)
    request = f"{cmd} mensagem_de_teste_{request_id}"
    
    s.send(str.encode(request))
    response = s.recv(1024)
    s.close()

def main():
    print(f"Iniciando {NUM_REQUESTS} requisições no modo {MODE}...")
    start_time = time.time()
    
    threads = []
    
    for i in range(NUM_REQUESTS):
        if MODE == "MULTI":
            t = threading.Thread(target=make_request, args=(i,))
            threads.append(t)
            t.start()
        else:
            make_request(i)
            
    if MODE == "MULTI":
        for t in threads:
            t.join()
            
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Tempo total para {NUM_REQUESTS} requisições: {total_time:.4f} segundos")

if __name__ == "__main__":
    main()
