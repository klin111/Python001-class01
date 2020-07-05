import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
'Referer' : 'https://shimo.im/login?from=home',
'cookie':'_csrf=JwEVi00_WCxOOt0qwextHRp_; deviceId=26f04431-c718-4504-8763-5ba8da3cf78d; deviceIdGenerateTime=1593857186397; shimo_gatedlaunch=3; shimo_kong=7; shimo_svc_edit=2168; sensorsdata2015session=%7B%7D; Hm_lvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1593857197; _bl_uid=d2k0bcqt7Okh0tfgRcFq6nwnnI4O; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2214350757%22%2C%22%24device_id%22%3A%22173194aa2d3a1f-038380d324ea67-31627403-1296000-173194aa2d490c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F18%3Farticle%3D253882%22%2C%22%24latest_referrer_host%22%3A%22u.geekbang.org%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22173194aa2d3a1f-038380d324ea67-31627403-1296000-173194aa2d490c%22%7D; anonymousUser=-8155657932; shimo_sid=s%3AIoU5mbClfUR5KEWCOM6OMrK1Rv2lWIHV.yWAWTf6fTmj%2FbUrsLVFA9UUVhf4H71Hgh2Kzq%2Fa2VoQ; Hm_lpvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1593935347',
'origin': 'https://shimo.im',
'pragma': 'no-cache',
'x-requested-with': 'XmlHttpRequest'
}

s = requests.Session()
# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie， 
# 期间使用 urllib3 的 connection pooling 功能。
# 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
# login_url = 'https://accounts.douban.com/j/mobile/login/basic'
login_url='https://shimo.im/lizard-api/auth/password/login'
# login_url= 'https://shimo.im/login?from=home'
form_data = {
'email': 'klin111@qq.com',
'mobile': '+86undefined',
'password': '123456'
}

response = s.post(login_url, data = form_data, headers = headers)


print('Status Code: %s' % response.status_code)

# 登录之后访问某个页面，验证登录是否成功
response = s.get('https://shimo.im/dashboard', headers=headers)
print('Status Code: %s' % response.status_code)
# print('Body: %s' % response.text)

# 登陆后可以进行后续的请求
# url2 = 'https://accounts.douban.com/passport/setting'

# response2 = s.get(url2,headers = headers)
# response3 = newsession.get(url3, headers = headers, cookies = s.cookies)

# with open('profile.html','w+') as f:
    # f.write(response2.text)
