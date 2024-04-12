from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from touch import TouchBox
from kivy.lang import Builder
root = Builder.load_string("""
<InstructionBox>: 
	size_hint:None, None
	size:"42dp", "42dp"
	md_bg_color:0/float(255), 0/float(255), 0/float(255), 1
	MDIconButton:
		id:instruction_sub_button
		icon:""
		size_hint:None, None
		size:"40dp", "40dp"
		icon_size:"20dp"
		pos_hint:{"center_x":.5, "center_y":.5}
		theme_text_color:"Custom"
		text_color:0/float(255), 0/float(255), 0/float(255), 1
<RobozzleScreen>:
	name:"robozzle"
	MDBoxLayout:
		md_bg_color:0, 0, 0, 1
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"150dp"
			MDBoxLayout:
				size_hint_x:None
				width:"40dp"
				orientation:"vertical"
				MDIconButton:
					size_hint:None, None
					size:"30dp", "30dp"
					icon:"arrow-left-top-bold"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
					pos_hint:{"center_x":.5, "center_y":.5}
				MDIconButton:
					size_hint:None, None
					size:"30dp", "30dp"
					icon:"keyboard-f1"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
					pos_hint:{"center_x":.5, "center_y":.5}
				MDIconButton:
					size_hint:None, None
					size:"30dp", "30dp"
					icon_size:"25dp"
					icon:"format-paint"
					theme_text_color:"Custom"
					text_color:0/float(255), 250/float(255), 154/float(255), 1
					pos_hint:{"center_x":.5, "center_y":.5}
			MDBoxLayout:
				size_hint_x:None
				width:"40dp"
				orientation:"vertical"
				MDIconButton:
					size_hint:None, None
					size:"30dp", "30dp"
					icon:"arrow-up-bold"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
					pos_hint:{"center_x":.5, "center_y":.5}
				MDIconButton:
					size_hint:None, None
					size:"30dp", "30dp"
					icon:"keyboard-f2"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
					pos_hint:{"center_x":.5, "center_y":.5}
				MDIconButton:
					size_hint:None, None
					size:"30dp", "30dp"
					icon_size:"25dp"
					icon:"format-paint"
					theme_text_color:"Custom"
					text_color:0/float(255), 0/float(255), 205/float(255), 1
					pos_hint:{"center_x":.5, "center_y":.5}
			MDBoxLayout:
				size_hint_x:None
				width:"40dp"
				orientation:"vertical"
				MDIconButton:
					size_hint:None, None
					size:"30dp", "30dp"
					icon:"arrow-right-top-bold"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
					pos_hint:{"center_x":.5, "center_y":.5}
				MDIconButton:
					size_hint:None, None
					size:"30dp", "30dp"
					icon:"keyboard-f3"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
					pos_hint:{"center_x":.5, "center_y":.5}
				MDIconButton:
					size_hint:None, None
					size:"30dp", "30dp"
					icon_size:"25dp"
					icon:"format-paint"
					theme_text_color:"Custom"
					text_color:255/float(255), 20/float(255), 147/float(255), 1
					pos_hint:{"center_x":.5, "center_y":.5}
			MDBoxLayout:
				orientation:"vertical"
				MDBoxLayout:
					size_hint_y:None
					height:"50dp"
					md_bg_color:0/float(255), 0/float(255), 0/float(255), 1
					spacing:4
					MDBoxLayout:
						size_hint:None, None
						size:"50dp", "50dp"
						orientation:"vertical"
						md_bg_color:0, 0, 1, 1
						Widget:
						MDIconButton:
							size_hint:None, None
							size:"50dp", "50dp"
							icon:"keyboard-f1"
							icon_size:"25dp"
							theme_text_color:"Custom"
							text_color:220/float(255), 220/float(255), 220/float(225), 1
							pos_hint:{"center_x":.5, "center_y":.5}
					MDBoxLayout:
						id:f1_instruction_list_space
						padding:"0dp", "4dp"
						spacing:2
						InstructionBox:
						InstructionBox:
						InstructionBox:	
						InstructionBox:
						InstructionBox:
				MDBoxLayout:
					size_hint_y:None
					height:"50dp"
					md_bg_color:0/float(255), 0/float(255), 0/float(255), 1
					spacing:4
					MDBoxLayout:
						size_hint:None, None
						size:"50dp", "50dp"
						orientation:"vertical"
						md_bg_color:0, 0, 0, 1
						Widget:
						MDIconButton:
							size_hint:None, None
							size:"50dp", "50dp"
							icon:"keyboard-f2"
							icon_size:"25dp"
							theme_text_color:"Custom"
							text_color:0/float(255), 0/float(255), 0/float(225), 1
							pos_hint:{"center_x":.5, "center_y":.5}
					MDBoxLayout:
						padding:"0dp", "4dp"
						spacing:2
						InstructionBox:
						InstructionBox:
						InstructionBox:	
						InstructionBox:
						InstructionBox:
				MDBoxLayout:
					size_hint_y:None
					height:"50dp"
					md_bg_color:0/float(255), 0/float(255), 0/float(255), 1
					spacing:4
					MDBoxLayout:
						size_hint:None, None
						size:"50dp", "50dp"
						orientation:"vertical"
						md_bg_color:0, 0, 0, 1
						Widget:
						MDIconButton:
							size_hint:None, None
							size:"50dp", "50dp"
							icon:"keyboard-f3"
							icon_size:"25dp"
							theme_text_color:"Custom"
							text_color:0/float(255), 0/float(255), 0/float(225), 1
							pos_hint:{"center_x":.5, "center_y":.5}
					MDBoxLayout:
						padding:"0dp", "4dp"
						spacing:2
						InstructionBox:
						InstructionBox:
						InstructionBox:	
						InstructionBox:
						InstructionBox:
		MDBoxLayout:
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
""")
class InstructionBox(TouchBox):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.white_color = 220/float(255), 220/float(255), 220/float(255), 1
	def respondToTouch(self):
		print("4894999:", self.md_bg_color)
		print("White: ", self.white_color)
		if self.md_bg_color == self.white_color:
			print("white white")
			self.md_bg_color = 0, 250/float(255), 0, 1
			if self.ids.instruction_sub_button == "":
				pass
class RobozzleScreen(MDScreen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.white_color = 220/float(255), 220/float(255), 220/float(255), 1
		self.ids.f1_instruction_list_space.children[-1].md_bg_color = self.white_color
		self.ids.f1_instruction_list_space.children[-1].ids.instruction_sub_button.text_color = self.white_color
		self.ids.f1_instruction_list_space.children[-2].md_bg_color = self.white_color
		self.ids.f1_instruction_list_space.children[-2].ids.instruction_sub_button.text_color = self.white_color
class TestApp(MDApp):
	def build(selff):
		root = RobozzleScreen()
		return root
if __name__ == "__main__":
	TestApp().run()