#!/usr/bin/python   
# -*- coding: utf-8 -*-   

from chatterbot import ChatBot  
from chatterbot.trainers import ListTrainer

bot = ChatBot("WeChatBot")
bot.set_trainer(ListTrainer)
bot.train([  
    "你叫什么名字？",  
    "我叫小语",  
    "今天天气真好",  
    "是啊，这种天气出去玩再好不过了。",  
    "那你有没有想去玩的地方？",  
    "我想去有山有水的地方。你呢？",  
    "没钱哪都不去",  
    "哈哈，这就比较尴尬了",  
])  
while True:  
    print(bot.get_response(input("user:")))