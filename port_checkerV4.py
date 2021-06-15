#time
#color for not connected
#check for Request per second

import argparse
import threading
import socket


parser= argparse.ArgumentParser(description="Port checker")
parser.add_argument('-u','--url',help="Url Or host",default='127.0.0.1')
parser.add_argument('-p','--ports',help="how many ports to scan default(1000)",default=1000,type=int)
parser.add_argument('-t','--threads',help="Total threads to use default(30)",type=int,default=30)
parser.add_argument('-b','--timeout',help="timeout to inspect a port", default=3,type=int)
args=parser.parse_args()



#host='127.0.0.1'



values=[i for i in range(1,args.ports)]
values=values[::-1]
lock=threading.Lock()
print('---'*10)
print(' '*10)

flag=0

def formater(x):
    print(f'\x1b[s Checking number({x})  \x1b[u',end='')


def target_fuction(i):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(args.timeout)
    try:

        s.connect((args.url,i))
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
    threads_ = [threading.Thread(target=printer) for x in range(args.threads)]
    for t in threads_: 
        t.start()
    for t in threads_:
        t.join()
main()
print('---'*10)
exit()

