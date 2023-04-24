from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from touch import TouchBox
import pickle
from kivy.lang import Builder
ui = Builder.load_string("""
<Block>:
    size_hint:None, None
    size:"30dp", "30dp"
    md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
    Widget:
    MDIcon:
        id:icon_space
        size_hint:None, None
        size:"25dp", "25dp"
        icon:"stop"
        theme_text_color:"Custom"
        pos_hint:{"center_x":.5, "center_y":.5}
        md_bg_color:[160/float(255), 160/float(255), 160/float(255), 1]
        text_color:[160/float(255), 160/float(255), 160/float(255), 1]
    Widget:
<BlocksGrid>:
    spacing:5
    rows:10
    cols:10
    size_hint:None, None
    size:"330dp", "330dp"
<ColoredBox>:
    size_hint:None, None
    size:"30dp", "30dp"
<DirectionHolderBlock>:
    size_hint:None, None
    size:"25dp", "25dp"
    pos_hint:{"center_y":.5}
    MDIcon:
        size_hint:None, None
        size:"25dp", "25dp"
        icon:"stop"
        md_bg_color:[160/float(255), 160/float(255), 160/float(255), 1]
        theme_text_color:"Custom"
        text_color:[160/float(255), 160/float(255), 160/float(255), 1]
        pos_hint:{"center_y":.5}
<ControlsAdditionScreen>:
    name:"controls_addition_screen"
    id:controls_addition_screen
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:"10dp", "5dp"
            BackToStageSetter:
                root:controls_addition_screen
                size_hint:None, None
                size:"100dp", "40dp"
                radius:[30, 30, 30, 30]
                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                MDLabel:
                    text:"Back"
                    size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                icon:"chevron-left"
                theme_text_color:"Custom"
                user_font_size:"30dp"
                text_color:[0, 0, 0, 1]
                pos_hint:{"center_y":.5}
                on_press:root.subtractStageNumber()
            MDBoxLayout:
                size_hint:None, None
                size:"50dp", "50dp"
                MDLabel:
                    id:stage_number
                    text:"1"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[0, 0, 0, 1]
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                icon:"chevron-right"
                user_font_size:"30dp"
                theme_text_color:"Custom"
                text_color:[0, 0, 0, 1]
                pos_hint:{"center_y":.5}
                on_press:root.addStageNumber()
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:0, 5, 10, 5
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"keyboard-f1"
                user_font_size:"20dp"
                pos_hint:{"center_y":.5}
            MDBoxLayout:
                spacing:2
                id:f_one_blocks_space
                DirectionHolderBlock:
                DirectionHolderBlock:
            Widget:
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"minus"
                pos_hint:{"center_y":.5}
                on_press:root.removeFOneBlock()
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"plus"
                pos_hint:{"center_y":.5}
                on_press:root.addFOneBlock()
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:0, 5, 10, 5
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"keyboard-f2"
                user_font_size:"20dp"
                pos_hint:{"center_y":.5}
            MDBoxLayout:
                spacing:2
                id:f_two_blocks_space
            Widget:
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"minus"
                pos_hint:{"center_y":.5}
                on_press:root.removeFTwoBlock()
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"plus"
                pos_hint:{"center_y":.5}
                on_press:root.addFTwoBlock()
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:0, 5, 10, 5
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"keyboard-f3"
                user_font_size:"20dp"
                pos_hint:{"center_y":.5}
            MDBoxLayout:
                spacing:2
                id:f_three_blocks_space
            Widget:
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"minus"
                pos_hint:{"center_y":.5}
                on_press:root.removeFThreeBlock()
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"plus"
                pos_hint:{"center_y":.5}
                on_press:root.addFThreeBlock()
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:"10dp", "5dp"
            AddGreenBrush:
                root:controls_addition_screen
                size_hint:None, None
                size:"200dp", "40dp"
                radius:[30, 30, 30, 30]
                md_bg_color:[190/float(255), 190/float(255), 190/float(255), 1]
                MDIconButton:
                    size_hint:None, None
                    size:"40dp", "40dp"
                    user_font_size:"20dp"
                    icon:"brush"
                    theme_text_color:"Custom"
                    text_color:[0, 255/float(255), 154/float(255), 1]
                    pos_hint:{"center_y":.5}
                MDBoxLayout:
                    MDLabel:
                        id:green_label
                        text:"Green brush"
                        size:self.size
                        halign:"left"
                        valign:"middle"
                        color:[0, 0, 0, 1]
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:"10dp", "5dp"
            AddBlueBrush:
                root:controls_addition_screen
                size_hint:None, None
                size:"200dp", "40dp"
                radius:[30, 30, 30, 30]
                md_bg_color:[190/float(255), 190/float(255), 190/float(255), 1]
                MDIconButton:
                    size_hint:None, None
                    size:"40dp", "40dp"
                    user_font_size:"20dp"
                    icon:"brush"
                    theme_text_color:"Custom"
                    text_color:[0/float(255), 154/float(255), 255/float(255), 1]
                    pos_hint:{"center_y":.5}
                MDBoxLayout:
                    MDLabel:
                        id:blue_label
                        text:"Blue brush"
                        size:self.size
                        halign:"left"
                        valign:"middle"
                        color:[0, 0, 0, 1]
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:"10dp", "5dp"
            AddOrangeBrush:
                root:controls_addition_screen
                size_hint:None, None
                size:"200dp", "40dp"
                radius:[30, 30, 30, 30]
                md_bg_color:[190/float(255), 190/float(255), 190/float(255), 1]
                MDIconButton:
                    size_hint:None, None
                    size:"40dp", "40dp"
                    user_font_size:"20dp"
                    icon:"brush"
                    theme_text_color:"Custom"
                    text_color:[255/float(255), 154/float(255), 0/float(255), 1]
                    pos_hint:{"center_y":.5}
                MDBoxLayout:
                    MDLabel:
                        id:orange_label
                        text:"Orange brush"
                        size:self.size
                        halign:"left"
                        valign:"middle"
                        color:[0, 0, 0, 1]
        MDBoxLayout:
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:5
            FinishButtonBox:
                root:controls_addition_screen
                radius:[40, 40, 40, 40]
                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                MDLabel:
                    text:"Finish"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    bold:True
                    color:[1, 1, 1, 1]
<StageSetterScreen>:
    name:"stage_block_screen"
    id:stage_setter_screen
    MDBoxLayout:
        md_bg_color:[0, 0, 0, 1]
        orientation:"vertical"
        MDBoxLayout:
            size_hint_y:None
            height:"185dp"
            orientation:"vertical"
            padding:"0dp", "5dp"
            spacing:5
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                padding:10
                spacing:10
                root:stage_setter_screen
                Widget:
                ColoredBox:
                    md_bg_color:[0, 255/float(255), 154/float(255), 1]
                ColoredBox:
                    md_bg_color:[0, 154/float(255), 255/float(255), 1]
                ColoredBox:
                    md_bg_color:[255/float(255), 154/float(255), 0/float(255), 1]
                EraseBlockButton:
                    id:erase_block
                    size_hint_y:None
                    height:"30dp"
                    radius:[20, 20, 20, 20]
                    size_hint_x:None
                    width:"120dp"
                    md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
                    MDLabel:
                        text:"Erase block"
                        text_size:self.size
                        halign:"center"
                        valign:"middle"
                        bold:True
                        color:[0, 0, 0, 1]
                Widget:
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                spacing:10
                Widget:
                MDIconButton:
                    icon:"corn"
                    size_hint:None, None
                    size:"50dp", "50dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    user_font_size:"20dp"
                    on_press:root.chooseFood(self)
                MDIconButton:
                    icon:"fruit-pineapple"
                    size_hint:None, None
                    size:"50dp", "50dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    user_font_size:"20dp"
                    on_press:root.chooseFood(self)
                MDIconButton:
                    icon:"fruit-grapes-outline"
                    size_hint:None, None
                    size:"50dp", "50dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    user_font_size:"20dp"
                    on_press:root.chooseFood(self)
                MDIconButton:
                    icon:"fruit-watermelon"
                    size_hint:None, None
                    size:"50dp", "50dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    user_font_size:"20dp"
                    on_press:root.chooseFood(self)
                MDIconButton:
                    icon:"fruit-cherries"
                    size_hint:None, None
                    size:"50dp", "50dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    user_font_size:"20dp"
                    on_press:root.chooseFood(self)
                MDIconButton:
                    icon:"virus"
                    size_hint:None, None
                    size:"50dp", "50dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    user_font_size:"20dp"
                    on_press:root.chooseFood(self)
                Widget:
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                spacing:5
                Widget:
                MDIconButton:
                    icon:"chevron-triple-right"
                    size_hint:None, None
                    size:"50dp", "50dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    user_font_size:"20dp"
                    on_press:root.chooseWalker(self)
                MDIconButton:
                    icon:"chevron-triple-up"
                    size_hint:None, None
                    size:"50dp", "50dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    user_font_size:"20dp"
                    on_press:root.chooseWalker(self)
                MDIconButton:
                    icon:"chevron-triple-down"
                    size_hint:None, None
                    size:"50dp", "50dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    user_font_size:"20dp"
                    on_press:root.chooseWalker(self)
                MDIconButton:
                    icon:"chevron-triple-left"
                    size_hint:None, None
                    size:"50dp", "50dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    user_font_size:"20dp"
                    on_press:root.chooseWalker(self)
                Widget:
        MDBoxLayout:
            orientation:"vertical"
            FloatLayout:
                pos:self.parent.pos
                size:self.parent.size
                MDBoxLayout:
                    pos:self.parent.pos
                    orientation:"vertical"
                    padding:"5dp", "0dp"
                    MDBoxLayout:
                        orientation:"vertical"
                        md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
                        radius:[20, 20, 20, 20]
                        Widget:
                        MDBoxLayout:
                            size_hint_y:None
                            height:"330dp"
                            Widget:
                            BlocksGrid:
                                root:stage_setter_screen
                            Widget:
                        Widget:
                    MDBoxLayout:
                        size_hint_y:None
                        height:"50dp"
                        padding:"0dp", "5dp"
                        NextButton:
                            id:next_button_box
                            root:stage_setter_screen
                            radius:[30, 30, 30, 30]
                            md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
                            MDLabel:
                                text:"Next"
                                bold:True
                                text_size:self.size
                                halign:"center"
                                valign:"middle"
                                color:[0, 0, 0, 1]
<MainScreenManager>:
    StageSetterScreen:
        id:stage_setter_screen
    ControlsAdditionScreen:
        id:controls_screen
""")
class Block(TouchBox):
    def respondToTouch(self):
        stage_setter_screen = self.parent.root
        if stage_setter_screen.current_block:
            stage_setter_screen.current_block.md_bg_color = [220/float(255), 220/float(255), 220/float(255), 1]
        stage_setter_screen.current_block = self
        stage_setter_screen.current_block.md_bg_color = [0, 0, 0, 1]
        if stage_setter_screen.current_block.ids.icon_space.text_color != [160/float(255), 160/float(255), 160/float(255), 1]:
            stage_setter_screen.ids.erase_block.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
            stage_setter_screen.ids.erase_block.children[0].color = [1, 1, 1, 1]
        else:
            stage_setter_screen.ids.erase_block.md_bg_color = [220/float(255), 220/float(255), 220/float(255), 1]
            stage_setter_screen.ids.erase_block.children[0].color = [0, 0, 0, 1]
class BlocksGrid(MDGridLayout):
    #make block grid
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            block = Block()
            self.add_widget(block)
class ColoredBox(TouchBox):
    #responsive color box button
    def checkIfTableComplete(self):
        if len(self.parent.root.path_table) >= 2:
            next = False
            for key in self.parent.root.path_table:
                try:
                    if self.parent.root.path_table[key]["walker"] and self.parent.root.path_table[key]["color"]:
                        next = True
                except:
                    pass
            if next:
                self.parent.root.ids.next_button_box.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
                self.parent.root.ids.next_button_box.children[0].color = [1, 1, 1, 1]
    def addColordBlockOnTable(self, color):
        stage_setter_screen = self.parent.root
        current_block = stage_setter_screen.current_block
        try:
            sub_table = stage_setter_screen.path_table[str(current_block.parent.children.index(current_block))]
            sub_table["color"] = str(color)
            stage_setter_screen.path_table[str(current_block.parent.children.index(current_block))] = sub_table
        except:
            stage_setter_screen.path_table[str(current_block.parent.children.index(current_block))] = {"color":str(self.md_bg_color)}
        self.checkIfTableComplete()
    def respondToTouch(self):
        stage_setter_screen = self.parent.root
        current_block = stage_setter_screen.current_block
        current_block.md_bg_color = self.md_bg_color
        current_block.ids.icon_space.md_bg_color = self.md_bg_color
        stage_setter_screen.ids.erase_block.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
        stage_setter_screen.ids.erase_block.children[0].color = [1, 1, 1, 1]
        self.addColordBlockOnTable(self.md_bg_color)
        if stage_setter_screen.current_block.ids.icon_space.icon == "stop":
            current_block.ids.icon_space.text_color = self.md_bg_color
        else:
            current_block.ids.icon_space.text_color = [1, 1, 1, 1]
class DirectionHolderBlock(MDBoxLayout):
    pass
class EraseBlockButton(TouchBox):
    def eraseBlockOnTable(self, index):
        no_walker = False
        try:
            self.parent.root.path_table[str(index)]["walker"]
            no_walker = True
        except:
            pass
        print("Before Erase :", self.parent.root.path_table)
        self.parent.root.path_table.pop(str(index))
        print(self.parent.root.path_table.keys())
        print("After Erase :", self.parent.root.path_table)
        if (len(self.parent.root.path_table) < 2) or no_walker:
            self.parent.root.ids.next_button_box.md_bg_color = [220/float(255), 220/float(255), 220/float(255), 1]
            self.parent.root.ids.next_button_box.children[0].color = [0, 0, 0, 1]
    def respondToTouch(self):
        current_block = self.parent.root.current_block
        self.eraseBlockOnTable(current_block.parent.children.index(current_block))
        if current_block:
            current_block.md_bg_color = [0, 0, 0, 1]
            current_block.ids.icon_space.text_color = [160/float(255), 160/float(255), 160/float(255), 1]
            current_block.ids.icon_space.md_bg_color = [160/float(255), 160/float(255), 160/float(255), 1]
            current_block.ids.icon_space.icon = "stop"
        self.md_bg_color = [220/float(255), 220/float(255), 220/float(255), 1]
        self.children[0].color = [0, 0, 0, 1]
class BackToStageSetter(TouchBox):
    def respondToTouch(self):
        self.root.parent.transition = SlideTransition(direction = "right")
        self.root.parent.current = "stage_block_screen"
class AddGreenBrush(TouchBox):
    def respondToTouch(self):
        if self.md_bg_color != [0, 0, 0, 1]:
            self.md_bg_color  = [0, 0, 0, 1]
            self.root.ids.green_label.color = [1, 1, 1, 1]
            self.root.brush_list.append([0/float(255), 255/float(255), 154/float(255), 1])
        else:
            self.md_bg_color  = [190/float(255), 190/float(255), 190/float(255), 1]
            self.root.ids.green_label.color = [0, 0, 0, 1]
            self.root.brush_list.remove([0/float(255), 255/float(255), 154/float(255), 1])
class AddBlueBrush(TouchBox):
    def respondToTouch(self):
        if self.md_bg_color != [0, 0, 0, 1]:
            self.md_bg_color  = [0, 0, 0, 1]
            self.root.ids.blue_label.color = [1, 1, 1, 1]
            self.root.brush_list.append([0/float(255), 154/float(255), 255/float(255), 1])
        else:
            self.md_bg_color  = [190/float(255), 190/float(255), 190/float(255), 1]
            self.root.ids.blue_label.color = [0, 0, 0, 1]
            self.root.brush_list.remove([0/float(255), 154/float(255), 255/float(255), 1])
class AddOrangeBrush(TouchBox):
    def respondToTouch(self):
        if self.md_bg_color != [0, 0, 0, 1]:
            self.md_bg_color  = [0, 0, 0, 1]
            self.root.ids.orange_label.color = [1, 1, 1, 1]
            self.root.brush_list.append([255/float(255), 154/float(255), 0, 1])
        else:
            self.md_bg_color  = [190/float(255), 190/float(255), 190/float(255), 1]
            self.root.ids.orange_label.color = [0, 0, 0, 1]
            self.root.brush_list.remove([255/float(255), 154/float(255), 0, 1])
class FinishButtonBox(TouchBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def saveGameData(self, table):
        file_object = open("gameDB", "wb")
        pickle.dump(table, file_object)
    def respondToTouch(self):
        stages_table = {}
        sub_table = {}
        self.root.controls_table["f1"] = self.root.f_one_blocks_number
        self.root.controls_table["f2"] = self.root.f_two_blocks_number
        self.root.controls_table["f3"] = self.root.f_three_blocks_number
        self.root.controls_table["brushes"] = self.root.brush_list
        sub_table["controls"] = self.root.controls_table
        temp_db_file = open("tempDB", "rb")
        path_table = pickle.load(temp_db_file)
        print("Temp_file :", path_table)
        sub_table["path"] = path_table
        stages_table[str(self.root.stage_number)] = sub_table
        print("Stage Table :", stages_table)
        data_table = {}
        self.saveGameData(stages_table)
class ControlsAdditionScreen(MDScreen):
    def __init__(self, **kwargs):
        super(ControlsAdditionScreen, self).__init__(**kwargs)
        self.controls_table = {}
        self.f_one_blocks_number = 2
        self.f_two_blocks_number = 0
        self.f_three_blocks_number = 0
        self.brush_list = []
        self.stage_number = 1
    def subtractStageNumber(self):
        if self.stage_number > 1:
            self.stage_number -= 1
            self.ids.stage_number.text = str(self.stage_number)
    def addStageNumber(self):
        if self.stage_number <= 99: 
            self.stage_number += 1
            self.ids.stage_number.text = str(self.stage_number)
    def removeFOneBlock(self):
        if self.f_one_blocks_number > 2:
            block = self.ids.f_one_blocks_space.children[0]
            self.ids.f_one_blocks_space.remove_widget(block)
            self.f_one_blocks_number -= 1
    def addFOneBlock(self):
        if self.f_one_blocks_number < 6:
            holder = DirectionHolderBlock()
            self.ids.f_one_blocks_space.add_widget(holder)
            self.f_one_blocks_number += 1
    def removeFTwoBlock(self):
        if self.f_two_blocks_number > 0:
            block = self.ids.f_two_blocks_space.children[0]
            self.ids.f_two_blocks_space.remove_widget(block)
            self.f_two_blocks_number -= 1
    def addFTwoBlock(self):
        if self.f_two_blocks_number < 8:
            holder = DirectionHolderBlock()
            self.ids.f_two_blocks_space.add_widget(holder)
            self.f_two_blocks_number += 1
    def removeFThreeBlock(self):
        if self.f_three_blocks_number > 0:
            block = self.ids.f_three_blocks_space.children[0]
            self.ids.f_three_blocks_space.remove_widget(block)
            self.f_three_blocks_number -= 1
    def addFThreeBlock(self):
        if self.f_three_blocks_number < 8:
            holder = DirectionHolderBlock()
            self.ids.f_three_blocks_space.add_widget(holder)
            self.f_three_blocks_number += 1
class NextButton(TouchBox):
    def respondToTouch(self):
        if self.md_bg_color == [0, 154/float(255), 255/float(255), 1]:
            self.root.parent.transition = SlideTransition(direction = "left")
            self.root.parent.current = "controls_addition_screen"
            temp_file_object = open("tempDB", "wb")
            pickle.dump(self.root.path_table, temp_file_object)
class StageSetterScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MDScreen, self).__init__(**kwargs)
        self.current_block = None
        self.walker_block = None
        self.xx = {}
        self.path_table = {}
    def checkIfTableComplete(self):
        if len(self.path_table) >= 2:
            next = True
            walker = False
            for key in self.path_table:
                sub_table = self.path_table[key]
                if not ("color" in sub_table.keys()):
                    next = False
                    break
                elif ("walker" in sub_table.keys()):
                    walker = True
            if next and walker:
                self.ids.next_button_box.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
                self.ids.next_button_box.children[0].color = [1, 1, 1, 1]
            else:
                self.ids.next_button_box.md_bg_color = [220/float(255), 220/float(255), 220/float(255), 1]
                self.ids.next_button_box.children[0].color = [0, 0, 0, 1]
    def addWalkerOnTable(self, walker):
        try:
            sub_table = self.path_table[str(self.current_block.parent.children.index(self.current_block))]
            if "food" in sub_table.keys():
                sub_table.pop("food")
                print("Foooooooood")
                self.ids.next_button_box.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
                self.ids.next_button_box.children[0].color = [1, 1, 1, 1]
                print("Next Button Color : ", [0/float(255), 154/float(255), 255/float(255), 1])
            sub_table["walker"]  = walker
            self.path_table[str(self.current_block.parent.children.index(self.current_block))] = sub_table
        except:
            self.path_table[str(self.current_block.parent.children.index(self.current_block))] = {"walker":walker}
    def chooseWalker(self, button):
        if self.current_block:
            self.ids.erase_block.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
            self.ids.erase_block.children[0].color = [1, 1, 1, 1]
            self.current_block.ids.icon_space.icon = button.icon
            self.current_block.ids.icon_space.text_color = [1, 1, 1, 1] 
            self.addWalkerOnTable(button.icon)
            if self.walker_block and (self.walker_block != self.current_block):
                sub_table = self.path_table[str(self.walker_block.parent.children.index(self.walker_block))]
                if "walker" in sub_table.keys():
                    sub_table.pop("walker")
                self.path_table[str(self.walker_block.parent.children.index(self.walker_block))] = sub_table
                self.xx[str(self.walker_block.parent.children.index(self.walker_block))]  = sub_table
                if self.walker_block.ids.icon_space.icon in ["chevron-triple-right", "chevron-triple-left", "chevron-triple-down", "chevron-triple-up"]:
                    self.walker_block.ids.icon_space.icon = "stop"
                    self.walker_block.ids.icon_space.text_color = self.walker_block.ids.icon_space.md_bg_color
            self.walker_block = self.current_block
            self.checkIfTableComplete()
    def addFoodOnTable(self, food):
        try:
            sub_table = self.path_table[str(self.current_block.parent.children.index(self.current_block))]
            if "walker" in sub_table.keys():
                sub_table.pop("walker")
            sub_table["food"]  = food
            self.path_table[str(self.current_block.parent.children.index(self.current_block))] = sub_table
        except:
            self.path_table[str(self.current_block.parent.children.index(self.current_block))] = {"food":food}
        self.checkIfTableComplete()
    def chooseFood(self, button):
        if self.current_block:
            self.ids.erase_block.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
            self.ids.erase_block.children[0].color = [1, 1, 1, 1]
            self.current_block.ids.icon_space.icon = button.icon
            self.current_block.ids.icon_space.text_color = [1, 1, 1, 1]
            self.addFoodOnTable(button.icon)
class MainScreenManager(ScreenManager):
    pass
class StageSetterApp(MDApp):
    def build(self):
        root = MainScreenManager()
        return root
if __name__ == "__main__":
    StageSetterApp().run()