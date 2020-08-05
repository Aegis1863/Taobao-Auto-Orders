# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:27:53 2020

@author: LiSunBowen
"""


from selenium import webdriver
import time
import datetime
def get_time_url():
    input('>> 使用方法：先将你的商品网页链接复制下来，以便后续输入\n中途需要扫码登录，登录完成后回到程序，跟随提示按回车\n***抢到单后会进入支付页面，切勿关闭程序，会导致浏览器一起关闭***\n>>阅读完毕按回车即可继续...')
    print('>> 默认时间是2020-07-20 00:00:00\n')
    date=str(input('>> 输入抢单日期【英文减号隔开】：'))
    seconds=str(input('>> 输入抢单时间(00:00:00~23:59:59)【英文冒号隔开】：'))
    if date == '' :
        date='2020-07-20'
    if seconds== '' :
        seconds='00:00:00.0'
    times=date+' '+seconds+'.0'
    url=str(input('>> 输入商品网页链接：'))
    if url =='':
        url='https://detail.tmall.com/item.htm?spm=a230r.1.14.1.5cc35102XAIJpL&id=609908639171&ns=1&abbucket=12&tbpm=1'
    return times,url

def buy(times, url2, train):
    url='https://www.taobao.com/'
    #有IP池就用以下注释的方法代替现有方法
    #chromeOptions = webdriver.ChromeOptions()
    #chromeOptions.add_argument("--proxy-server=http://202.20.16.82:10152")
    #driver=webdriver.Chrome(chrome_options = chromeOptions)
    driver=webdriver.Chrome()
    try:
        driver.get(url)
        driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "h", " " ))]').click()
        driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "icon-qrcode", " " ))]').click()
    except:
        print('出现错误，您尝试登录的次数过多，被拒绝访问，请关闭程序，一段时间后重试')
    print('暂停运行...')
    input('>>> 扫码登录完成后回到程序按回车，等待中...\n')
    print('继续运行...')
    driver.get(url2)
    print('>> 请选择款式并回到程序按回车，等待中...')
    driver.find_element_by_xpath('//*[(@id = "J_LinkBuy")]').click()
    print('***>已点击购买，到时间后自动提交订单\n')
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        endtime = datetime.datetime.strptime(times , '%Y-%m-%d %H:%M:%S.%f')
        nowtime = datetime.datetime.strptime(now , '%Y-%m-%d %H:%M:%S.%f')
        if nowtime > endtime:
            try:
                if train == 2 :
                    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "go-btn", " " ))]').click()
                    print('***>已下订单\n')
                break
            except:
                print('可能出现网络问题，请尽快手动抢单')    
                break
        else:
            period = endtime - nowtime
            print('>>距离抢单还有 %f 秒\n'%period.total_seconds(),end='\r')

if __name__ == '__main__':
    train=int(input('练习模式最终不会提交订单，若是练习模式按1并回车，若是真实抢购按2并回车：'))
    times,turl=get_time_url()
    buy(times,turl,train)
    input('>> 【注意】 ***如果抢到请勿关闭程序，否则会导致浏览器关闭***  继续支付完成后按回车退出程序\n')
    input('>> 【再次警告】***未完成支付请勿关闭程序*** 支付完成之后按回车退出程序\n')
    input('>>  完成支付后按回车，关闭程序\n')
