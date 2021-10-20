import requests,json
u=input("输入你的cookie")
url='https://comm.ams.game.qq.com/ams/ame/amesvr?ameVersion=0.3&sServiceType=start&iActivityId=407796&sServiceDepartment=group_l&sSDID=febf9f32af4f2d90dedae9cf6d42138c&sMiloTag=AMS-MILO-407796-809290-o1666149353-1634723503687-Suu8i3&_=1634723503691'
headers={
    'Host':'comm.ams.game.qq.com',
    'content-length':'364',
    'sec-fetch-mode':'cors',
    'origin':'https://start.qq.com',
    'user-agent':'Mozilla/5.0(Linux; Android 10;V1838A) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
    'content-type':'application/x-www-form-urlencoded',
    'accept':'*/*',
    'sec-fetch-site':'same-site',
    'referer':'https://start.qq.com/act/a202110/?viptoken=ce68c5d0604aceff9863363dbce4234d',
    'accept-encoding':'gzip,deflate,br',
    'accept-language':'zh-CN,en-US;q=0.9',
    'cookie':u,
}
data='gameId=&sArea=&iSex=&sRoleId=&iGender=&sServiceType=start&objCustomMsg=&areaname=&roleid=&rolelevel=&rolename=&areaid=&iActivityId=407796&iFlowId=809290&g_tk=696630012&e_code=0&g_code=0&eas_url=http%3A%2F%2Fstart.qq.com%2Fact%2Fa202110%2F&eas_refer=http%3A%2F%2Fnoreferrer%2F%3Freqid%3D1beaebd2-86b2-4706-9412-504b801301a1%26version%3D24&sServiceDepartment=group_l'
k=requests.post(url=url,headers=headers,data=data).text
print(k)