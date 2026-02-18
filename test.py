import keyboard

print("Presiona cualquier tecla...")
event = keyboard.read_event()  # espera una tecla
print("Tecla presionada:", event.name)