import os
import sys
import urllib.request
import json
from Papago_language_detection import language_dection

client_id = "4GGZaLGX4YRq8ufnEtV0" # 개발자센터에서 발급받은 Client ID 값
client_secret = "XZ1FFffklI" # 개발자센터에서 발급받은 Client Secret 값
pld = language_dection()

try :
    print("텍스트를 입력하세요.")
    text = input()
    language_type = eval(pld.api_request(text))
    language_type = language_type["langCode"]
    encText = urllib.parse.quote(text)

    data = "source={0}&target=ko&text={1}".format(language_type, encText)
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        response_body = json.loads(response_body.decode('utf-8'))
        response_body = response_body["message"]["result"]["translatedText"]
        print(response_body)
    else:
        print("Error Code:" + rescode)

except:
    print("잘못된 입력입니다.")