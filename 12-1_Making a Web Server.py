import network
import usocket
import monitor

SSID = "studuinobit"
PASSWORD = "Artecrobo2"

modules = {
    "/monitor.py": "monitor"
}

def launch_ap(ssid, password):
    wlan = network.WLAN(network.AP_IF)
    wlan.config(essid=ssid, password=password, authmode=4, channel=11, hidden=False)
    wlan.active(True)
    return wlan


def launch_webserver(wlan):
    ip_addr = wlan.ifconfig()[0]
    print(ip_addr)

    sock_addr = usocket.getaddrinfo(ip_addr, 80)[0][-1]
    sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
    sock.bind(sock_addr)
    sock.listen(1)

    while True:
        conn, addr = sock.accept()
        print("A client connected from {}.".format(addr))
        req = get_request(conn)
        print(req)
        if req:
            res = make_response(req)
            print(res)
            conn.sendall(res)
        conn.close()


def get_request(conn):
    conn.settimeout(3.0)
    req = bytes()
    try:
        while True:
            data = conn.recv(100)
            req += data
            if len(data) < 100:
                break
    except OSError:
        print("Time out.")
        return False
    else:
        return req.decode("utf-8")


def make_response(req):
    method_name = req[:req.find(" ")]

    if method_name != "GET":
        status = "HTTP/1.1 405 Method Not Allowed"
        body = "The {} method is not supported on this server.".format(method_name)
        header = {
            "Content-Encoding": "identity",
            "Content-Length": str(len(body.encode("utf-8"))),
            "Content-Type": "text/plain; charset=UTF-8",
            "Server": "MicroPython"
        }
    else:
        req_line = req[:req.find("\n")]
        url = req_line[req_line.find(" ")+1:req_line.rfind(" ")]
        path = url.replace("http://192.168.4.1", "")
        try:
            file = open(path, "rt")
        except OSError:
            status = "HTTP/1.1 404 Not Found"
            body = "The requested document was not found on this server."
            header = {
                "Content-Encoding": "identity",
                "Content-Length": str(len(body.encode("utf-8"))),
                "Content-Type": "text/plain; charset=UTF-8",
                "Server": "MicroPython"
            }
        else:
            status = "HTTP/1.1 200 OK"
            if ".py" in path:
                file.close()
                module = modules[path]
                body, mimetype = eval("{}.main()".format(module))
            else:
                body = file.read()
                file.close()
                mimetype = "text/html"
            header = {
                "Content-Encoding": "identity",
                "Content-Length": str(len(body.encode("utf-8"))),
                "Content-Type": "{}; charset=UTF-8".format(mimetype),
                "Server": "MicroPython"
            }

    res = status + "\n"
    for key, val in header.items():
        res += "{}: {}\n".format(key, val)
    res += "\n" + body
    res = res.encode("utf-8")
    return res


wlan = launch_ap(SSID, PASSWORD)
launch_webserver(wlan)
