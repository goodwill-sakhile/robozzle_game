from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
root = Builder.load_string("""
<TopBarBoxWithNextPreviousButton>:
    size_hint_y:None
    height:"100dp"
    md_bg_color:[0, 0, 0, 1]
    MDBoxLayout:
        size_hint_x:None
        width:"70dp"
        orientation:"vertical"
        padding:"10dp", "0dp"
        Widget:
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            icon:"skip-previous"
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
            icon_size:"40dp"
        Widget
    MDBoxLayout:
    MDBoxLayout:
        size_hint_x:None
        width:"70dp"
        orientation:"vertical"
        padding:"10dp", "0dp"
        Widget:
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            icon:"skip-next"
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
            icon_size:"40dp"
        Widget
<TopBarBoxWithNextButton>:
    size_hint_y:None
    height:"100dp"
    md_bg_color:[0, 0, 0, 1]
    MDBoxLayout:
    MDBoxLayout:
        size_hint_x:None
        width:"70dp"
        orientation:"vertical"
        padding:"10dp", "0dp"
        Widget:
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            icon:"skip-next"
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
            icon_size:"40dp"
        Widget:
<ThreeColorRoundBox>
    size_hint_y:None
    height:"70dp"
    padding:"0dp", "10dp"
    Widget:
    MDBoxLayout:
        size_hint_x:None
        width:"350dp"
        radius:[40, 40, 40, 40]
        md_bg_color:[0, 0, 0, 1]
        spacing:10
        padding:"0dp", "5dp"
        Widget:
        MDBoxLayout:
            size_hint:None, None
            size:"40dp", "40dp"
            radius:[40, 40, 40, 40]
            md_bg_color:[0/float(255), 255/float(255), 154/float(255), 1]
        MDBoxLayout:
            size_hint:None, None
            size:"40dp", "40dp"
            radius:[40, 40, 40, 40]
            md_bg_color:[0/float(255), 154/float(255), 255/float(255), 1]
        MDBoxLayout:
            size_hint:None, None
            size:"40dp", "40dp"
            radius:[40, 40, 40, 40]
            md_bg_color:[255/float(255), 154/float(255), 0/float(255), 1]
        Widget:
    Widget:
<ThreeArrowFaceDirection>
    size_hint_y:None
    height:"80dp"
    padding:"0dp", "10dp"
    Widget:
    MDBoxLayout:
        size_hint_x:None
        width:"350dp"
        radius:[50, 50, 50, 50]
        md_bg_color:[0, 0, 0, 1]
        spacing:10
        padding:"10dp", "7dp"
        MDIconButton:
            size_hint:None, None
            size:"40dp", "40dp"
            icon:"arrow-right-bold"
            radius:[40, 40, 40, 40]
            md_bg_color:[0/float(255), 255/float(255), 154/float(255), 1]
        Widget:
        MDIconButton:
            size_hint:None, None
            size:"40dp", "40dp"
            icon_size:"25dp"
            icon:"arrow-down-right"
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
        MDIconButton:
            size_hint:None, None
            size:"40dp", "40dp"
            icon_size:"25dp"
            icon:"arrow-up-left"
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
        Widget:
    Widget:
""")
class TopBarBoxWithNextPreviousButton(MDBoxLayout):
    pass
class TopBarBoxWithNextButton(MDBoxLayout):
    pass
class ThreeColorRoundBox(MDBoxLayout):
    pass
class ThreeArrowFaceDirection(MDBoxLayout):
    pass
class TestApp(MDApp):
    def build(self):
        root = ThreeArrowFaceDirection()
        return root
if __name__ == "__main__":
    TestApp().run()