import PySimpleGUI as sg
from calculator import Calculator
from apihandler import ApiHandler

C_BTN_SIZE = (7,2)


LAYOUT = [
    [sg.Text('',size=(19, 1), font=('Arial', 24) , key='-INPUT-',text_color='black', background_color='white')],
    [sg.Button('7', size=C_BTN_SIZE),sg.Button('8', size=C_BTN_SIZE),sg.Button('9', size=C_BTN_SIZE), sg.Button('+/-', size=C_BTN_SIZE, button_color='darkgray'), sg.Button('<-', size=C_BTN_SIZE, button_color='darkgray')],
    [sg.Button('4', size=C_BTN_SIZE),sg.Button('5', size=C_BTN_SIZE),sg.Button('6', size=C_BTN_SIZE), sg.Button('*', size=C_BTN_SIZE, button_color='gray'), sg.Button('/', size=C_BTN_SIZE, button_color='gray')],
    [sg.Button('1', size=C_BTN_SIZE),sg.Button('2', size=C_BTN_SIZE),sg.Button('3', size=C_BTN_SIZE),sg.Button('+', size=C_BTN_SIZE, button_color='gray') , sg.Button('-', size=C_BTN_SIZE, button_color='gray')],
    [sg.Button('C', size=C_BTN_SIZE, button_color='red'), sg.Button('0', size=C_BTN_SIZE),sg.Button('.', size=C_BTN_SIZE),sg.Button('click', size=C_BTN_SIZE), sg.Button('=', size=C_BTN_SIZE, button_color='darkblue')],
    [sg.Button('^', size=(16,2)), sg.Button('√', size=(16,2))],
    [sg.Text('Podaj wzór funkcji: ',size=(15,1)), sg.InputText(size=(16,1)), sg.Button("2D"),  sg.Button("3D")],
]

class CalculatorGUI:
    def __init__(self):
        self.api_handler = ApiHandler()
        self.calculator = Calculator()
        self.on_display = ''

        self.first = False
        self.operation = False
        self.operation_changed = False
        self.first_run = 0
        
    def open_main_window(self):
        self.__window = sg.Window('Simple calculator', 
                            layout=LAYOUT, 
                            element_justification='c', 
                            finalize=True)
        
    def open_function_window(self, new_func:str):
        
        self.api_handler.get_new_image(new_func)
        filename = new_func.replace(' ', '_')
        
        popup_layout = [
        [sg.Image(f'images/{filename}.png', key='-IMAGE-')],
        ]
        sg.Window('Function plot', 
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

    def clear_screen(self):
        self.on_display = ''
        self.update_screen()

    def reset_flags(self):
        self.first = False
        self.operation = False
        self.operation_changed = False
        self.first_run = 0
        self.num_changed = False
        self.number_typing = True
        self.calculator.reset()

    def set_display_data(self, data): # for tests
        self.on_display = data

    def get_display_data(self): # for tests
        return self.on_display

    def change_sign(self):
        if len(self.on_display) > 2 and self.on_display[0] == 0 or len(self.on_display) > 0:

            self.on_display = '-' + self.on_display if self.on_display[0] != '-' else self.on_display[1:]
            self.operation_changed = False
            self.update_screen()

    def remove_char(self):
        if len(self.on_display) > 0:
            self.on_display = self.on_display[:-1]
        self.update_screen()

    def handle_sign(self, sign):
        if not len(self.on_display):
            return
        
        if not self.first:
            self.calculator.set_first(self.on_display)
            self.first = True

        if not self.operation_changed:
            self.first_run += 1 
            self.operation_changed = True


        print(self.first_run)
        if self.first_run > 1:
            self.perform_the_action()

        self.on_display = sign
        self.operation = sign
        self.calculator.set_operation(sign)
        self.update_screen()

    def handle_nums(self, num):
        if len(self.on_display) == 1 and self.on_display[0] in '0+-*/^':
            self.clear_screen()
        self.on_display += str(num)
        # self.calculator.set_second(self.on_display) # not required
        self.update_screen()
        self.num_changed = True
        self.operation_changed = False
        
    def show_result(self):
        if self.first and self.operation and len(self.on_display) > 0:
            self.perform_the_action()
            self.update_screen()

    def perform_the_action(self):
        if self.num_changed:
            self.calculator.set_second(self.on_display)
        try:
            self.calculator.handle_operations()
        except KeyError:
            pass
        except ZeroDivisionError:
            sg.Popup("Can't divide by 0!", keep_on_top=True)
        except ValueError:
            sg.Popup("Can't raise 0 to the power of 0, it's undefined!", keep_on_top=True)
        finally:
            self.on_display = self.calculator.get_result()
            self.calculator.set_first(self.on_display)
            self.first_run = 0
            self.num_changed = False

    def handle_sqrt(self):
        if len(self.on_display) > 0:
            self.calculator.set_first(self.on_display)
            if self.on_display[0] in '0123456789':
                self.first = True
                self.operation='√'
                self.calculator.set_operation('√')
                self.calculator.sqrt()
                self.show_result()
            else:
                sg.Popup("Can't get sqrt of negative number!", keep_on_top=True, )

    def update_screen(self):
        self.__window['-INPUT-'].update(self.on_display)