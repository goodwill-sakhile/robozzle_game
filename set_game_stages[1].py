from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from touch import TouchBox
from kivy.lang import Builder 
root  = Builder.load_string("""
<Block>:
	size_hint:None, None
	size:"21dp", "21dp"
	md_bg_color:[1, 1, 1, 1]
<SetGameSpaceBox>:
	id:set_game_space_box
	orientation:"vertical"
	md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
	MDBoxLayout:
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"50dp"
			padding:5
			spacing:5
			Widget:
			GreenBox:
				root:set_game_space_box
				id:green_box
				size_hint:None, None
				size:"40dp", "40dp"
				md_bg_color:[0, 0, 0, 1]
				padding:2
				MDBoxLayout:
					md_bg_color:[0/float(255), 255/float(255), 154/float(255), 1]
			BlueBox:
				root:set_game_space_box
				id:blue_box
				size_hint:None, None
				size:"40dp", "40dp"
				padding:2
				md_bg_color:[0, 154/float(255), 255/float(255), 1]
				MDBoxLayout:
					md_bg_color:[0, 154/float(255), 255/float(255), 1]	
			OrangeBox:
				root:set_game_space_box
				id:orange_box
				size_hint:None, None
				size:"40dp", "40dp"
				padding:2
				md_bg_color:[255/float(255), 140/float(255), 0, 1]
				MDBoxLayout:
					md_bg_color:[255/float(255), 140/float(255), 0, 1]
			Widget:	
	MDBoxLayout:
		size_hint:None, None
		size:"368dp", "368dp"
		padding:2
		BlocksLayout:
			root:set_game_space_box
			size_hint:None, None
			size:"366dp", "366dp"
	MDBoxLayout:
		size_hint_y:None
		height:"50dp"
		padding:5
		MoveToNextScreen:
			radius:[30, 30, 30, 30]
			md_bg_color:[0, 154/float(255), 255/float(255), 1]
			MDLabel:
				text:"Next"
				text_size:self.size
				halign:"center"
				valign:"middle"
				color:[1, 1, 1, 1]
				bold:True
<BlockSelectScreen>:
	name:"block_select_screen"
	SetGameSpaceBox:
<MainScreenManager>:
	BlockSelectScreen:
""")
class Block(TouchBox):
	def respondToTouch(self):
		if self.md_bg_color == [1, 1, 1, 1]:
			self.parent.root.selected_blocks[self] = self.parent.children.index(self)
			self.md_bg_color = self.parent.root.color
		else:
			self.md_bg_color = [1, 1, 1, 1]
			self.parent.root.selected_blocks.pop(self)
class GreenBox(TouchBox):
	def respondToTouch(self):
		self.root.removeBlackBackgroundFromBlock()
		self.md_bg_color = [0, 0, 0, 1]
		self.root.color = [0/float(255), 255/float(255), 154/float(255), 1]
class BlueBox(TouchBox):
	def respondToTouch(self):
		self.root.removeBlackBackgroundFromBlock()
		self.md_bg_color = [0, 0, 0, 1]
		self.root.color = [0, 154/float(255), 255/float(255), 1]
class OrangeBox(TouchBox):
	def respondToTouch(self):
		self.root.removeBlackBackgroundFromBlock()
		self.md_bg_color = [0, 0, 0, 1]
		self.root.color = [255/float(255), 140/float(255), 0, 1]
class BlocksLayout(MDGridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 16
		self.rows = 16
		self.spacing = 2
		for i in range(256):
			block = Block()
			self.add_widget(block)
class MoveToNextScreen(TouchBox):
	def respondToTouch(self):
		pass
class SetGameSpaceBox(MDBoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.selected_blocks = {}
		self.color = [0/float(255), 255/float(255), 154/float(255), 1]
	def removeBlackBackgroundFromBlock(self):
		self.ids.green_box.md_bg_color = [0/float(255), 255/float(255), 154/float(255), 1]
		self.ids.blue_box.md_bg_color  = [0, 154/float(255), 255/float(255), 1]
		self.ids.orange_box.md_bg_color = [255/float(255), 140/float(255), 0, 1]
class BlockSelectScreen(MDScreen):
	pass
class MainScreenManager(ScreenManager):
	pass
class BlockSetterApp(MDApp):
	def build(self):
		root = MainScreenManager()
		return root
if __name__ == "__main__":
	BlockSetterApp().run()