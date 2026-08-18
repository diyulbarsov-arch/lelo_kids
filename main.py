from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock

# ============================================================
# ГЛАВНЫЙ ЭКРАН
# ============================================================
class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Заголовок
        self.add_widget(Label(text='LE&LO kids', font_size=32, bold=True, color=(0.4, 0.49, 0.91, 1), size_hint_y=0.15))

        # Поле для логина
        self.login_input = TextInput(hint_text='Логин (номер швеи)', multiline=False, font_size=18)
        self.add_widget(self.login_input)

        # Поле для пароля
        self.password_input = TextInput(hint_text='Пароль', multiline=False, password=True, font_size=18)
        self.add_widget(self.password_input)

        # Кнопка входа
        btn = Button(text='Войти', font_size=18, background_color=(0.4, 0.49, 0.91, 1))
        btn.bind(on_press=self.login)
        self.add_widget(btn)

        # Метка для ошибок
        self.error_label = Label(text='', color=(1, 0, 0, 1), size_hint_y=0.1)
        self.add_widget(self.error_label)

    def login(self, instance):
        login = self.login_input.text.strip()
        password = self.password_input.text.strip()

        if login == 'admin' and password == 'admin123':
            self.error_label.text = '✅ Вход выполнен!'
            self.show_welcome()
        else:
            self.error_label.text = '❌ Неверный логин или пароль'

    def show_welcome(self):
        # Очищаем экран
        self.clear_widgets()
        # Показываем приветствие
        self.add_widget(Label(text='👋 Добро пожаловать!', font_size=28, bold=True, color=(0.2, 0.8, 0.4, 1)))
        self.add_widget(Label(text='Вы успешно вошли в систему LE&LO kids', font_size=18))
        btn = Button(text='Выйти', font_size=16, background_color=(0.9, 0.2, 0.2, 1), size_hint_y=0.1)
        btn.bind(on_press=self.logout)
        self.add_widget(btn)

    def logout(self, instance):
        # Возвращаем экран входа
        self.clear_widgets()
        self.__init__()

# ============================================================
# ЗАПУСК ПРИЛОЖЕНИЯ
# ============================================================
class PlanchetApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    PlanchetApp().run()
