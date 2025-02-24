from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.lang import Builder
from touch import TouchBox
root = Builder.load_string("""

<BlueColorButton>:
    size_hint:None, None
    size:"50dp", "50dp"
    md_bg_color:30/float(255), 144/float(255), 255/float(255), 1
<OrangeColorButton>:
    size_hint:None, None
    size:"50dp", "50dp"
    md_bg_color: 255/float(255), 165/float(255), 0/float(255), 1
<GreenColorButton>:
    size_hint:None, None
    size:"50dp", "50dp"
    md_bg_color:0/float(255), 255/float(255), 127/float(255), 1
<ControlsSpace>:
    id:control_space
    size_hint:None, None
    size:"120dp", "206dp"
    MDBoxLayout:
        size_hint_x:None
        width:"50dp"
        orientation:"vertical"
        space:2
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            icon:"arrow-up-thin"
        MDIOconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            icon:"arrow-left-thin"
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50d0p"
            icon:"arrow-right-thin"
        MDBoxLayout:
            md_bg_color:120/float(255), 120/float(255), 120/float(255), 1
            size_hint:None, None
            size:"50dp", "50dp"
            MDLabel:
                text:"F1"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:0, 0, 0, 1
                bold:True
    MDBoxLayout:
        size_hint_x:None
        width:"20dp"
    MDBoxLayout:
        space:2
        Widget:
        BlueColorButton:
            root:control_space
        OrangeColorButton:
            root:control_space
        GreenColorButton:
            root:control_space
        Widget:
<ExecutionCommands>:
    size_hint_y:None
    width:"258dp"
    spacing:2
    MDIconButton:
        size_hint:None, None
        size:"50dp", "50dp"
        icon:"play"
    MDIconButton:
        size_hint:None, None
        size:"50dp", "50dp"
        icon:"play-pause"
    MDIconButton:
        size_hint:None, None
        size:"50dp", "50dp"
        icon:"stop"
    MDIconButton;
        size_hint:None, None
        size:"50dp", "50dp"
        icon:"window-close"
<SpeedButtonBox>:
    id:speed_button_box
    size_hint:None, None
    size:"50dp", "50dp"
    MDLabel:
        id:speed_number
        text:"x1"
        text_size:self.size
        halign:"center"
        valign:"middle"
        color:1, 1, 1, 1
<GameSpeed>:
    id:game_speed_box
    size_hint:None, None
    size:"70dp", "160dp"
    orientation:"vertical"
    MDBoxLatyout:
        size_hint_y:None
        height:"20dp"
        MDLabel:
            text:"Game Speed"
            text_size:self.size
            halign:"left"
            valign:"middle"
            color:0, 0, 0, 1
    MDBoxLayout:
        SpeedButtonBox:
            root:game_speed_box
        SpeedButtonBox:
            root:game_speed_box
            self.ids.speed_number.text = "x2"
        SpeedButtonBox:
            root:game_speed_box
            self.ids.speed_number.text = "x3"
<Block>:
    size_hint:None, None
    size:"50dp", "50dp"
    md_bg_color: 90/float(255), 90/float(255), 90/float(255), 1
<BlocksSpace>:
    size_hint:None, None
    size:"800dp", "800dp"
    BlocksGrid:
<MainGameSpace>:
    md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
    orientation:"vertical"
    MDBoxLayout:
        size_hint_y:None
        hieght:"800dp"
        BlocksSpace:
        MDBoxLayout:
    MDBoxLayout:
        GameSpeed:
        MDBoxLayout:
            size_hint_x:None
            width:"200dp"
        ExecutionCommands:
        Widget:
""")
class BlueColorButton(TouchBox):
    def respondToTouch(self):
        pass
class OrangeColorButton(TouchBox):
    def respondToTouch(self):
        pass
class GreenColorButton(TouchBox):
    def respondToTouch(self):
        pass
class ExecutionCommands(MDBoxLayout):
    pass
class SpeedButtonBox(TouchBox):
    def respondToTouch(self):
        pass
class GameSpeed(MDBoxLayout):
    pass
class Block(MDBoxLayout):
    pass
class BlocksSpace(MDBoxLayout):
    pass
class BlocksGrid(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 8
        self.rows = 8
        for i range(50):
            block = Block()
            self.add_widget(block)
class MainGameSpace(MDBoxLayout):
    pass
class RobozzleApp(MDApp):
    def build(self):
        root = MainGameSpace()
        return root
if __name__ == "__main__":
    RobozzleApp().run()
