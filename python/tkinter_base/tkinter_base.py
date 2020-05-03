# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:37:04 2020

@author: jianhua.yang
"""

import tkinter as tk
from tkinter import *
import tkinter.messagebox

class data(object):
    def __init__(self):
        self.num1 = 1
        self.num2 = 2
        self.num3 = 0
        self.label1 = None
        self.label2 = None
        self.label3 = None
        self.label4 = None
        self.entry1 = None
        self.entry2 = None
        self.button1 = None
        self.button2 = None
        self.radiobutton1 = None
        self.radiobutton2 = None

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
        label4.bind('<Enter>',self.showEvent)
        label4.bind('<Leave>',self.showLeaveEvent)
        label4.focus_set()
        self.data1.label4 = label4
              
    def mainloop(self):
        self.root.mainloop()
        
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
#        
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
        
    def showErrorMessage(self):
 #       win32api.MessageBox(0, "输入的数字中存在字符串", "错误(Error):",win32con.MB_OK) 
        tkinter.messagebox.showerror("错误","输入的数字中存在字符串")

          
    def is_alphabet(self,uchar):
        for i in range(0,len(uchar)):
            if (uchar[i] >= u'\u0041' and uchar[i] <= u'\u005a') or (uchar[i] >= u'\u0061' and uchar[i] <= u'\u007a'):
                return True        
        return False
    
    
    def radioButton(self,data1):
        if self.var.get()==0: 
            self.showPlusInfo(self.data1)
        else:
            self.showSubInfo(self.data1) 
            
    def showEvent(self,event):        
        self.data1.label4['bg']='black'
        
    def showLeaveEvent(self,event): 
        self.data1.label4['bg']='white'
        
    def newWindow(self):
        newwin=tk.Toplevel(self.root)
        newwin.title('新窗口')
        newwin.geometry('400x400')
      
            
if __name__=='__main__':
    app = main()
    # to do
    app.__init__()

