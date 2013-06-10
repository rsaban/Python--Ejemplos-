#!/usr/bin/env python
import gtk

class ventan1:
	
	def __init__(self):
		
		builder = gtk.Builder()
		builder.add_from_file("ventana1.glade")
		self.label1 = builder.get_object("label1")
		
		c={"on_btDale_clicked":self.btDaleClick}
		builder.connect_signals(c)
	
	
	def btDaleClick(self, widget):
		self.label1.set_text("He cambiado")
		
		
#if __name__=="__ventan1__":
	#ventan1()
	#gtk.ventan1()	
