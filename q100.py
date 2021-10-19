import requests,json
requests=requests.Session
headers={
    'Host':'api.m.jd.com',
    'cookie':'pin=jd_64d2983c0c155;wskey=AAJA7Mubf3QZuUT4BJAWk5A-qwrtHYuVC4Nco3PF7up-ce_C92-KD49r02B2W_VWtwU0xqd2GzHFhiMqOxPmg;whwswswws=meQeTpL+aY02ci6jxV1qH+xIFzStf2fdc4KKZtM14bwolvbTTzxchZVuBeaNv0wlhj6XFn7y+ZSWbK4Gn2i+jzuJ4FZzMzm++NB7eOeskDew=;unionwsws={"devicefinger":"eidA02478121f6se5WKkFwYOTPC8kfmzeRkQMuVipZNcF7f7BwLIBsv+CdKShizIbhD0n3Bn6aW2nSgwF7MMTbqeA1YfwyE0Q1h9SZGw\/v+HJ\/lcD\/Bo","jmafinger":"meQeTpL+aY02ci6jxV1qH+xIFzStf2fdc4KKZtM14bwolvbTTzxchZVuBeaNv0wlhj6XFn7y+ZSWbK4Gn2i+jzuJ4FZzMzm++NB7eOeskDew="}',
    'jdc-backup':'pin=jd_64d2983c0c155;wskey=AAJU4A7Mubf3QZuUT4BJAWk5A-qwrtHYuVC4Nco3PF7up-ce_C92-KD49r02B2W_VWtwU0xqd2GzHFhiMqOxPmg;whwswswws=meQeTpL+aY02ci6jxV1qH+xIFzStf2fdc4KKZtM14bwolvbTTzxchZVuBeaNv0wlhj6XFn7y+ZSWbK4Gn2i+jzuJ4FZzMzm++NB7eOeskDew=;unionwsws={"devicefinger":"eidA02478121f6se5WKkFwYOTPC8kfmzeRkQMuVipZNcF7f7BwLIBsv+CdKShizIbhD0n3Bn6aW2nSgwF7MMTbqeA1YfwyE0Q1h9SZGw\/v+HJ\/lcD\/Bo","jmafinger":"meQeTpL+aY02ci6jxV1qH+xIFzStf2fdc4KKZtM14bwolvbTTzxchZVuBeaNv0wlhj6XFn7y+ZSWbK4Gn2i+jzuJ4FZzMzm++NB7eOeskDew="};',
    'charset''UTF-8',
    'accept-encoding':'br,gzip,deflate',
    'user-agent':'okhttp/3.12.1;jdmall;android;version/10.1.4;build/90060;screen/1080x2340;os/10;network/wifi;'

def login():
    url='https://api.m.jd.com/client.action?functionId=stationPullServiceV1008&t=1633744690034&appid=MessageCenter&clientVersion=10.1.4&build=90060&client=android&d_brand=vivo&d_model=V1838A&osVersion=10&screen=2340*1080&partner=vivo&oaid=33012dd5e3420876d218673d0d48c2d4fe3be4d2e8690bf30de55aeb745e4017&openudid=dffa96232996e7e5&eid=eidA02478121f6se5WKkFwYOTPC8kfmzeRkQMuVipZNcF7f7BwLIBsv+CdKShizIbhD0n3Bn6aW2nSgwF7MMTbqeA1YfwyE0Q1h9SZGw/v+HJ/lcD/Bo&sdkVersion=29&lang=zh_CN&uuid=dffa96232996e7e5&aid=dffa96232996e7e5&area=22_1930_49324_0&networkType=wifi&wifiBssid=unknown&uts=0f31TVRjBSvkI0yIAfrTGXtK1Nv3Q%2FagmEA1zssgQhviR3Oo1UA%2FtH9Vm93LHGhoSaaAqdiE7c6JORbh8GCtd0BnicmTKKnwN6GbX5TV57gZsV6DDfXEwUem30%2FTjv8Y7xkJSyQPIxnIeHIbPlovvMmWQBrM3pUnDdg7MFO9seSqcU2szGHdy9uTQc%2Bz%2FA7Cok5lHNIDThHoRitdtw2rnw%3D%3D&uemps=0-0&harmonyOs=0&sign=100bd919aa966ef7ab62c917e698db8b0988663177a146cf02ea50e3bc245bd2'
    data='body=%7B%22pageId%22%3A%22MyJD%22%7D&'
    k=requests.post(url=url,headers=headers,data=data)
    l=k.json()
    print(l)
login()
   
   
   
