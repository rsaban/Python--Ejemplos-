#!/usr/bin/env python

import gtk
from ventana1 import ventan1

class main:
	
	def __init__(self):
		
		builder=gtk.Builder()
		builder.add_from_file("form1.glade")
		
		
		d={"on_btMostrar_clicked":self.btMostrarClick}
		builder.connect_signals(d)
		
	def btMostrarClick(self, widget):
		ventan1()
		
		
		
if __name__=="__main__":
	main()
	gtk.main()
