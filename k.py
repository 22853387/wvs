import requests,json
requests=requests.Session()
u=input("输入你的cookie")
headers={
    'Host':'api.m.jd.com',
    'cookie':u,
    'charset':'UTF-8',
    'accept-encoding':'br,gzip,deflate',
    'user-agent':'okhttp/3.12.1;jdmall;android;version/10.1.4;build/90060;screen/1080x2340;os/10;network/wifi;'
    }
def login():
    url='https://api.m.jd.com/client.action?functionId=stationPullServiceV1008&t=1633744690034&appid=MessageCenter&clientVersion=10.1.4&build=90060&client=android&d_brand=vivo&d_model=V1838A&osVersion=10&screen=2340*1080&partner=vivo&oaid=33012dd5e3420876d218673d0d48c2d4fe3be4d2e8690bf30de55aeb745e4017&openudid=dffa96232996e7e5&eid=eidA02478121f6se5WKkFwYOTPC8kfmzeRkQMuVipZNcF7f7BwLIBsv+CdKShizIbhD0n3Bn6aW2nSgwF7MMTbqeA1YfwyE0Q1h9SZGw/v+HJ/lcD/Bo&sdkVersion=29&lang=zh_CN&uuid=dffa96232996e7e5&aid=dffa96232996e7e5&area=22_1930_49324_0&networkType=wifi&wifiBssid=unknown&uts=0f31TVRjBSvkI0yIAfrTGXtK1Nv3Q%2FagmEA1zssgQhviR3Oo1UA%2FtH9Vm93LHGhoSaaAqdiE7c6JORbh8GCtd0BnicmTKKnwN6GbX5TV57gZsV6DDfXEwUem30%2FTjv8Y7xkJSyQPIxnIeHIbPlovvMmWQBrM3pUnDdg7MFO9seSqcU2szGHdy9uTQc%2Bz%2FA7Cok5lHNIDThHoRitdtw2rnw%3D%3D&uemps=0-0&harmonyOs=0&sign=100bd919aa966ef7ab62c917e698db8b0988663177a146cf02ea50e3bc245bd2'
    data='body=%7B%22pageId%22%3A%22MyJD%22%7D&'
    e=requests.post(url=url,headers=headers,data=data)
    l=e.json()
    print(l)
login()
def jiaoshui():
    url='https://api.m.jd.com/client.action?functionId=waterGoodForFarm&body=%7B%22type%22%3A%22%22%2C%22version%22%3A14%2C%22channel%22%3A1%2C%22babelChannel%22%3A%22121%22%7D&appid=wh5'

    i=requests.get(url,headers=headers).text
    j=json.loads(i)
    global p
    p=int(j.get('totalEnergy'))
jiaoshui()
while p>=10:
    jiaoshui()
    print("正在浇水")
