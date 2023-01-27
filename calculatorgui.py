from apihandler import ApiHandler
from calculator import Calculator
import PySimpleGUI as sg

C_BTN_SIZE = (7,2)


LAYOUT = [
    [sg.Text('',size=(19, 1), font=('Arial', 24) , key='-INPUT-',text_color='black', background_color='white')],
    [sg.Button('7', size=C_BTN_SIZE),sg.Button('8', size=C_BTN_SIZE),sg.Button('9', size=C_BTN_SIZE), sg.Button('+/-', size=C_BTN_SIZE, button_color='darkgray'), sg.Button('<-', size=C_BTN_SIZE, button_color='darkgray')],
    [sg.Button('4', size=C_BTN_SIZE),sg.Button('5', size=C_BTN_SIZE),sg.Button('6', size=C_BTN_SIZE), sg.Button('*', size=C_BTN_SIZE, button_color='gray'), sg.Button('/', size=C_BTN_SIZE, button_color='gray')],
    [sg.Button('1', size=C_BTN_SIZE),sg.Button('2', size=C_BTN_SIZE),sg.Button('3', size=C_BTN_SIZE),sg.Button('+', size=C_BTN_SIZE, button_color='gray') , sg.Button('-', size=C_BTN_SIZE, button_color='gray')],
    [sg.Button('C', size=C_BTN_SIZE, button_color='red'), sg.Button('0', size=C_BTN_SIZE),sg.Button('.', size=C_BTN_SIZE),sg.Button('+', size=C_BTN_SIZE), sg.Button('=', size=C_BTN_SIZE, button_color='darkblue')],
    [sg.Button('^', size=(16,2)), sg.Button('√', size=(16,2))],
    [sg.Text('Podaj wzór funkcji: ',size=(15,1)), sg.InputText(size=(16,1)), sg.Button("2D"),  sg.Button("3D")],
]


class CalculatorGUI:
    def __init__(self):
        self.api_handler = ApiHandler()
        self.calculator = Calculator()
        self.on_display = ''
        self.__window = self.__open_main_window()
    
    def __open_main_window(self):
        window = sg.Window('Testing', 
                            layout=LAYOUT, 
                            element_justification='c', 
                            finalize=True)
        return window
        
    def open_function_window(self, new_func:str):
        
        self.api_handler.get_new_image(new_func)

        popup_layout = [
        [sg.Image('function_image.png', key='-IMAGE-')],
        ]
        sg.Window('Wykres funkcji', 
            layout=popup_layout, 
            element_justification='c', 
            finalize=True, keep_on_top=True)
    
    def get_window_data(self):
        return self.__window.read()
    
    def handle_dot(self):
        if not '.' in self.on_display:
            if len(self.on_display) == 1 and self.on_display[0] == '0' or \
            not len(self.on_display):
                self.on_display = '0.'
            else:
                self.on_display += '.'

            self.update_screen()

    def handle_nums(self, num):
        if len(self.on_display) == 1 and self.on_display[0] in '0+-*/':
            self.clear_screen()
        self.on_display += str(num)
        self.update_screen()

    def clear_screen(self):
        self.on_display = ''
        self.calculator.reset()
        self.update_screen()

    def change_sign(self):
        if len(self.on_display) > 2 and self.on_display[0] == 0 or \
            len(self.on_display):
            self.on_display = '-' + self.on_display if self.on_display[0] != '-' else self.on_display[1:]
            self.update_screen()

    def remove_char(self):
        if len(self.on_display) > 0:
            self.on_display = self.on_display[:-1]
        self.update_screen()

    def handle_sign(self, sign):
        if not len(self.on_display):
            return
        self.calculator.set_temporary(self.on_display)
        self.on_display = sign
        self.update_screen()
        

    def update_screen(self):
        self.__window['-INPUT-'].update(self.on_display)