# 네이버 Papago 언어감지 API 예제
import os
import sys
import urllib.request

class language_dection:

    def __init__(self):
        
        self.client_id = "SMENmviRhsrFtjKUt7hn"
        self.client_secret = "tXuOMNIbLD"

    def api_request(self, text):
        encQuery = urllib.parse.quote(text)
        data = "query=" + encQuery
        url = "https://openapi.naver.com/v1/papago/detectLangs"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",self.client_id)
        request.add_header("X-Naver-Client-Secret",self.client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            return response_body.decode('utf-8')
        else:
            print("Error Code:" + rescode)