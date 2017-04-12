#!/usr/bin/env python
# --coding:utf-8--

import Image,ImageDraw,ImageFont
import os
import random
msgNum = str(random.randint(1,99))#随机生成一个数字，并将其转换为字符串

im = Image.open("/home/jitianze/gitck/python_practise/qq.png")#打开一张图片

w,h = im.size # 获取图片的宽度和高度

wDraw = 0.8*w

hDraw = 0.08*w

font = ImageFont.truetype('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf',30)

draw = ImageDraw.Draw(im)

draw.text((wDraw,hDraw),'99',font=font, fill=(255,33,33))

#draw.text((wDraw,hDraw),msgNum,font=font, fill=(255,33,33))


im.save("/home/jitianze/gitck/python_practise/qq+msg.png",'png')#保存图片位置及格式
