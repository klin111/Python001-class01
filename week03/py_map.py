import fire
from concurrent.futures import ThreadPoolExecutor
import subprocess


def ping(ip):
    p=subprocess.run(['ping','ip','-t','1'])

def nc():
    port_range='1-1024'
    n=subprocess.run(['nc','rz','w','2','ip','port_range' ])

def ping_f(n, f, ip):
    # 把ip地址格式标准化，用map方式加入线程池
    if f == 'ping':

        print(111 )
     
    elif f == 'tcp':
       
        print(2222)
    else:
        print("please choose -f args  'ping' or 'tcp' function!")

fire.Fire(ping_f)

