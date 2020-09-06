from kivymd.app import MDApp
from kivy.uix.screenmanager import (Screen, ScreenManager, NoTransition,
                                    FadeTransition, SlideTransition, WipeTransition)
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
#from kivymd.uix.button import MDRaisedButton
from kivymd.uix.progressbar import MDProgressBar
from kivymd.toast import toast
from kivy.animation import Animation
from random import randint

class PopContent(Popup):
    def __init__(self, which, **kwargs):
        super(PopContent, self).__init__(**kwargs)
        self.title= 'Warning!'
        self.title_size= 12
        self.auto_dismiss= False
        self.size_hint= [0.8, 0.3]
        self.pos_hint= {"top":.7, 'x':.1}
        self.box= BoxLayout(orientation='vertical', spacing=20, padding=5)
        self.add_widget(self.box)
        self.b= Button(bold= True, text='OK', color=(0,0,0,1), background_normal='',
        background_color=(1,1,1,1))
        
        if which == 'outside':        
            self.w= MDLabel(text='you have not entered your monthly income yet!'.title(),
            font_size=17, theme_text_color= "Custom", text_color=[1,1,1,1], bold=True, halign='center')
        elif which == 'inside':
            self.w= MDLabel(text='all textfields have to be saved.'.title(),
            font_size=17, theme_text_color= "Custom", text_color=[1,1,1,1], bold=True, halign='center')
        elif which == 'side':
            self.w= MDLabel(text='\nin order to see your income managements, all your monthly spendings info as well as your monthly income should be entered...'.lower(),
            font_size='8dp', valign='bottom', theme_text_color= "Custom", text_color=[1,1,1,1], bold=False, halign='center')
            self.size_hint_y= 0.35
            self.b.size_hint_y=.35



        self.box.add_widget(self.w)

        self.b.bind(on_press= lambda x: self.dismiss())
        self.box.add_widget(self.b)      
class Results(Popup):
    def __init__(self, data, tot, spent, alll, **kwargs):
        super(Results, self).__init__(**kwargs)
        self.one= data.keys()
        self.two= data.values()
        self.tot= float(sum(tot))
        self.allofit= alll
        self.spent= spent
        self.title= 'Income managements'.title()
        self.title_size= 30
        self.title_size= '20dp'
        self.title_align= 'center'
        self.auto_dismiss= False
        self.size_hint= [.9, .9]
        self.pos_hint= {'x':.05, 'y':.05}
        self.caption1= MDLabel(text='monthly spendings:'.title(), italic= True,
        halign='left', underline=True, size_hint=(1,.1), theme_text_color='Custom',
                        text_color=[.6,0,0,1], pos_hint={'x':0, 'top':1})

        self.box0= BoxLayout(size_hint=(.1, .5), pos_hint= {"top":.92, "center_x":.55},
                             orientation= 'vertical', spacing=14)
        self.box1= BoxLayout(size_hint=(.55, .5), pos_hint= {"top":.92, "x":0},
                             orientation= 'vertical', spacing=14)
        self.box2= BoxLayout(size_hint=(.45, .5), pos_hint= {"top":.92, "x":.53},
                             orientation= 'vertical', spacing=14)
        for item in self.one:
            self.lbl= MDLabel(text=str(item), bold= True, text_color=[1,1,1,1],
            halign='left', theme_text_color='Custom')
            self.box1.add_widget(self.lbl)
        for item2 in self.two:
            self.lbl= MDLabel(text=str(item2)+'$', bold= True, text_color=[1,1,1,1],
            halign='right', theme_text_color='Custom')
            self.box2.add_widget(self.lbl)
        for item2 in self.one:
            self.lbl= Label(text=":", bold= True, color=[1,1,1,1])
            self.box0.add_widget(self.lbl)

        self.total= MDLabel(text='total spendings'.title(), theme_text_color='Custom', 
                        text_color=[.6,0,0,1], bold=True, halign='left')
        self.box1.add_widget(self.total)
        self.colom= Label(text=':', color=[1,1,1,1], bold=True)
        self.box0.add_widget(self.colom)
        self.res= MDLabel(text=str(self.tot)+"$", theme_text_color='Custom', 
                        text_color=[.6,0,0,1], bold=True,halign='right')
        self.box2.add_widget(self.res)

        self.txt= MDLabel(text=f'- you still have an amount of  [b][color=#980000]{str(self.spent)}$[/color][/b]  from your monthly income.'.lower(),
                            markup= True, theme_text_color='Custom', text_color=[1,1,1,1], halign='left',
                             size_hint=(1, .2), pos_hint= {"top":.45, "x":0})
        self.txt2= MDLabel(text=f'- you spent a percentage of  [b][color=#980000]{str(100-((float(self.spent)*100)/float(self.allofit)))}%[/color][/b]  from your monthly income'.lower(),
                            markup= True,  theme_text_color='Custom', text_color=[1,1,1,1], halign='left',
                             size_hint=(1, .2), pos_hint= {"top":.35, "x":0})
        self.txt3= MDLabel(text='- this is how much is spent from your monthly income:'.title(),
                            bold= True,  theme_text_color='Custom', text_color=[1,1,1,1], halign='left',
                             size_hint=(1, .2), pos_hint= {"top":.25, "x":0})

        self.bar= MDProgressBar(value=float(100-((float(self.spent)*100)/float(self.allofit))), color=[1,1,1,1],
                    size_hint=(.6, .1), pos_hint={"x":.05, "top":.15} )
        
        self.txt4= MDLabel(text=str(int(100-((float(self.spent)*100)/float(self.allofit))))+"%",
                            theme_text_color='Custom', text_color=[1,1,1,1],
                             size_hint=(.1, .1), pos_hint= {"top":.15, "x":0.73}, halign='left')


        self.cancel= Button(text='OK', background_normal='',color=[0,0,0,1],
                        background_color=[1,1,1,1], size_hint=(.9, .06), pos_hint={"x":.05, 'top':.07},
                        bold=True)
        self.cancel.bind(on_release=lambda x: self.dismiss())
        self.float= FloatLayout(size_hint=(1, 1), pos_hint={'top':1})
        self.float.add_widget(self.caption1)
        self.float.add_widget(self.box1)
        self.float.add_widget(self.box2)
        self.float.add_widget(self.box0)
        self.float.add_widget(self.txt)
        self.float.add_widget(self.txt2)
        self.float.add_widget(self.txt3)
        self.float.add_widget(self.txt4)
        self.float.add_widget(self.cancel)
        self.float.add_widget(self.bar)
        self.add_widget(self.float)


class Start(Screen):
    pass

class Home(Screen):
    pass

    
class Food(Screen):
    food_data= {"food1":0.0, "food2":0.0}

    def the_sum(self, data, sc_txt):
        if sc_txt == 'food1':
            self.food_data['food1']= data
        elif sc_txt == 'food10':
            pass
        elif sc_txt == 'food2':
            self.food_data['food2']= data
        elif sc_txt == 'food20':
            pass
        
        res= float(sum(self.food_data.values()))
        return res

class Housing(Screen):
    house_data= {"house1":0.0, "house2":0.0, "house3":0.0}

    def the_sum(self, data, sc_txt):
        if sc_txt == 'house1':
            self.house_data['house1']= data
        elif sc_txt == 'house10':
            pass
        elif sc_txt == 'house2':
            self.house_data['house2']= data
        elif sc_txt == 'house20':
            pass
        elif sc_txt == 'house3':
            self.house_data['house3']= data
        elif sc_txt == 'house30':
            pass
        
        res= float(sum(self.house_data.values()))
        return res

class Healthcare(Screen):
    health_data= {"health1":0.0, "health2":0.0, "health3":0.0}

    def the_sum(self, data, sc_txt):
        if sc_txt == 'health1':
            self.health_data['health1']= data
        elif sc_txt == 'health10':
            pass
        elif sc_txt == 'health2':
            self.health_data['health2']= data
        elif sc_txt == 'health20':
            pass
        elif sc_txt == 'health3':
            self.health_data['health3']= data
        elif sc_txt == 'health30':
            pass
        
        res= float(sum(self.health_data.values()))
        return res

class Insurance_Pensions(Screen):
    in_p_data= {"in_p1":0.0, "in_p2":0.0, "in_p3":0.0}

    def the_sum(self, data, sc_txt):
        if sc_txt == 'in_p1':
            self.in_p_data['in_p1']= data
        elif sc_txt == 'in_p10':
            pass
        elif sc_txt == 'in_p2':
            self.in_p_data['in_p2']= data
        elif sc_txt == 'in_p20':
            pass
        elif sc_txt == 'in_p3':
            self.in_p_data['in_p3']= data
        elif sc_txt == 'in_p30':
            pass
        
        res= float(sum(self.in_p_data.values()))
        return res


class Other_Goods_Services(Screen):
    o_g_s_data= {"o_g_s1":0.0, "o_g_s2":0.0, "o_g_s3":0.0}

    def the_sum(self, data, sc_txt):
        if sc_txt == 'o_g_s1':
            self.o_g_s_data['o_g_s1']= data
        elif sc_txt == 'o_g_s10':
            pass
        elif sc_txt == 'o_g_s2':
            self.o_g_s_data['o_g_s2']= data
        elif sc_txt == 'o_g_s20':
            pass
        elif sc_txt == 'o_g_s3':
            self.o_g_s_data['o_g_s3']= data
        elif sc_txt == 'o_g_s30':
            pass
        
        res= float(sum(self.o_g_s_data.values()))
        return res

class Transportation(Screen):
    tran_data= {"tran1":0.0, "tran2":0.0, "tran3":0.0}

    def the_sum(self, data, sc_txt):
        if sc_txt == 'tran1':
            self.tran_data['tran1']= data
        elif sc_txt == 'tran10':
            pass
        elif sc_txt == 'tran2':
            self.tran_data['tran2']= data
        elif sc_txt == 'tran20':
            pass
        elif sc_txt == 'tran3':
            self.tran_data['tran3']= data
        elif sc_txt == 'tran30':
            pass
        
        res= float(sum(self.tran_data.values()))
        return res

class Taxes(Screen):
    taxes_data= {"taxes1":0.0, "taxes2":0.0, "taxes3":0.0}

    def the_sum(self, data, sc_txt):
        if sc_txt == 'taxes1':
            self.taxes_data['taxes1']= data
        elif sc_txt == 'taxes10':
            pass
        elif sc_txt == 'taxes2':
            self.taxes_data['taxes2']= data
        elif sc_txt == 'taxes20':
            pass
        elif sc_txt == 'taxes3':
            self.taxes_data['taxes3']= data
        elif sc_txt == 'taxes30':
            pass
        
        res= float(sum(self.taxes_data.values()))
        return res


class Savings(Screen):
    savings_data= {"savings1":0.0, "savings2":0.0, "savings3":0.0}

    def the_sum(self, data, sc_txt):
        if sc_txt == 'savings1':
            self.savings_data['savings1']= data
        elif sc_txt == 'savings10':
            pass
        elif sc_txt == 'savings2':
            self.savings_data['savings2']= data
        elif sc_txt == 'savings20':
            pass
        elif sc_txt == 'savings3':
            self.savings_data['savings3']= data
        elif sc_txt == 'savings30':
            pass
        
        res= float(sum(self.savings_data.values()))
        return res



class MainApp(MDApp):

    total_data= dict()
    total= [0.0,0,0,0,0,0,0,0]

    def build(self):
        Window.size= (360, 640)
        return Builder.load_file('main.kv')

    # open popup if the income is not entered:
    def show_me(self, which):
        target= PopContent(which)
        target.open()
    
    def on_start(self):
        self.go_to_start()
        Clock.schedule_interval(self.anime_wallet, 1)
        


    # changing screens:
    def go_to_start(self, *args):
        current_screen= self.root.ids.screen_manager
        current_screen.current = 'start_sc'

    def go_to_home(self, s):
        current_screen= self.root.ids.screen_manager
        if s == 'start':
            current_screen.transition= SlideTransition()
        else:
            current_screen.transition= NoTransition()
        current_screen.transition.direction= 'up'
        current_screen.transition.duration= 1/2
        current_screen.current= 'home_sc'

    def go_to_food(self, *args):
        current_screen= self.root.ids.screen_manager
        current_screen.transition= NoTransition()
        current_screen.transition.duration= 1
        current_screen.current= 'food_sc'

    def go_to_housing(self, *args):
        current_screen= self.root.ids.screen_manager
        current_screen.transition.duration= 1
        current_screen.transition= NoTransition()
        current_screen.current= 'housing_sc'

    def go_to_transportation(self, *args):
        current_screen= self.root.ids.screen_manager
        current_screen.transition.duration= 1
        current_screen.transition= NoTransition()
        current_screen.current= 'tran_sc'

    def go_to_iandp(self, *args):
        current_screen= self.root.ids.screen_manager
        current_screen.transition.duration= 1
        current_screen.transition= NoTransition()
        current_screen.current= 'iandp_sc'

    def go_to_savings(self, *args):
        current_screen= self.root.ids.screen_manager
        current_screen.transition.duration= 1
        current_screen.transition= NoTransition()
        current_screen.current= 'savings_sc'

    def go_to_healthcare(self, *args):
        current_screen= self.root.ids.screen_manager
        current_screen.transition.duration= 1
        current_screen.transition= NoTransition()
        current_screen.current= 'health_sc'

    def go_to_othergands(self, *args):
        current_screen= self.root.ids.screen_manager
        current_screen.transition.duration= 1
        current_screen.transition= NoTransition()
        current_screen.current= 'gands_sc'

    def go_to_taxs(self, *args):
        current_screen= self.root.ids.screen_manager
        current_screen.transition.duration= 1
        current_screen.transition= NoTransition()
        current_screen.current= 'taxes_sc'

    def acces_infos(self):
        count= self.total_data.items()
        if len(count) == 8:
            return True
        else:
            return False

    def send_data(self, data, sc, sc_txt):
        data= 0.0 if data == '' else data
        s1= Food()
        s2= Housing()
        s3= Healthcare()
        s4= Transportation()
        s5= Insurance_Pensions()
        s6= Other_Goods_Services()
        s7= Taxes()
        s8= Savings()

        if sc == 'food':
            food= s1.the_sum(float(data), sc_txt)
            self.total_data["Food"]= food
            self.total[0]=food
        elif sc == 'house':
            house= s2.the_sum(float(data), sc_txt)
            self.total_data["Housing"]= house
            self.total[1]=house
        elif sc == 'health':
            health= s3.the_sum(float(data), sc_txt)
            self.total_data["Healthcare"]= health
            self.total[2]=health
        elif sc == 'tran':
            trans= s4.the_sum(float(data), sc_txt)
            self.total_data["Transportation"]= trans
            self.total[3]=trans
        elif sc == 'in_p':
            i_p= s5.the_sum(float(data), sc_txt)
            self.total_data["Insurance/Pension"]= i_p
            self.total[4]=i_p
        elif sc == 'o_g_s':
            gs= s6.the_sum(float(data), sc_txt)
            self.total_data["Other Goods/Services"]= gs
            self.total[5]=gs
        elif sc == 'taxes':
            taxes= s7.the_sum(float(data), sc_txt)
            self.total_data["Taxes"]= taxes
            self.total[6]=taxes
        elif sc == 'savings':
            save= s8.the_sum(float(data), sc_txt)
            self.total_data["Savings"]= save
            self.total[7]=save

    # show the income managements to the user
    def budget_managemnts(self, salary_txt):
        self.spent= float(salary_txt) - sum(self.total)
        self.allofit= salary_txt

        final_res= Results(self.total_data, self.total, self.spent, self.allofit)
        final_res.open()
        

    #Animations:
    def anime_wallet(self, *args):
        target= self.root.ids.start_id.ids.my_wallet
        anime1= Animation(colour=[float(randint(0,255)/255), 0,float(randint(0,255)/255),1], d=0.4)
        anime1.start(target)

if __name__ == '__main__':
    app= MainApp()
    app.run()