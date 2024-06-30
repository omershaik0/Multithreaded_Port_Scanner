import socket
import sys
import argparse
import re
import time
import queue
import threading
from colorama import init, Fore, Back, Style

init()
# Colors inside variables
r, g, b = 255, 165, 0


def rgb(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'


background = Back.CYAN + Fore.BLACK
magenta = Fore.MAGENTA
green = Fore.GREEN
red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
yellow = Fore.YELLOW
yellow_bright = rgb(255, 255, 0)
violet = rgb(238, 130, 238)
white = Fore.WHITE
green_bright = rgb(0, 255, 0)
reset = Style.RESET_ALL

script_name = sys.argv[0]

arguments = argparse.ArgumentParser(description="Multi-Threaded Port Scanning tool",
                                    usage=f"python3 {script_name} -l Target IP/Domain -p Target Port(s) -t Threads [optional]")
arguments.add_argument('-l', "--target", help="Enter the Target IP/Domain to scan Ports", required=True)
arguments.add_argument('-p', "--port", help="Enter the Target Port(s) e.g 21 |OR| 22,23,21 |OR| 1-65535", required=True)
arguments.add_argument('-t', "--threads", help="Enter number of Threads, Default is 10 Threads", nargs='?', const=1,
                       type=int, default=10)
args = arguments.parse_args()

target = args.target
port = args.port
threads = args.threads
result = "PORT\tSTATE\tSERVICE\n"


def ip_check(target):
    ip_regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if re.search(ip_regex, target):
        return "Valid IP address"
    else:
        return "Invalid IP address"


if ip_check(target) == "Invalid IP address":
    try:
        target = socket.gethostbyname(target)
    except Exception as e:
        print(e)
        exit()

port_list = re.split('[,-]', port)

current_time = time.ctime()
print(f"\n{magenta}[*] Scanning Started at {current_time}{reset}\n")
print(f"{yellow}[!] Scanning Target {target}:{reset}\n")


def get_banner(ports, s):
    try:
        return s.recv(1024).decode()
    except:
        return 'Not Found'


def port_scan(t_no):
    global result
    while not q.empty():
        ports = q.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            connection = s.connect_ex((target, ports))
            if connection == 0:
                banner = get_banner(ports, s)
                banner = ''.join(banner.splitlines())
                result += f"{red}{ports}{reset}\t{green}OPEN{reset}\t{banner}\n"
            s.close()
        except:
            pass
        q.task_done()


q = queue.Queue()
start_time = time.time()
if "-" in port:
    for j in range(int(port_list[0]), int(port_list[1]) + 1):
        q.put(j)
else:
    for x in port_list:
        int_ports = int(x)
        q.put(int_ports)

for thread in range(threads):
    t = threading.Thread(target=port_scan, args=(thread,))
    t.start()

q.join()
end_time = time.time()
execution_time = end_time - start_time
result_lines = result.split('\n')

if len(result_lines) >= 2:
    second_line = result_lines[1]
    if "OPEN" in second_line:
        print(result)
        print("{}[$] Total Time took for Scanning {:.2f} seconds{}".format(cyan, execution_time, reset))
    else:
        print(f"\n{red}No OPEN Ports Found :({reset}\n")
