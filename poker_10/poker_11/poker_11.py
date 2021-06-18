import random

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


def main_code(num_of_players, user_card_1_num, user_card_1_suit, user_card_2_num, user_card_2_suit):
    def fill_deck(suit):
        for i in range(2, 15):
            num = i    
            deck.append([num, suit])


    def create_deck():
        fill_deck('ch')
        fill_deck('bu')
        fill_deck('kr')
        fill_deck('pi')


    def print_all_combinations():
        print('river')
        print(river)

        print('')
        print('YOU')
        print(user.card_1, user.card_2)
        print(user.combination) 

        for i in range(num_of_players - 1):
            print('')
            print(i+2)
            print(players[i].card_1, players[i].card_2)
            print(players[i].combination)


    def compare_combinations(i):
        if user.combination[0] == 1:
            if user.combination[1] < players[i].combination[1]:
                return 0

        if user.combination[0] == 2:
            if user.combination[1] < players[i].combination[1]:
                return 0
            if user.combination[1] == players[i].combination[1]:
                user_cards = [user.card_1, user.card_2]
                playser_cards = [players[i].card_1, players[i].card_2]
                if max(playser_cards) > max(user_cards):
                    return 0    

        if user.combination[0] == 3:
            if user.combination[2] < players[i].combination[2]:
                return 0         
            if user.combination[2] == players[i].combination[2]:
                if user.combination[1] < players[i].combination[1]:
                    return 0 
                if user.combination[1] == players[i].combination[1]:
                    user_cards = [user.card_1, user.card_2]
                    playser_cards = [players[i].card_1, players[i].card_2]
                    if max(playser_cards) > max(user_cards):
                        return 0     

        if user.combination[0] == 4:
            if user.combination[1] < players[i].combination[1]:
                return 0 
            if user.combination[1] == players[i].combination[1]:
                user_cards = [user.card_1, user.card_2]
                playser_cards = [players[i].card_1, players[i].card_2]
                if max(playser_cards) > max(user_cards):
                    return 0

        if user.combination[0] == 5:
            if user.combination[1] < players[i].combination[1]:
                return 0  
            if user.combination[1] == players[i].combination[1]:
                user_cards = [user.card_1, user.card_2]
                playser_cards = [players[i].card_1, players[i].card_2]
                if max(playser_cards) > max(user_cards):
                    return 0           

        if user.combination[0] == 6:
            return 1

        if user.combination[0] == 7:
            return 1     

        if user.combination[0] == 8:
            if user.combination[1] < players[i].combination[1]:
                return 0 
            if user.combination[1] == players[i].combination[1]:
                user_cards = [user.card_1, user.card_2]
                playser_cards = [players[i].card_1, players[i].card_2]
                if max(playser_cards) > max(user_cards):
                    return 0    

        if user.combination[0] == 9:
            return 1        

        return 1        

        
    def determine_the_winner():
        for i in range(num_of_players - 1):
            if players[i].combination[0] > user.combination[0]:
                return 0
            elif players[i].combination[0] == user.combination[0]:
                if compare_combinations(i) == 0:
                    return 0  
        return 1              


    class Player():


        def __init__(self):
            self.card_1 = None
            self.card_2 = None
            self.combination = None
            self.is_three = 0
            self.is_straight = 0
            self.is_flush = 0
            self.is_winner = 0


        def add_cards(self, is_user=0):
            if is_user == 0:
                self.card_1 = random.choice(deck)
                deck.remove(self.card_1) 
                self.card_2 = random.choice(deck)
                deck.remove(self.card_2) 
            else:               
                my_cards = []

                self.card_1 = [str(user_card_1_num), str(user_card_1_suit)]    
                self.card_2 = [str(user_card_2_num), str(user_card_2_suit)]

                
                if self.card_1[0] == 'J':
                    self.card_1[0] = 11
                elif self.card_1[0] == 'Q':
                    self.card_1[0] = 12
                elif self.card_1[0] == 'K':
                    self.card_1[0] = 13
                elif self.card_1[0] == 'A':
                    self.card_1[0] = 14     
                else:
                    self.card_1[0] = int(self.card_1[0])

                if self.card_2[0] == 'J':
                    self.card_2[0] = 11
                elif self.card_2[0] == 'Q':
                    self.card_2[0] = 12
                elif self.card_2[0] == 'K':
                    self.card_2[0] = 13
                elif self.card_2[0] == 'A':
                    self.card_2[0] = 14     
                else:
                    self.card_2[0] = int(self.card_2[0])    

                deck.remove(self.card_1)
                deck.remove(self.card_2)  

        #2 3
        def check_pairs(self):
            num = 0
            kol_pairs = 0
            for i in range(2, 15):
                if self.nums.count(i) == 2:
                    kol_pairs += 1
                    pred_num = num
                    num = i

            if kol_pairs == 1:
                self.combination = [2, num] 

            if kol_pairs == 2:
                self.combination = [3, pred_num, num] 

        #4
        def check_three_of_a_kind(self):
            num = 0
            kol_threes = 0
            for i in range(2, 15):
                if self.nums.count(i) == 3:
                    kol_threes += 1
                    num = i

            if kol_threes > 0:
                self.combination = [4, num] 
                self.is_three = num

        #5
        def check_straight(self):
            temp = 0
            num = 0
            for i in range(1, 7):
                if self.nums[i] - self.nums[i-1] == 1:
                    temp += 1
                    num = self.nums[i]
                else:
                    if self.nums[i] != self.nums[i-1]:
                        if temp < 4:
                            temp = 0    

            if temp >= 4:
                self.combination = [5, num]
                self.is_straight = 1
            if self.nums.count(14)>0 and self.nums.count(2)>0 and self.nums.count(3)>0 and self.nums.count(4)>0 and self.nums.count(5)>0:
                self.combination = [5, 5]      
                self.is_straight = 1   

        #6    
        def check_flush(self):
            self.seven_cards = sorted(self.seven_cards)
            suits = []
            for i in range(7):
                suits.append(self.seven_cards[i][1])

            for i in range(7):
                if suits.count(suits[i]) >= 5:
                    self.combination = [6]
                    self.is_flush = 1

        #7
        def check_full_hose(self):
            if self.is_three > 0:
                kol_pairs = 0
                for i in range(2, 15):
                    if self.nums.count(i) == 2:
                        kol_pairs += 1

                if kol_pairs == 1:
                    self.combination = [7]

        #8
        def check_four_of_a_kind(self):
            num = 0
            kol_fours = 0
            for i in range(2, 15):
                if self.nums.count(i) == 4:
                    kol_fours += 1
                    num = i

            if kol_fours > 0:
                self.combination = [8, num] 
                self.is_three = num           
                        
        #9
        def check_straight_flush(self):
            if self.is_straight > 0 and self.is_flush > 0:
                self.combination = [9]                


        def check_combinations(self):
            self.seven_cards = river.copy()
            self.seven_cards.append(self.card_1)
            self.seven_cards.append(self.card_2)   
            
            self.nums = []
            for i in range(7):
                self.nums.append(self.seven_cards[i][0])

            self.nums = sorted(self.nums)

            self.check_pairs()
            self.check_three_of_a_kind()
            self.check_straight()
            self.check_flush()
            self.check_full_hose()
            self.check_four_of_a_kind()
            self.check_straight_flush()
            if self.combination == None:
                self.combination = [1, self.nums[-1]]
            self.is_three = 0
            self.is_straight = 0
            self.is_flush = 0        

    
    deck = []
    create_deck() 
    
    user = Player()
    user.add_cards(1)

    ''' ПАРТИЯ '''
    kol_wins = 0
    pogr = 10000
    for i in range(pogr):
        ''' СОЗДАНИЕ КОЛОДЫ ''' 
        deck = []
        create_deck()  

        deck.remove(user.card_1)
        deck.remove(user.card_2)  


        ''' СОЗДАНИЕ ИГРКОВ '''
        players = []
        for i in range(num_of_players - 1):
            players.append(Player())

        for i in range(num_of_players - 1):
            (players[i]).add_cards()


        ''' РИВЕР '''
        river = []
        #river = [[9, 'pi'], [10, 'ch'], [11, 'kr'], [12, 'ch'], [8, 'bu']]

        for i in range(5):
            card = random.choice(deck)
            river.append(card)
            deck.remove(card) 

        ''' ПРОВЕРКА КОМБИНАЦИЙ '''

        for i in range(num_of_players-1):
            (players[i]).check_combinations()
        user.check_combinations()

        if determine_the_winner() == 1:
            kol_wins += 1

        river.clear()
        for i in range(num_of_players-1):
            (players[i]).combination = None
        user.combination = None
            
        
    print('')
    print(str(kol_wins//(pogr//100)) + ',' + str(kol_wins%(pogr//100)) + '%')  
    ans = str(kol_wins//(pogr//100)) + ',' + str(kol_wins%(pogr//100)) + '%'
    MyApp.end = 1
    MyApp.answer = ans

class MyApp(App):


    def play_again(self):
        self.rows.clear_widgets()
        self.build()


    def add_num(self, instance):
        if MyApp.end == 0:           
            if MyApp.step == 2:
                if MyApp.card_num == 2:
                    MyApp.user_card_2_num = str(instance.text)
                    self.lbl.text = str(MyApp.user_card_1_num) + str(MyApp.user_card_1_suit) + '   ' + str(MyApp.user_card_2_num) + str(MyApp.user_card_2_suit)
                    print(MyApp.user_card_2_num) 
                
                if MyApp.card_num == 1:
                    MyApp.user_card_1_num = str(instance.text)
                    MyApp.card_num += 1
                    self.lbl.text = str(MyApp.user_card_1_num) + str(MyApp.user_card_1_suit) + '   ' + str(MyApp.user_card_2_num) + str(MyApp.user_card_2_suit)
                    print(MyApp.user_card_1_num)
            else:
                MyApp.num_of_players = int(instance.text)
                print(MyApp.num_of_players)
                self.lbl.text = 'Какие у вас карты?'
                MyApp.step = 2
        else:
            self.play_again()        


    def add_user_card_num(self, instance):
        if MyApp.card_num == 2:
            MyApp.user_card_2_num = str(instance.text)
            self.lbl.text = str(MyApp.user_card_1_num) + str(MyApp.user_card_1_suit) + '   ' + str(MyApp.user_card_2_num) + str(MyApp.user_card_2_suit)
            print(MyApp.user_card_2_num)
        if MyApp.card_num == 1:
            MyApp.user_card_1_num = str(instance.text)
            MyApp.card_num += 1
            self.lbl.text = str(MyApp.user_card_1_num) + str(MyApp.user_card_1_suit) + '   ' + str(MyApp.user_card_2_num) + str(MyApp.user_card_2_suit)
            print(MyApp.user_card_1_num) 


    def add_user_card_suit(self, instance):
        if MyApp.card_suit == 2:
            MyApp.user_card_2_suit = str(instance.text)
            self.lbl.text = str(MyApp.user_card_1_num) + str(MyApp.user_card_1_suit) + '   ' + str(MyApp.user_card_2_num) + str(MyApp.user_card_2_suit)
            print(MyApp.user_card_2_suit)
            main_code(MyApp.num_of_players, MyApp.user_card_1_num, MyApp.user_card_1_suit, MyApp.user_card_2_num, MyApp.user_card_2_suit)
            self.lbl.text = MyApp.answer
        if MyApp.card_suit == 1:
            MyApp.user_card_1_suit = str(instance.text)
            MyApp.card_suit += 1
            self.lbl.text = str(MyApp.user_card_1_num) + str(MyApp.user_card_1_suit) + '   ' + str(MyApp.user_card_2_num) + str(MyApp.user_card_2_suit)
            print(MyApp.user_card_1_suit)
                    

    def build(self):
        MyApp.step = 1
        MyApp.card_num = 1
        MyApp.card_suit = 1
        MyApp.user_card_1_num = ''
        MyApp.user_card_1_suit = ''
        MyApp.user_card_2_num = ''
        MyApp.user_card_2_suit = ''
        MyApp.end = 0
        MyApp.answer = ''

        self.rows = BoxLayout(orientation = 'vertical') #, padding = [10, 30, 10, 450])
        suits = BoxLayout(orientation = 'horizontal', spacing = 10, padding = [30], size_hint = (1, .20))
        num = GridLayout(cols = 3, spacing = 10, padding = [50, 0], size_hint = (1, .4))
        j_a = BoxLayout(orientation = 'horizontal', spacing = 10, padding = [30], size_hint = (1, .20))

        self.lbl = Label(text = 'Сколько игроков за столом?', font_size = 20, size_hint=(1, .3))
        self.rows.add_widget(self.lbl)

        suits.add_widget(Button(text = 'ch', font_size = 27, background_color = [1, 0, 0, 1], on_press = self.add_user_card_suit))
        suits.add_widget(Button(text = 'bu', font_size = 27, background_color = [1, 0, 0, 1], on_press = self.add_user_card_suit))
        suits.add_widget(Button(text = 'kr', font_size = 27, background_color = [1, 1, 1, .3], on_press = self.add_user_card_suit))
        suits.add_widget(Button(text = 'pi', font_size = 27, background_color = [1, 1, 1, .3], on_press = self.add_user_card_suit))

        self.rows.add_widget(suits)

        for i in range(2, 11):
            btn1 = Button(text = str(i), font_size = 27, background_color = [1, 1, 1, 1])
            btn1.bind(on_press = self.add_num)
            num.add_widget(btn1)
            
        self.rows.add_widget(num)
        
        j_a.add_widget(Button(text = 'J', font_size = 27, background_color = [1, 1, 1, .7], on_press = self.add_user_card_num))
        j_a.add_widget(Button(text = 'Q', font_size = 27, background_color = [1, 1, 1, .7], on_press = self.add_user_card_num))
        j_a.add_widget(Button(text = 'K', font_size = 27, background_color = [1, 1, 1, .7], on_press = self.add_user_card_num))
        j_a.add_widget(Button(text = 'A', font_size = 27, background_color = [1, 1, 1, .7], on_press = self.add_user_card_num))

        self.rows.add_widget(j_a)
        
        return self.rows    


if __name__ == '__main__':
    MyApp().run()

    
