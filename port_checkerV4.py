#time
#ports
#threads
#url
#timeout
#color for not connected
#check for Request per second


import threading
import socket
host='127.0.0.1'

values=[i for i in range(1,1000)]
values=values[::-1]
lock=threading.Lock()
print('---'*10)
print(' '*10)

flag=0

def formater(x):
    print(f'\x1b[s Checking number({x})  \x1b[u',end='')


def target_fuction(i):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(9)
    try:

        s.connect((host,i))
        #print('\x1b[#F')
        print(f'[+]     \x1b[38;5;46m     connected {i} \x1b[0m',end='\n')
        #print('\x1b[#F')
    except ConnectionRefusedError:
        return
        #print('Closed port')
    except socket.timeout:
        print(f'[+]     \x1b[38;5;208m     Filtered connected {i} \x1b[0m',end='\n')
    except socket.gaierror:
        return
        #print(f'[-]     \x1b[38;5;196m     Not Connected {i} \x1b[0m',end      ='\n')
    except OSError as errors:
        global flag 
        if flag==0:
            print(f'[-]     \x1b[38;5;226m     Not connected to internet  Or Not reachable\x1b[0m',end      ='\n')
            flag=1
        exit()




def printer():
    if len(values)==0:
        return
    while True:
        with lock:
            if len(values)==0:
                return
            x=values.pop()
            formater(x)
        target_fuction(x)
def main():
    global lock
    threads = [threading.Thread(target=printer) for x in range(30)]
    for t in threads: 
        t.start()
    for t in threads:
        t.join()
main()
print('---'*10)
exit()

