# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:27:53 2020

@author: LiSunBowen
"""


from selenium import webdriver
import datetime

def get_time_url():
    #input('>> 使用方法：先将你的商品网页链接复制下来，以便后续输入\n中途需要扫码登录，登录完成后回到程序，跟随提示按回车\n***抢到单后会进入支付页面，切勿关闭程序，会导致浏览器一起关闭***\n>>阅读完毕按回车即可继续...')
    print('>> 默认时间是{}\n'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
    date=str(input('>> 输入抢单日期【英文减号隔开】：'))
    seconds=str(input('>> 输入抢单时间(00:00:00~23:59:59)【英文冒号隔开】：'))
    if date == '' or seconds == '':
        times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    times = date+' '+seconds+'.0'
    url=str(input('>> 输入商品网页链接：'))
    if url =='':
        url='https://h5.m.taobao.com/cart/order.html?itemId=619506446365&skuId=4543697726511&quantity=1&buyNow=true'
    return times,url

def buy(times,url,train):
    driver=webdriver.Chrome()
    driver.get(url)
    input('>>> 登录完成后按回车\n')
    print('继续运行...')
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        endtime = datetime.datetime.strptime(times , '%Y-%m-%d %H:%M:%S.%f')
        nowtime = datetime.datetime.strptime(now , '%Y-%m-%d %H:%M:%S.%f')
        if nowtime > endtime:
            try:
                if train == 2 :
                    try:
                        driver.find_element_by_xpath('//*[@id="submitBlock_1"]/div/div/div/div[3]/div[2]/span').click()
                        print('***>已下订单\n')
                    except:
                        driver.find_element_by_xpath('//*[@id="submitOrder_1"]/div[2]/div[2]/div/span').click()
                        print('***已下订单\n')
                break
            except:
                print('可能出现网络问题，请尽快手动抢单')    
                break
        else:
            period = endtime - nowtime
            print('>>距离抢单还有 %f 秒\n'%period.total_seconds(),end='\r')
    pass

def main():
    train=int(input('练习模式最终不会提交订单，若是练习模式按1并回车，若是真实抢购按2并回车：'))
    times,url=get_time_url()
    buy(times,url,train)
    input('>> 【注意】 已经尝试提交订单，如果提交成功，可以按回车关闭程序，同时也会关闭网页。\n')
    input('>> 【再次确认】确认无误后按回车关闭程序\n')
    
if __name__ == '__main__':
    main()
