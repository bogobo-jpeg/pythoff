def type():
    import keyboard
    import time
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    typeme = input('type string ')
    time.sleep(5)
    print(typeme)
    start = time.time()
    keyboard.type(typeme)
    end = time.time()
    timetook = (end - start)
    print(timetook)
while True:
    type()
