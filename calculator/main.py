from calculatorgui import CalculatorGUI
import PySimpleGUI as sg

def main():
    gui = CalculatorGUI() # making of app window
    gui.open_main_window()
    while True:
        event, values = gui.get_window_data() # getting data and events from our app
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event in ['2D', '3D']:
            new_func = event + 'plot ' + values[0] # making of command for wolfram API
            gui.open_function_window(new_func) # showing function graph
        elif event in '0123456789':
            gui.handle_nums(event)
        elif event == 'C':
            gui.clear_screen()
            gui.reset_flags()
        elif event == '.':
            gui.handle_dot()
        elif event == '+/-':
            gui.change_sign()
        elif event == '<-':
            gui.remove_char()
        elif event in '+-*/^':
            gui.handle_sign(event)
        elif event == '√':
            gui.handle_sqrt()
        elif event == '=':
            gui.show_result()
        elif event == 'click':
            sg.Popup("There's no point of this popup, just the lack of button prompting it ruins the layout")


if __name__ == "__main__":
    main()