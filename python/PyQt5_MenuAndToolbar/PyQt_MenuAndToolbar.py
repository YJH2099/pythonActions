'''
用PyQt5实现菜单和工具条的制作
其中，工具条可以位图与文本同时显示
显示状态栏（包括标签，实时显示时间）

'''
'''
调用的类库
'''
import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtCore import Qt
import time,datetime

'''
创建主窗口
'''

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.num = 0
        self.InitGUI()
        self.AddMenu()
        self.AddToolbar()
        self.show()
    '''初始化界面'''
    def InitGUI(self):
        self.resize(800, 600)
        self.setWindowTitle('菜单和工具条')
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))

        '''设置标签,lable0用于实时显示时间'''
        self.label0 = QtWidgets.QLabel(self)
        timer = QtCore.QTimer(self.label0)
        timer.timeout.connect(self.showtime)
        timer.start()
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('这是一个测试菜单和工具条的程序')
        '''设置状态栏'''
        self.statusBar().addPermanentWidget(self.label1)
        self.statusBar().addPermanentWidget(self.label0)

        '''设置按钮'''
        self.button = QtWidgets.QPushButton(self)
        self.button.setText('点击')
        self.button.setGeometry(QtCore.QRect(100,20,100,120))
        self.button.move(200,300)
        '''单击查看状态栏中的变化'''
        self.button.clicked.connect(self.ModifyStatusBar)

    '''添加菜单函数'''
    def AddMenu(self):
        '''
        设置菜单的动作
        '''
        self.Action1 = QtWidgets.QAction(QtGui.QIcon('favicon.ico'),'新建',self)#可以添加图标

        self.Action1.setShortcut('Ctrl+N')
        self.Action2 = QtWidgets.QAction('打开',self)
        self.Action3 = QtWidgets.QAction('保存',self)
        self.Action4 = QtWidgets.QAction('退出',self)
        self.Action4.setShortcut('Ctrl+Q')
        self.Action4.triggered.connect(quit)
        self.Action5 = QtWidgets.QAction('撤回',self)


        '''添加菜单'''
        self.Menubar1 = self.menuBar()      #因为是MainWindow,所以采用self.menuBar(),如果用QtWidgets.MenuBar(self),则会出现位置不对的情况
        '''添加第一组菜单'''
        self.menu1 = self.Menubar1.addMenu('文件')
        self.menu1.addAction(self.Action1)
        self.menu1.addAction(self.Action2)
        self.menu1.addAction(self.Action3)
        self.menu1.addAction(self.Action4)
        '''添加第二组菜单'''
        self.menu2 = self.Menubar1.addMenu('编辑')

    '''添加工具条函数'''
    def AddToolbar(self):
        '''创建工具条的动作'''
        self.ToolActions1 = QtWidgets.QAction(QtGui.QIcon('favicon.ico'),'新建',self)
        self.ToolActions1.setToolTip('新建')
        self.ToolActions1.setIconText('新建')

        self.ToolActions2 = QtWidgets.QAction('打开',self)

        '''添加工具条'''
        self.toobar1 = self.addToolBar('打开')
        '''为工具条添加动作'''
        self.toobar1.addAction(self.ToolActions1)
        # toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon) # 文字图片垂直排列
        self.toobar1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)#文件图片并排排列
        self.toobar1.addAction(self.ToolActions2)
    def ModifyStatusBar(self):
        self.num += 1
        self.timestr = datetime.datetime.now()
        self.label1.setText('这是第 %d' % (self.num) + ' 次点击'+'        '+str(self.timestr))
    def showtime(self):
        self.label0.setText("     " + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = MyMainWindow()
    GUI.show()
    sys.exit(app.exec_())

