import datetime
import requests

def Get_up_call(apiid,apikey,mobile,message):
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"
        }
        params={
                'account': apiid,
                'password': apikey,
                'content': message,
                'mobile': mobile,
                'format': 'json'
                }
        response = requests.post("http://api.vm.ihuyi.com/webservice/voice.php?method=Submit", params=params, headers=headers, timeout=30)
        response_str = response.content.decode('utf-8')
        print(response_str)
    
def Ontime(hour,minute):
    if(datetime.datetime.now().hour==hour and datetime.datetime.now().minute==minute):
        return True
    else:
        return False



if __name__ == '__main__':
    print(Ontime(20,49))
    while(1):
        if(Ontime(20,49)==True):
            Get_up_call('VM78106739', '87df1f2e8078792f8629ce5bf35f60e7',
                    '13120235355','起床啦起床啦起床啦起床啦起床啦')
            break