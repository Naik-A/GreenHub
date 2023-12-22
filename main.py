from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from forumapp import mega_function

KV = '''
ScreenManager:
    WelcomeScreen:
    FeaturesScreen:
        name: 'features_screen'

<WelcomeScreen>:
    name: 'welcome_screen'
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)

        MDIconButton:
            icon:r"\\Users\\aayushhnaik\\Downloads\\GreenHub.jpeg" # Update with the correct path to your logo
            user_font_size: "500sp"

        MDLabel:
            text: "Welcome to GreenHub"
            font_style: 'H4'
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1  # Green color

        MDRaisedButton:
            text: "Explore Green Features"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # White color
            md_bg_color: 0, 1, 0, 1  # Green color
            on_press: app.root.current = 'features_screen'

<FeaturesScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)

        FeatureButton:
            text: "Case Studies"
            on_press: app.show_feature("Case Studies")

        FeatureButton:
            text: "Best Practices"
            on_press: app.show_feature("Best Practices")

        FeatureButton:
            text: "Interactive Elements"
            on_press: app.show_feature("Interactive Elements")
        
        FeatureButton:
            text: "Forum"
            on_press: app.show_feature("Forum ")
            
            
        
        FeatureButton:
            text: "Shut App"
            on_press: app.show_feature("Shut App")
            on_press: app.root.current(main)

        FeatureButton:
            text: "Sustainable Material Selection and Green Chemistry Synthesis"
            on_press: app.show_feature("Sustainable Material Selection and Green Chemistry Synthesis")

<FeatureButton@MDRaisedButton>:
    theme_text_color: "Custom"
    text_color: 1, 1, 1, 1  # White color
    md_bg_color: 0, 1, 0, 1  # Green color
'''

class WelcomeScreen(MDScreen):
    pass

class FeaturesScreen(MDScreen):
    pass

class GreenHubApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_feature(self, feature_name):
        print(f"Opening feature: {feature_name}")

if __name__ == '__main__':
    GreenHubApp().run()
