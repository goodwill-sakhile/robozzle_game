from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
<Block>:
 	size_hint:None, None
 	size:"24dp", "24dp"
 	color:[220/float(255), 220/float(255, 220/float255, 1]
 <GridBlocks>:
 	size_hint:None, None
 	size:"384dp", "384dp"
 	rows:16
 	cols:16
 	spacing:1
<SetBlocksScreen>:
	name:"set_blocks_screen"
	MDBoxLayout:
		color:[0, 0, 0, 1]
		orientation:"vertical"
		MDBoxLayout:
			radius:[30, 30, 0, 0]
			MDBoxLayout:
			GridBlocks:
			MDBoxLayout:
		MDBoxLayout:
			size_hint_y:None
			height:"100dp"
			
<SetArrowScreen>:
	name:"set_arrow_screen"
	MDBoxLayout:
		color:[0,  0, 0, 1]
		orientation:"vertical"
		MDBoxLayout:
			radius:[30, 30, 0, 0]
			MDBoxLayout:
			GridBlocks:
			MDBoxLayout:
		MDBoxLayout:
			size_hint_y:None
			height:"100dp"
<SetTreatyScreen>:
	name:"set_treaty_screen"
	MDBoxLayout:
		color:[0, 0, 0, 1]
		orientation:"vertical"
		MDBoxLayout:
			radius:[30, 30, 0, 0]
			MDBoxLayout:
			GridBlocks:
			MDBoxLayout:
		MDBoxLayout:
			size_hint_y:None
			height:"100dp"
""")
class Block(MDBoxLayout):
	pass
class GridLayout(MDGridLayout):
	def __init__(self, **kwargs):
		super().__init __(**kwargs)
		self.addBlocks()
	def addBlocks(self):
		for i in range(256):
			block = Block()
			self.add_widget(block)