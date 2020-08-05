# 中文
## 环境准备
* 需要有selenium库
* 需要有最新版谷歌浏览器和谷歌浏览器驱动程序
## ```淘宝抢单.py```操作步骤
1. 复制你需要的商品的**网页链接**后打开程序
2. 先选择是训练模式还是真实抢购预备模式，训练模式按1，真实模式按2。
3. 打开手机淘宝准备扫码登录，程序首先会要求您需要输入抢单时间，格式务必不能输错，按照程序中的提示进行输入（输错了重启程序即可），然后输入商品网址链接。
4. 等待进入二维码登录页面，扫码登录完成之后，**回到程序界面按回车继续运行程序**。
5. 进入商品界面，**选好款式后回到程序按回车**，**若不需要选款式也需要回到程序按回车**（无法自动选款式，因为不同商品有不同款式）。
6. 到时间后程序会第一时间提交订单，若提交成功，可以按回车退出程序，若提交失败，您可以继续手动提交。
## ```淘宝下单2(针对bp页面链接).py```操作步骤
1. 复制好**确认商品订单BP页面的链接**后打开程序
2. 选择是训练模式还是真实抢购预备模式，训练模式按1，真实模式按2。
3. 程序首先会要求您需要输入抢单时间，格式务必不能输错，按照程序中的提示进行输入（输错了重启程序即可），然后输入商品网址链接。
4. 在登录页面用自己的手机号登录，完成验证后点击登录，进入确认订单页面后，**回到程序按回车**。
5. **确认订单BP页面**不需要您选择款式，因为您既然使用该程序，应该知道如何获取URL，而这个URL里面已经选择了款式。
6. 到时间后程序会第一时间提交订单，若提交成功，可以按回车退出程序，若提交失败，您可以继续手动提交
## 注意
1. 仓库中有两个抢单程序
	* 第一个```淘宝抢单.py```适用于所有**商品链接**
	* 第二个```淘宝下单2(针对bp页面链接).py```仅适用于**BP确认订单页面**
2. 如果您不知道如何获取BP确认订单页面链接，请勿使用第二个程序

# Engilsh
## Environmental preparation
* Selenium library is required
* Need the latest version of Google browser and Google browser driver
## Operation steps
1. Choose training mode or real purchase preparation mode first, press 1 for training mode and 2 for real mode
2. First copy the webpage link of the product you need, and then open the mobile phone Taobao to scan the code for login. First, you need to input the order grabbing time. The format must not be wrong. Input according to the prompts in the program. If you input the wrong product, close the program and open it again. Then enter the product website link.
3. Wait to enter the QR code login page. After scanning the code, return to the program interface and press enter.
4. When you enter the commodity interface, you must select the style first. If you don't need to select the style, you don't need to select it. If you need to select it, you must select it first(In this case, it can't choose the style automatically, because there is different style for different products).
5. When the time is up, the program will click the grab button once at the fastest speed, and the program will only click once, because frequent clicking may be prohibited, so if you don't grab it, you can manually continue. If you grab it, you will enter the payment page. Do not close the program, and close it after payment.