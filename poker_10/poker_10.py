import kivy
kivy.require('1.0.7')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '315')
Config.set('graphics', 'height', '560')


def callback(instance):
    print('esssss')


class MyApp(App):
    def build(self):
        rows = BoxLayout(orientation = 'vertical') #, padding = [10, 30, 10, 450])
        num = GridLayout(cols = 3, spacing = 10, padding = [50, 60, 50, 150])
        #five_seven = BoxLayout(orientation = 'horizontal', spacing = 10, padding = [50])
        #eight_ten = BoxLayout(orientation = 'horizontal', spacing = 10, padding = [50])

        rows.add_widget(Label(text = 'Сколько игроков за столом?', font_size = 20, size_hint=(1, .3)))

        for i in range(2, 11):
            btn1 = Button(text = str(i), font_size = 27, background_color = [1, 0, 1, 1])
            btn1.bind(on_press=callback)
            num.add_widget(btn1)
            

        rows.add_widget(num)

        '''for i in range(5, 8):
           five_seven.add_widget(Button(text = str(i)))

        rows.add_widget(five_seven)

        for i in range(8, 11):
            eight_ten.add_widget(Button(text = str(i)))

        rows.add_widget(five_seven)'''
        
        return rows    


if __name__ == '__main__':
    MyApp().run()
