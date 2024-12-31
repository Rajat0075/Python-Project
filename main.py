from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kv import kv_code
from design import design
from kivy.lang import Builder

class Myapp(MDApp):
	data = {
	       'new file': 'file',
	       'upload File': 'upload'
	}
	def build(self):
		screen = Screen()
		builder=Builder.load_string(kv_code)
		#builder=Builder.load_string(design)
		
		screen.add_widget(builder)
		return screen
		
Myapp().run()
