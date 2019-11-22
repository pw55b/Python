# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import socket 
import Server
import threading
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 (wx.Frame):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500, 500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer1 = wx.BoxSizer(wx.VERTICAL)

		self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400,-1),0)
		bSizer1.Add(self.m_textCtrl1,0,wx.ALL, 5)

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,200 ), wx.TE_MULTILINE )
		bSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button2, 0, wx.ALL, 5 )


		self.SetSizer(bSizer1)
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner(self, wx.ID_ANY)

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_button2.Bind(wx.EVT_BUTTON, self.m_button2OnButtonClick)
		self.Bind(wx.EVT_TIMER, self.m_timer1OnTimer, id=wx.ID_ANY)

	def __del__(self):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button2OnButtonClick(self, event):
		Server.Server.sendata=win.m_textCtrl1.Value
		Server.Server.event.set()
		event.Skip()

	def m_timer1OnTimer(self, event):
		event.Skip()
	# Virtual event handlers, overide them in your derived class
	def MyFrame1OnShow( self, event ):
		event.Skip()



app = wx.App()
win = MyFrame1(None)
win.Show()
t=threading.Thread(target=Server.main).start()
app.MainLoop()
