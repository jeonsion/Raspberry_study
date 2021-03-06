import requests
import datetime as dt
import datetime
#필터를 적용하여 resource 가져오기 la값을 수정하면 컨테이너에 해당하는 cin의 개수만큼 가져올 수 있음 아래처럼 la=250이면 249개의 데이터를 가져온다.
url = "http://203.253.128.177:7579/Mobius/phone/data?fu=2&la=250ty=4&rcn=4"

payload={}
headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'SOrigin'
}

r = requests.get(url, headers = headers)
 
r.raise_for_status()
jr = r.json()
#print(jr)

count = 0
x = dt.datetime.now()
for c in jr['m2m:rsp']['m2m:cin']:
    if(c['con']=='1'):
        count+=1

print(f"약을 복용한 횟수 : {count}")


today = datetime.date.today()
targetday = datetime.date(2022,2,21)

values = today - targetday
print(f"영양제를 복용한 후 경과일 : {values.days}")
print("건강한 사람이 되기위한 과정을 {:.2f} % 실현 중".format((count/150)*100))
