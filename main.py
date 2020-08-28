import requests, random, time
g=0
def autoreg(g):
    _name=""
    _email = ""
    for x in range(25):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    _email = _name+'@gmail.com'
    cookrand1 = random.randint(0, 99999999999)
    cookrand2 = random.randint(0, 9999999999999999999)
    cookrand3 = random.randint(0, 9999999999)
    cookrand4 = random.randint(0, 999999)
    cookrand5 = random.randint(0, 999)
    uagent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Linux; Android 10; GM1900) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; HRY-LX1MEB) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; MAR-LX1M Build/HUAWEIMAR-L21MEA; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 GSA/11.18.11.21.arm64",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.0 Chrome/79.0.3945.136 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI VNS-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"]
    payload = {"email":_email,"password":password,"checkbox":"true","captcha":""}
    headers = {"User-Agent": uagent[int(random.randint(0, len(uagent)-1))],
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json;charset=utf-8",
    "Content-Length": str(len(payload)),
    "Origin": "https://vto.pe",
    "Connection": "keep-alive",
    "Referer": "https://vto.pe/login",
    "Cookie": "__cfduid=dd"+str(cookrand5)+"d"+str(cookrand4)+"a8f434392d10a56e4bdc"+str(cookrand1)+"; mock=none; _ym_uid="+str(cookrand2)+"; _ym_d="+str(cookrand3)+"; _ga=GA1.2.354857218.1595367593; _gid=GA1.2.394200422.1595367593; _gat=1; _ym_visorc_24016507=w; _ym_isad=2",
    "Host": "vto.pe"}
    r = requests.post("https://vto.pe/webapi/new/register", json=payload, headers=headers)
    if r.text == "":
        li = "-"*(9+len(_email))
        try:
            f = open("test.txt", "a")
            f.write(li+"\nEmail: "+_email+"\nPassword: "+password+"\n")
        finally:
            f.close()
        print(li)
        print("\033[32mEmail:\033[33m",_email,"\033[0m")
        print("\033[32mPassword:\033[33m",password,"\033[0m")
        print("\033[32mPoints:\033[33m 100\033[0m")
    else:
        print("\033[31mЖдем смены IP адреса или разблок.\033[0m")
        time.sleep(5)
def accounts():
    count = input("vtohack>>> ")
    for w in range(int(count)):
        autoreg(g)
        time.sleep(2)
accounts()
