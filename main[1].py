from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from touch import TouchBox

x = Builder.load_string("""
<MainGameBox>:
	orientation:"vertical"
	id:main_game_box
	md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
	MDBoxLayout:
		size_hint_y:None
		height:"150dp"
		md_bg_color:[49/float(255), 79/float(255), 79/float(255), 1]
	MDBoxLayout:
	MDBoxLayout:
		size_hint_y:None
		height:"50dp"
		padding:"0dp", "5dp"
		spacing:2
		MDIconButton:
			icon:"play"
			size_hint:None, None
			size:"40dp", "40dp"
		MDIconButton:
			icon:"pause"
			size_hint:None, None
			size:"40dp", "40dp"
		MDIconButton:
			icon:"play-pause"
			size_hint:None, None
			size:"40dp", "40dp"
		MDIconButton:
			icon:"stop"
			size_hint:None, None
			size:"40dp", "40dp"
		MDIconButton:
			icon:"close"
			size_hint:None, None
			size:"40dp", "40dp"
		MDBoxLayout:
			padding:"5dp", "5dp"
			spacing:3
			Widget:
			SpeedOneBox:
				md_bg_color:[0, 0, 0, 1]
				size_hint:None, None
				size:"30dp", "30dp"
				padding:2
				MDBoxLayout:
					root:main_game_box
					id:speed_one_black_box
					md_bg_color:[0/float(255), 0/float(255), 0/float(255), 1]
					MDLabel:
						id:speed_one_label
						text:"1x"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:[1, 1, 1, 1]
			SpeedTwoBox:
			    md_bg_color:[0, 0, 0, 1]
				size_hint:None, None
				size:"30dp", "30dp"
				padding:2
				MDBoxLayout:
					root:main_game_box
					id:speed_two_black_box
					md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
					MDLabel:
						id:speed_two_label
						text:"2x"
						text_size:self.size
						halign:"center"
						valign:"middle"
			SpeedThreeBox:
		        md_bg_color:[0, 0, 0, 1]
			    size_hint:None, None
			    size:"30dp", "30dp"
			    padding:2
			    MDBoxLayout:
			    	root:main_game_box
			    	id:speed_three_black_box
					md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
					MDLabel:
						id:speed_three_label
						text:"3x"
						text_size:self.size
						halign:"center"
						valign:"middle"
""")
class SpeedOneBox(TouchBox):
	def respondToTouch(self):
		self.children[0].root.changeAllSpeedBoxToWhite()
		self.children[0].md_bg_color = [0, 0, 0, 1]
		self.children[0].children[0].color = [1, 1, 1, 1]
class SpeedTwoBox(TouchBox):
	def respondToTouch(self):
		self.children[0].root.changeAllSpeedBoxToWhite()
		self.children[0].md_bg_color = [0, 0, 0, 1]
		self.children[0].children[0].color = [1, 1, 1, 1]
class SpeedThreeBox(TouchBox):
	def respondToTouch(self):
		self.children[0].root.changeAllSpeedBoxToWhite()
		self.children[0].md_bg_color = [0, 0, 0, 1]
		self.children[0].children[0].color = [1, 1, 1, 1]
class MainGameBox(MDBoxLayout):
	def changeAllSpeedBoxToWhite(self):
		self.ids.speed_one_black_box.md_bg_color = [220/float(255), 220/float(255), 220/float(255), 1]
		self.ids.speed_one_label.color = [0, 0, 0, 1]
		self.ids.speed_two_black_box.md_bg_color = [220/float(255), 220/float(255), 220/float(255), 1]
		self.ids.speed_two_label.color = [0, 0, 0, 1]
		self.ids.speed_three_black_box.md_bg_color = [220/float(255), 220/float(255), 220/float(255), 1]
		self.ids.speed_three_label.color = [0, 0, 0, 1]
class RobbozleApp(MDApp):
	def build(self):
		root = MainGameBox()
		return root
if __name__ == "__main__":
	RobbozleApp().run()