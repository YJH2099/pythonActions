# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:37:04 2020

@author: jianhua.yang
"""

import math
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog



class data(object):
    def __init__(self):
        self.num1 = 1
        self.num2 = 2
        self.num3 = 0
        self.w0 = 160
        self.h0 = 120
        self.label1 = None
        self.label2 = None
        self.label3 = None
        self.label4 = None
        self.entry1 = None
        self.entry2 = None
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.radiobutton1 = None
        self.radiobutton2 = None
        self.canvas = None

class main():
    data1 = data()
    root = tk.Tk()
  
    root.title('Welcome')
    root.geometry('400x400')
    root.iconbitmap('butterfly.ico')
   
    
    var = tk.IntVar()
    def __init__(self):
        self.createMenu()
        self.creatControl()
        self.mainloop()
        
    
    def createMenu(self):
        menu = tk.Menu(self.root)
        submenu1 = tk.Menu(menu,tearoff=0)
        menu.add_cascade(label='计算',menu=submenu1)
        submenu1.add_command(label='加法',command = lambda: self.showPlusInfo(self.data1)) 
        submenu1.add_command(label='减法',command = lambda: self.showSubInfo(self.data1))
        submenu1.add_command(label='退出',command = self.root.destroy)
       
        submenu2 = tk.Menu(menu,tearoff=0)
        menu.add_cascade(label="窗口",menu=submenu2)
        submenu2.add_command(label="弹出",command =self.newWindow)
        submenu2.add_command(label="另存为",command = self.saveas)
        submenu2.add_command(label="聚焦按键",command=self.focuskey)
        
        self.root.config(menu=menu)  

    def creatControl(self):
        root1 = self.root
        entry1 = tk.Entry(root1,bg='white',fg="red",font=('微软雅黑',12),width=10,relief=tk.GROOVE)
        entry1.grid(column=0,row=0)
        self.data1.entry1 = entry1

        label1 = tk.Label(root1,text='+',font=('微软雅黑',16),width=4,fg="Red")
        label1.grid(column=1,row=0)
        self.data1.label1 = label1
        
        entry2 = tk.Entry(root1,fg="red",font=('微软雅黑',12),width=10,relief=tk.GROOVE)
        entry2.grid(column=2,row=0)
        self.data1.entry2 = entry2       
        
        label2 = tk.Label(root1,text='=',font=('微软雅黑',16),width=4,fg="Red")
        label2.grid(column=3,row=0)
        self.data1.label2 = label2
        
        label3 = tk.Label(root1,text='',fg="red",font=('微软雅黑',12),width=6)
        label3.grid(column=4,row=0)
        self.data1.label3 = label3
        
        button1 = tk.Button(root1,text='加法',bg='green',fg="red",font=('微软雅黑',12),width=10,relief=tk.GROOVE,command = lambda: self.showPlusInfo(self.data1))
        button1.grid(column=0,columnspan = 2,row=1)
        self.data1.button1 = button1
        
        button2 = tk.Button(root1,text='减法',bg='green',fg="red",font=('微软雅黑',12),width=10,relief=tk.GROOVE,command=lambda: self.showSubInfo(self.data1))
        button2.grid(column=2,columnspan = 2,row=1)
        self.data1.button2 = button2        
      
              
        rd1 = tk.Radiobutton(root1,text="加",variable=self.var,value=0,command =lambda:self.radioButton(self.data1))
        rd1.grid()
        self.data1.radiobutton1 = rd1
        
        rd2 = tk.Radiobutton(root1,text="减",variable=self.var,value=1,command =lambda:self.radioButton(self.data1))
        rd2.grid()
        self.data1.radiobutton2 = rd2
        
        
        label4 = tk.Label(root1,text='',fg="red",font=('微软雅黑',12),width=6,relief=tk.GROOVE)
        label4.grid()
#        label4.bind('<Enter>',self.showEvent)
#        label4.bind('<Leave>',self.showLeaveEvent)
        label4.bind('<Key>',self.showkey)
        label4.focus_set()
        self.data1.label4 = label4
        
        button3 = tk.Button(root1,text='画曲线',bg='green',fg="red",font=('微软雅黑',12),width=10,relief=tk.GROOVE,command= self.drawAxis)
        button3.grid()
        self.data1.button3 = button3
        
        cav = tk.Canvas(self.root,width=320,height=240)
        cav.grid()
        self.data1.canvas = cav  
        
    def mainloop(self):
        self.root.mainloop()
    #加法运算   
    def showPlusInfo(self,data1):
        data1.label1['text'] = '+'  
        
        str1 = self.data1.entry1.get()
        str2 = self.data1.entry2.get()       


        if self.is_alphabet(str1) or self.is_alphabet(str2):
            self.showErrorMessage()
            self.data1.entry1.delete(0,tk.END)
            self.data1.entry2.delete(0,tk.END)
            self.data1.label3['text']=""
            return       
        
        data1.num3 = float(str1) + float(str2)
        new_text = '{}'.format(data1.num3)
         
        data1.label3['text'] = new_text        
    #显示减法        
    def showSubInfo(self,data1):
                 
        data1.label1['text'] = '-'  
        
        str1 = self.data1.entry1.get()
        str2 = self.data1.entry2.get()
       
        if self.is_alphabet(str1) or self.is_alphabet(str2):
            self.showErrorMessage()
            self.data1.entry1.delete(0,tk.END)
            self.data1.entry2.delete(0,tk.END)
            self.data1.label3['text']=""
            return        
        
        data1.num3 = float(str1) - float(str2)        
        
        new_text = '{}'.format(data1.num3)
        data1.label3['text'] = new_text 
    #弹出消息提示框    
    def showErrorMessage(self):
 #       win32api.MessageBox(0, "输入的数字中存在字符串", "错误(Error):",win32con.MB_OK) 
        tkinter.messagebox.showerror("错误","输入的数字中存在字符串")

    #判断字符串中是否存在非阿拉伯字符     
    def is_alphabet(self,uchar):
        for i in range(0,len(uchar)):
            if (uchar[i] >= u'\u0041' and uchar[i] <= u'\u005a') or (uchar[i] >= u'\u0061' and uchar[i] <= u'\u007a'):
                return True        
        return False
    
    #单选按钮事件
    def radioButton(self,data1):
        if self.var.get()==0: 
            self.showPlusInfo(self.data1)
        else:
            self.showSubInfo(self.data1) 
    #显示鼠标滑过后的事件      
    def showEvent(self,event):        
        self.data1.label4['bg']='black'
     #显示鼠标离开事件  
    def showLeaveEvent(self,event): 
        self.data1.label4['bg']='white'
    def showkey(self,event):
        self.data1.label4['text'] = str(event.keysym)
    #将标签4（label4重新聚焦，以接收和显示按键信息）
    def focuskey(self):
        self.data1.label4.focus_set()
#        self.data1.label4.config(te)
    def newWindow(self):
        newwin=tk.Toplevel(self.root)
        newwin.title('新窗口')
        newwin.geometry('400x400')
   
    def drawAxis(self):
        self.data1.canvas.create_line(0,120,320,120,fill="red",arrow=tk.LAST)
        self.data1.canvas.create_line(160,240,160,0,fill="red",arrow=tk.LAST)
        # 标题文字
        self.data1.canvas.create_text(self.data1.w0+50,10,text='y=sin(x)')
        # x轴刻度
        for i in range(-3,4):
            j=i*40
            self.data1.canvas.create_line(j+self.data1.w0,self.data1.h0,j+self.data1.w0,self.data1.h0-5,fill="red")
            self.data1.canvas.create_text(j+self.data1.w0,self.data1.h0+5,text=str(i))
            # y轴刻度
        for i in range(-2,3):
            j=i*40
            self.data1.canvas.create_line(self.data1.w0,j+self.data1.h0,self.data1.w0+5,j+self.data1.h0,fill="red")
            self.data1.canvas.create_text(self.data1.w0-10,j+self.data1.h0,text=str(-i))
        # 计算x
        def x(t):
            x=t*40  # x轴放大40倍
            x+=self.data1.w0   # 平移x轴
            return x
        # 计算y
        def y(t):
            y=math.sin(t)*40  # y轴放大40倍
            y-=self.data1.h0             # 平移y轴
            y=-y              # y轴值反向
            return y
        # 连续绘制微置线
        t=-math.pi
        while(t<math.pi):
            self.data1.canvas.create_line(x(t),y(t),x(t+0.01),y(t+0.01),fill="blue")
            t+=0.01
    #打开另存为的文件名称
    def saveas(self):
        saveasfilename = tk.filedialog.askopenfilename()
        if saveasfilename!='':
            return saveasfilename
        else:
            tk.messagebox.showerror("错误(error):","未选择另存为的文件")
if __name__=='__main__':
    app = main()
    # to do
    app.__init__()

