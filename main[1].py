from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
root = Builder.load_string("""
<MainRobozzleBox>:
	orientation:"vertical"
	md_bg_color:[47/float(255), 79/float(255), 79/float(255), 1]
	MDBoxLayout:
		size_hint_y:None
		height:"100dp"
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"40dp"
			spacing:5
			padding:"10dp", "5dp"
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				md_bg_color:[0, 255/float(255), 0/float(255), 1]
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				md_bg_color:[255/float(255), 150/float(255), 0/float(255), 1]
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				md_bg_color:[0/float(255), 0/float(255), 255/float(255), 1]
			MDBoxLayout:
				size_hint:None, None
				size:"5dp", "10dp"
				md_bg_color:[47/float(255), 79/float(255), 79/float(255), 1]
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
				MDIcon:
					icon:"arrow-up-bold"
					pos_hint:{"center_x":.5, "center_y":.5}
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
				MDIcon:
					icon:"arrow-left-top-bold"
					pos_hint:{"center_x":.5, "center_y":.5}
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
				MDIcon:
					icon:"arrow-right-top-bold"
					pos_hint:{"center_x":.5, "center_y":.5}
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
				MDIcon:
					icon:"dots-vertical-circle-outline"
					pos_hint:{"center_x":.5, "center_y":.5}
			Widget:
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				md_bg_color:[47/float(255), 79/float(255), 79/float(255), 1]
				MDIcon:
					icon:"play"
					pos_hint:{"center_x":.5, "center_y":.5}
					theme_text_color:"Custom"
					text_color:[220/float(255), 220/float(255), 220/float(255), 1]
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				md_bg_color:[47/float(255), 79/float(255), 79/float(255), 1]
				MDIcon:
					icon:"step-forward"
					pos_hint:{"center_x":.5, "center_y":.5}
					theme_text_color:"Custom"
					text_color:[220/float(255), 220/float(255), 220/float(255), 1]
			Widget:
		MDBoxLayout:
			size_hint_y:None
			height:"40dp"
			padding:"5dp", "5dp"
			spacing:5
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				MDLabel:
					text:"F1"
					text_size:self.size
					halign:"center"
					valign:"middle"
					color:[220/float(255), 220/float(255), 220/float(255), 1]
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
			Widget:
			MDBoxLayout:
				size_hint:None, None
				size:"30dp", "30dp"
				md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
				MDIcon:
					icon:"dots-vertical-circle-outline"
					pos_hint:{"center_x":.5, "center_y":.5}
		Widget:
	MDBoxLayout:
		radius:[20, 20, 0, 0]
		md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
		orientation:"vertical"
		MDBoxLayout:
		MDBoxLayout:
			size_hint_y:None
			height:"60dp"
			padding:0, 0, 0, 10
			Widget:
			MDBoxLayout:
				md_bg_color:[0/float(255), 154/float(255), 255/float(255), 1]
				size_hint_x:None
				width:"250dp"
				radius:[40, 40, 40, 40]
				MDBoxLayout:
					spacing:20
					padding:"5dp", "5dp"
					Widget:
					MDBoxLayout:
						size_hint:None, None
						size:"40dp", "40dp"
						md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
						radius:[30, 30, 30, 30]
						MDLabel:
							text:"x1"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:[0, 0, 0, 1]
					MDBoxLayout:
						size_hint:None, None
						size:"40dp", "40dp"
						md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
						radius:[30, 30, 30, 30]
						MDLabel:
							text:"x2"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:[0, 0, 0, 1]
					MDBoxLayout:
						size_hint:None, None
						size:"40dp", "40dp"
						md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
						radius:[30, 30, 30, 30]
						MDLabel:
							text:"x2"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:[0, 0, 0, 1]
					Widget:
			MDIconButton:
				size_hint:None, None
				size:"50dp", "50dp"
				icon:"stop"
				pos_hint:{"center_y":.5}
			MDIconButton:
				size_hint:None, None
				size:"50dp", "50dp"
				icon:"close"
				pos_hint:{"center_y":.5}
			Widget:
		
""")
class MainRobozzleBox(MDBoxLayout):
	pass
class MainApp(MDApp):
	def build(self):
		root = MainRobozzleBox()
		return root
if __name__ == "__main__":
	MainApp().run()