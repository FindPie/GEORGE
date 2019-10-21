from auto_chatting import getdate
from auto_chatting import getWeather
from auto_chatting import getExchangeRate
import itchat

#   私人聊天
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):

    print(msg['Content'])
    return 0

#   群组聊天
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        print(msg['Content'])
        if msg['Content'] == "@发馅 日期":
            American, Beijing, UK, Japan = getdate.get_date()
            print(American)
            itchat.send('American: ' + American + '\n' +
                        'Beijing: ' + Beijing + '\n' +
                        'UK: ' + UK + '\n' +
                        'Japan: ' + Japan + '\n', toUserName=groupName)

        elif msg['Content'] == "@发馅 时间":
            American, Beijing, UK, Japan = getdate.get_time()
            itchat.send('American: ' + American + '\n'+
                        'Beijing: ' + Beijing + '\n'+
                        'UK: ' + UK + '\n'+
                        'Japan: ' + Japan + '\n', toUserName=groupName)

        elif msg['Content'] == "@发馅 天气":
            weather = getWeather.get_weather()
            itchat.send(weather, toUserName=groupName)

        elif "@发馅 汇率" in msg['Content']:
            currency = msg['Content'].replace("@发馅 汇率", '')
            rate = getExchangeRate.get_exchange_rate(currency)
            itchat.send(rate, toUserName=groupName)
    return 0


itchat.auto_login(hotReload=True)

group = itchat.search_chatrooms(name='进城了')
print(group)
groupName = group[0]['UserName']
itchat.send('喝水小助手3.1目前实现功能，@我 并且输入"日期","时间","天气"获得信息,新功能汇率查询为汇率+货币名称，例如"汇率GBP"', toUserName=groupName)

#   想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
users = itchat.search_friends(name='棉棉猪')
#   获取好友全部信息,返回一个列表,列表内是一个字典
print(users)
userName = users[0]['UserName']
#itchat.send('', toUserName=userName)

itchat.run()