import socket
import time
import threading

threads=[]

target=input("Enter a IP for scanning ")
start=time.time()


with open("result.txt","w") as f:
    f.write(f"Scan results for {target}\n")
    f.write("="*30+"\n")
def scan_port(port):
        s=socket.socket()
        s.settimeout(0.5)
        result=s.connect_ex((target,port))
        with open("result.txt", "a") as f: 
         if result==0:
            print(f"Port {port} --->Open")
            f.write(f"Port {port} --> OPEN\n")
         else:
            print(f"Port {port} --->Closed")
            f.write(f"Port {port} --> Closed\n")
        s.close()
    
for port in range(20,1025):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()
        
for t in threads:
    t.join()

end=time.time()
elapsed=round((end-start),2)

with open("result.txt","a") as f:
    f.write(f"\n Scan complete in {elapsed} seconds")
    
    
print(f"\nScan complete in {elapsed} seconds")
print("Results saved to results.txt") 

