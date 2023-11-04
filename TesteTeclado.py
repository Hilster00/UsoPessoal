import keyboard


def on_press(event):
        if event.name in "1234567890":
            print(f'Tecla {event.name} d', end="")
            if event.is_keypad:
                print('o Teclado Numérico pressionada.')
            else:
                print('a Parte Superior do Teclado pressionada.')
        elif event.name == "enter":
            print("Enter",end="")
            if event.is_keypad:
                print(" do Teclado Numérico pressionada.")
            else:
                print(" Grande pressionada.")
        elif event.name == "pause":
            print("Tecla Pause Break pressionada.")
        else:
            print(f"Tecla {event.name} pressionada.")

keyboard.on_press(on_press)

while True:
    
    keyboard.wait()
