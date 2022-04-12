from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

#
# class BoxLayoutTest(Screen):
#     pass


# Builder.load_string("""
# <MenuScreen>:
#     BoxLayout:
#         Button:
#             text: 'Goto settings'
#             on_press: root.manager.current = 'settings'
#         Button:
#             text: 'Quit'
#
# <SettingsScreen>:
#     BoxLayout:
#         Button:
#             text: 'My settings button'
#         Button:
#             text: 'Back to menu'
#             on_press: root.manager.current = 'menu'
# """)


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class TheLabApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm
