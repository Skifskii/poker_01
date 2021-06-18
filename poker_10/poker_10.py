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


class MyApp(App):


    def add_num(self,instance):
        print(int(instance.text))


    def build(self):
        rows = BoxLayout(orientation = 'vertical') #, padding = [10, 30, 10, 450])
        suits = BoxLayout(orientation = 'horizontal', spacing = 10, padding = [30], size_hint = (1, .20))
        num = GridLayout(cols = 3, spacing = 10, padding = [50, 0], size_hint = (1, .4))
        j_a = BoxLayout(orientation = 'horizontal', spacing = 10, padding = [30], size_hint = (1, .20))
        #eight_ten = BoxLayout(orientation = 'horizontal', spacing = 10, padding = [50])

        rows.add_widget(Label(text = 'Сколько игроков за столом?', font_size = 20, size_hint=(1, .3)))

        suits.add_widget(Button(text = 'ch', font_size = 27, background_color = [1, 0, 1, 1], on_press = self.add_num))
        suits.add_widget(Button(text = 'bu', font_size = 27, background_color = [1, 0, 1, 1], on_press = self.add_num))
        suits.add_widget(Button(text = 'kr', font_size = 27, background_color = [1, 0, 1, 1], on_press = self.add_num))
        suits.add_widget(Button(text = 'pi', font_size = 27, background_color = [1, 0, 1, 1], on_press = self.add_num))

        rows.add_widget(suits)

        for i in range(2, 11):
            btn1 = Button(text = str(i), font_size = 27, background_color = [1, 0, 1, 1])
            btn1.bind(on_press = self.add_num)
            num.add_widget(btn1)
            
        rows.add_widget(num)
        
        j_a.add_widget(Button(text = 'J', font_size = 27, background_color = [1, 0, 1, 1], on_press = self.add_num))
        j_a.add_widget(Button(text = 'Q', font_size = 27, background_color = [1, 0, 1, 1], on_press = self.add_num))
        j_a.add_widget(Button(text = 'K', font_size = 27, background_color = [1, 0, 1, 1], on_press = self.add_num))
        j_a.add_widget(Button(text = 'A', font_size = 27, background_color = [1, 0, 1, 1], on_press = self.add_num))

        rows.add_widget(j_a)
        '''for i in range(5, 8):
           five_seven.add_widget(Button(text = str(i)))

        rows.add_widget(five_seven)

        for i in range(8, 11):
            eight_ten.add_widget(Button(text = str(i)))

        rows.add_widget(five_seven)'''
        
        return rows    


if __name__ == '__main__':
    MyApp().run()
