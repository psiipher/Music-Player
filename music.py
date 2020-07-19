from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import os
import sys

os.environ['KIVY_AUDIO'] = 'gstplayer'


class MusicPlayer(App):

    def __init__(self):
        App.__init__(self)
        self.sound = SoundLoader.load('Zara Zara by Maadhyam.mp3')
    

    def build(self):
        layout = FloatLayout()
        playbtn = Button(text="Play",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(450, 150))
                     
        pausebtn = Button(text="Stop",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(750, 150))
                     
        forwardbtn = Button(text="FORWARD",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(750, 400))

        rewindbtn = Button(text="REWIND",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(450, 400))
                     
        volincrease = Button(text="INCREASE\nVOLUME",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(25, 25),
                     size_hint=(.1, .1),
                     pos=(1200, 400))
                     
        voldecrease = Button(text="DECREASE\nVOLUME",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(25, 25),
                     size_hint=(.1, .1),
                     pos=(1200, 200))
                     
        exit = Button(text="EXIT",
                      font_size="20sp",
                      background_color=(1,1,1,1),
                      color=(1,1,1,1),
                      size=(20,20),
                      size_hint=(.1,.1),
                      pos=(0,695))
                      
                     
                     
        layout.add_widget(playbtn)
        layout.add_widget(pausebtn)
        layout.add_widget(forwardbtn)
        layout.add_widget(rewindbtn)
        layout.add_widget(volincrease)
        layout.add_widget(voldecrease)
        layout.add_widget(exit)
        layout.add_widget(Label(text='Zara Zara by Maadhyam', markup=True, font_size="20sp"))

        playbtn.bind(on_press=self.play)
        pausebtn.bind(on_press=self.pause)
        forwardbtn.bind(on_press=self.forward)
        rewindbtn.bind(on_press=self.rewind)
        voldecrease.bind(on_press=self.decrease)
        volincrease.bind(on_press=self.increase)
        exit.bind(on_press=self.stop)

        return layout

    def play(self, event):
        
        if self.sound:
            self.sound.play()

    def pause(self, event):
    	if self.sound:
        	self.sound.stop()
        	
    def forward(self, event):
        if self.sound:
            self.sound.seek(self.sound.get_pos() + 5)
            
    def rewind(self, event):
        if self.sound.get_pos() >= 5:
            self.sound.seek(self.sound.get_pos() - 5)
            
    def increase(self, event):
        self.sound.volume += 0.1
    
    def decrease(self, event):
        self.sound.volume -= 0.1
        
    def exit(self, event):
        sys.exit()

root = MusicPlayer()
Window.fullscreen = 'auto'
root.run()
