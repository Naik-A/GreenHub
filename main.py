from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image as KivyImage
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex
import fitz

class GreenHubApp(App):
    def build(self):
        self.title = 'GreenHub - Green Chemistry at Your Fingertips'
        return self.create_main_interface()

    def create_main_interface(self):
        # Main layout with vertical orientation
        main_layout = BoxLayout(orientation='vertical', spacing=10)

        # Green-themed background
        with main_layout.canvas.before:
            Color(rgb=get_color_from_hex('#4CAF50'))
            Rectangle(pos=main_layout.pos, size=main_layout.size)

        # Feature Buttons with green color
        features = ["Case Studies", "Best Practices", "Interactive Elements", "RecycleHub", "Sustainability"]

        for feature in features:
            button = Button(text=feature, on_press=self.on_feature_button_press, background_color=get_color_from_hex('#388E3C'))
            main_layout.add_widget(button)

        # App Logo
        app_logo = KivyImage(source='path_to_your_app_logo.png', size_hint=(1, None), height=100, allow_stretch=True)
        main_layout.add_widget(app_logo)

        return main_layout

    def on_feature_button_press(self, instance):
        feature_name = instance.text
        if feature_name == "Sustainability":
            self.show_sustainability_pdf()
        else:
            print(f"You pressed the {feature_name} feature.")

    def show_sustainability_pdf(self):
        # Replace 'your_sustainability_pdf.pdf' with the actual path of your Sustainability PDF file
        sustainability_pdf_path = r"C:\\Users\\abhik\\Desktop\\SS greenhub\\3527309853_c01.pdf"
        
        # Read the content of the PDF using fitz
        text_content = self.read_pdf(sustainability_pdf_path)

        # Display the Sustainability PDF content in a new popup with green color
        pdf_popup = Popup(title='Sustainability PDF Viewer', content=ScrollView(size_hint=(1, None), size=(800, 600)),
                          size_hint=(None, None), size=(800, 600), background_color=get_color_from_hex('#4CAF50'))
        
        pdf_popup.content.add_widget(Label(text=text_content, font_size=12, color=get_color_from_hex('#000000')))
        pdf_popup.open()

    def read_pdf(self, sustainability_pdf_path):
        # Read the content of the PDF using fitz
        pdf_document = fitz.open(sustainability_pdf_path)
        text_content = ""

        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text_content += page.get_text()

        return text_content

if __name__ == '__main__':
    GreenHubApp().run()
