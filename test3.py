import datetime
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget

from plyer  import storagepath

import shutil

Builder.load_file('cam.kv')

class Mylayout(Widget):
    def hello_on(self):
        self.ids.my_label.text="Nguyễn Huy Hoàng ......"
    def hello_off(self):
        self.ids.my_label.text="hoang camfhoang camfhoang camfhoang camfhoang camfhoang camfhoang camfhoang camfhoang camfhoang camfhoang camf"

class CameraApp(App):


    source = str(storagepath.get_pictures_dir())
    target = ""
    def build(self):
        return Mylayout()

    def picture_taken(self, obj, filename):
        print('Picture taken and saved to {}'.format(filename))

        #self.source = str(storagepath.get_pictures_dir())
        self.target = filename
        

        shutil.copy(self.target , self.source)


if __name__ == '__main__':
    CameraApp().run()