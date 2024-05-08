from http.server import HTTPServer,SimpleHTTPRequestHandler
import sys
from threading import Thread
import subprocess


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="./static/", **kwargs)



if len(sys.argv) == 3:
    try:
        server = HTTPServer((sys.argv[1], int(sys.argv[2])), Handler)
        t = Thread(target=server.serve_forever, args=[0.5])
        t.start()
        print(f"\n[+]\tHttp server started!")
    except Exception:
        print(f"\n[-]\tCouldn't start http server!")
        

else:
    print(f"\n[usage]\n\tngrook.py [ip here] [port here]")
    exit(1)


def ngrok():
    try:
        subprocess.run(['ngrok', 'http', f'http://{sys.argv[1]}:{sys.argv[2]}'])
    except Exception:
        raise Exception


try:
    print(f"\n[+]\tStarting ngrok...\n")
    ngrok()
except Exception:
    print(f"\n[-]\tCouldn't start ngrok, maybe you don't have it installed or it's not configured yet!")
