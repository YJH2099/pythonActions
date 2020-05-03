# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:38:23 2020

@author: jianhua.yang
"""

import turtle as pen
import numpy as np

screen = pen.getscreen()  #获取pen的屏幕
screen.title("Python蝴蝶动画")  #设置屏幕的标题
pen.screensize(500, 500, bg="grey") #设置绘图区和背景色
pen.shapesize(0.5,0.5,1)#设置画笔的比例，这里是没用的因为是隐藏画笔
pen.hideturtle()#隐藏画笔

pointnumber = 2000#设置蝴蝶点数
screenCoe=50#设置蝴蝶上点与绘图的比例
'''
画像素点，如果画不笔抬起，则是画直线
'''
def drawPixel(x,y):
    pen.down()#画笔按下
    pen.goto(x,y)#画笔到（x,y）位置
#    pen.dot(2)#画笔点的形式
'''
    计算蝴蝶上的点数据（共n个点）
'''
def drawButterfly(n):
    px = []#设置x轴数据链表
    py = []#设置y轴数据链表
    for num in range(0,n-1):
        t = 12*np.pi*num/(n-1)
        x = np.sin(t)*(np.e**np.cos(t) - 2*np.cos(4*t)-np.sin(t/12)**5)
        y = np.cos(t)*(np.e**np.cos(t) - 2*np.cos(4*t)-np.sin(t/12)**5)
        px.append(x)
        py.append(y)   
    return(px,py)
    
(px1,py1) = drawButterfly(pointnumber)  #获取点数据

for num in range(1,len(px1)):
    if num==1:#将画图移动到第一个点
        pen.penup()
        pen.goto(px1[num]*screenCoe,py1[num]*screenCoe)              #设置图片点的比例，以与绘图区匹配
    else:
        if px1[num]<0:#左侧设置一种颜色
            pen.color("gold")      
        else:#右侧设置一种颜色
            pen.color("gold")
        pen.delay(0)#画笔无延迟
        pen.speed(0)#画图的速度
        drawPixel(px1[num]*screenCoe,py1[num]*screenCoe)
pen.done()#画图完成

