from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
root = Builder.load_string("""
<MainRobbozleBox>:
    orientation:"vertical"
    md_bg_color:[0, 0, 0, 1]
    MDBoxLayout:
        size_hint_y:None
        height:"200dp"
    MDBoxLayout:
        md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
    MDBoxLayout:
        md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
        size_hint_y:None
        height:"60dp"
        padding:5
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            icon:"play"
            icon_size:"30dp"
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            icon:"play-pause"
            icon_size:"30dp"
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            icon:"stop"
            icon_size:"30dp"
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            icon:"close"
            icon_size:"30dp"
""")
class MainRobbozleBox(MDBoxLayout):
    pass
class RobbozleApp(MDApp):
    def build(self):
        root = MainRobbozleBox()
        return root
if __name__ == "__main__":
    RobbozleApp().run()