from calculatorgui import CalculatorGUI
import PySimpleGUI as sg


if __name__ == "__main__":
    gui = CalculatorGUI() # tworzenie naszego okienka
    while True:
        event, values = gui.get_window_data() # odebranie danych od okienka naszej aplikacji
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event in ['2D', '3D']:
            new_func = event + 'plot ' + values[0] # zapytanie do API (zrobienie wykresu)
            gui.open_function_window(new_func) # wyświetlenie odebranego wykresu
        elif event in '0123456789':
            gui.handle_nums(event)
        elif event == 'C':
            gui.clear_screen()
        elif event == '.':
            gui.handle_dot()
        elif event == '+/-':
            gui.change_sign()
        elif event == '<-':
            gui.remove_char()
        elif event in '+-*/':
            gui.handle_sign(event)