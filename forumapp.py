#APP
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import shelve
def mega_function():
    class ForumApp(App):
        def build(self):
            self.posts = shelve.open("forum_posts.db", writeback=True)
            self.main_layout = BoxLayout(orientation='vertical', spacing=10)
            self.post_list_layout = BoxLayout(orientation='vertical', spacing=5)
            self.input_layout = BoxLayout(orientation='horizontal', spacing=5)

            self.load_posts()

            self.label = Label(text='GreenHub Forum', font_size=20)
            self.post_list_label = Label(text='Forum Posts:', font_size=16)
            self.post_input = TextInput(hint_text='Type your post...', multiline=False, size_hint_x=0.8)
            self.post_button = Button(text='Post', on_press=self.add_post, size_hint_x=0.2)

            self.main_layout.add_widget(self.label)
            self.main_layout.add_widget(self.post_list_label)
            self.main_layout.add_widget(self.post_list_layout)
            self.main_layout.add_widget(self.input_layout)
            self.input_layout.add_widget(self.post_input)
            self.input_layout.add_widget(self.post_button)

            return self.main_layout

        def load_posts(self):
            if 'posts' not in self.posts:
                self.posts['posts'] = []
            for post in self.posts['posts']:
                self.post_list_layout.add_widget(Label(text=post, font_size=14))

        def add_post(self, instance):
            new_post = self.post_input.text
            if new_post:
                self.posts['posts'].append(new_post)
                self.posts.sync()
                self.post_list_layout.add_widget(Label(text=new_post, font_size=14))

                self.post_input.text = ''

        def on_stop(self):
            self.posts.close()

    if __name__ == '__main__':
        ForumApp().run()
mega_function()
