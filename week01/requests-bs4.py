
import requests
from bs4 import BeautifulSoup as bs
import pandas  as pd
import lxml.etree


user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
cookie='''__mta=214809256.1593232415887.1593232897731.1593233442371.6; uuid_n_v=v1; uuid=3D531450B82F11EAB11C23537EB4C64BA3800A5296EC47AF8627A0F32FD34835; _csrf=d79bafc172ac74be9ecb7dff1b61e12d7b600dddfdcdb7b631e0a5d0da405804; mojo-uuid=5e2311b6b94ded1f9ee10d29e267abad; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593232412; _lxsdk_cuid=172f40d4fa3c8-08dabd60f9b7c3-31627403-13c680-172f40d4fa3c8; _lxsdk=3D531450B82F11EAB11C23537EB4C64BA3800A5296EC47AF8627A0F32FD34835; mojo-session-id={"id":"efa608e8c8a759156def3729ab352912","time":1593269565545}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593269566; __mta=214809256.1593232415887.1593233442371.1593269566815.7; _lxsdk_s=172f6443506-860-f81-7e0%7C%7C3'''

header={'user-agent':user_agent,'cookie':cookie}

myurl='https://maoyan.com/films?showType=3'

response=requests.get(myurl,headers=header)

# print(response.text)
print(f'reponse code:{response.status_code}')

bs_info=bs(response.text,'html.parser')

selector = lxml.etree.HTML(response.text)
film_name = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[2]/text()')
# print(f'电影名称: {film_name}')
print(film_name,'0',sep='')

film_time = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[4]/text()')
print(film_time)


cont=10
n=0
result_list=[]

for m_info in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    if n >= cont:
        break
    # 获取电影name,type,time
        movie_name=None
        movie_time=None
        movie_type=None
    for m in m_info.find_all('div'):
        movie_name=m.get('title')
        span = m.find('span')
        if span.text == '类型:':
            movie_type = m.text.split()[-1]
        elif span.text == '上映时间:':
            movie_time = m.text.split()[-1]
    result={'m_name':movie_name,'m_type':movie_type,'m_atime':movie_time}
    result_list.append(result)
    n += 1

# print(result_list)
# m_cvs=pd.DataFrame(result_list)
# m_cvs.to_csv('./movie.cvs',encoding='utf8',index=False)

