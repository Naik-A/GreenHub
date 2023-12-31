from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

class GreenHubApp(App):
    def build(self):
        self.title = 'GreenHub - Green Chemistry at Your Fingertips'
        return self.create_main_interface()

    def create_main_interface(self):
        # Main layout with green background
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Draw green background
        with main_layout.canvas.before:
            Color(0, 0.6, 0.2, 1)  # Set the background color
            self.background_rect = Rectangle(pos=main_layout.pos, size=main_layout.size)

        main_layout.bind(pos=self.update_background_rect, size=self.update_background_rect)
        #App logo
        app_logo=Image(source=r"C:\\Users\\abhik\\Pictures\\Screenshots\\greenhub.png", size_hint=(1,None), height=100, allow_stretch=True)

        # Header Label
        header_label = Label(text='Welcome to GreenHub!', font_size='24sp', bold=True, color=[1, 1, 1, 1])
        main_layout.add_widget(header_label)

        # Feature Buttons
        feature_buttons_layout = BoxLayout(orientation='horizontal', spacing=10)

        features = ["Case Studies", "Best Practices", "Interactive Elements", "Sustainability", "RecycleHub"]

        for feature in features:
            button = Button(text=feature, on_press=self.on_feature_button_press)
            feature_buttons_layout.add_widget(button)

        main_layout.add_widget(feature_buttons_layout)

        # Screen Manager for Interactive Elements
        self.screen_manager = ScreenManager()

        interactive_elements_screen = Screen(name='Interactive Elements')

        interactive_elements_buttons_layout = BoxLayout(orientation='vertical', spacing=10)
        interactive_features = ["Quiz Fun!", "Green Simulate!", "Videos", "Community"]

        for interactive_feature in interactive_features:
            button = Button(text=interactive_feature, on_press=self.on_interactive_feature_press)
            interactive_elements_buttons_layout.add_widget(button)

        interactive_elements_screen.add_widget(interactive_elements_buttons_layout)
        self.screen_manager.add_widget(interactive_elements_screen)

        main_layout.add_widget(self.screen_manager)

        # Add green-themed image (replace 'your_image_path.png' with the actual image path)
        green_image = Image(source=r"C:\Users\abhik\Pictures\Screenshots\greenhub.png", size_hint=(1, 0.7), allow_stretch=True)
        main_layout.add_widget(green_image)

        return main_layout

    def update_background_rect(self, instance, value):
        self.background_rect.pos = instance.pos
        self.background_rect.size = instance.size

    def on_feature_button_press(self, instance):
        feature_name = instance.text
        if feature_name == "Interactive Elements":
            self.screen_manager.current = 'Interactive Elements'
        else:
            # Handle other features
            print(f"You pressed the {feature_name} feature.")

    def on_interactive_feature_press(self, instance):
        interactive_feature_name = instance.text
        # Handle interactive features
        print(f"You pressed the {interactive_feature_name} feature under Interactive Elements.")

if __name__ == '__main__':
    GreenHubApp().run()
