from httpx import Client
from httpx_socks import SyncProxyTransport
from requests import get
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from subprocess import check_output

print('''



     ██╗  ██╗██╗   ██╗██╗     ██╗███╗   ██╗ █████╗     ████████╗███████╗ █████╗ ███╗   ███╗
     ╚██╗██╔╝╚██╗ ██╔╝██║     ██║████╗  ██║██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
      ╚███╔╝  ╚████╔╝ ██║     ██║██╔██╗ ██║███████║       ██║   █████╗  ███████║██╔████╔██║
      ██╔██╗   ╚██╔╝  ██║     ██║██║╚██╗██║██╔══██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
     ██╔╝ ██╗   ██║   ███████╗██║██║ ╚████║██║  ██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║
     ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                                                      


''')                                                                                  

exec=ThreadPoolExecutor(max_workers=1000000)
proxy=open("proxy.txt", encoding='utf-8').read().splitlines()
print("[!] Proxy loaded successfully")
proxyn=0
token_l=open("token.txt", encoding='utf-8').read().splitlines()
print("[!] Token loaded successfully")
invite_code=input("[!] invite link or code >> ").replace("discord.gg/invite/","").replace("discord.gg/","").replace("http://","").replace("https://","")
print(invite_code)

def get_p():
    global proxy,proxyn
    try:
        p=proxy[proxyn]
        proxyn+=1
    except:
        p=proxy[0]
        proxyn=0
    return p.replace("\n","")

def check_invite(code):
    req = Client().get(f"https://discord.com/api/v9/invites/{code}?with_counts=true&with_expiration=true",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"})
    st = req.status_code
    if st == 200:
        return True,"working"
    elif st == 404:
        return False,"code not found"
    else :
        return False,f"idk error {req.text}"

def join(_):
    try:
        req = Client(transport=SyncProxyTransport.from_url(f'http://{get_p()}')).post(f"https://discord.com/api/v9/invites/{invite_code}",timeout=10,json={},headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US","authorization": _,"cache-control": "no-cache","content-type": "application/json","cookie": "__dcfduid=32e905702ca911ecbfd11de192a08f1c; __sdcfduid=32e905712ca911ecbfd11de192a08f1ccd3272e0b9e60187cc3196a3a7cb5c4599c78788ddc34baa3af81821dfd17596; locale=en-US","origin": "https://discord.com","pragma": "no-cache","referer": "http://discord.com/channels/@me","sec-ch-ua": 'Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',"sec-ch-ua-mobile": "?0","sec-ch-ua-platform": "Windows","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47","x-debug-options": "bugReporterEnabled","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InRoIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk0LjAuNDYwNi44MSBTYWZhcmkvNTM3LjM2IEVkZy85NC4wLjk5Mi40NyIsImJyb3dzZXJfdmVyc2lvbiI6Ijk0LjAuNDYwNi44MSIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDEwNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}).status_code
        if req == 200:
            print(f"[*] token {_[:35]} | join to guild")
        elif req == 403:
            print(f"[!] token : {_} | phone lock TOKEN")
        else:
            print(f"[!] token : {_} | idk error | {req.text}")
    except Exception as e :print(f"[!] token : {_} | proxy died | {e}")

pass_, text = check_invite(invite_code)
if pass_ == True:
    print("[*] invite working")
else:
    print(f"[!] invite has been deleted | {text}")
    exit()

for _ in token_l:
    exec.submit(join,_)
    sleep(1)
exec.shutdown(wait=True)
print("[*] all done")