import curses
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT
from luma.led_matrix.device import max7219

device = None

def display(display_type, payload):
    if (display_type == 'input'):
        with canvas(device) as draw:
            text(draw, (0, 0), payload, fill='white', font=proportional(CP437_FONT))
    elif (display_type == 'message'):
        if (payload != ''):
            show_message(device, payload, fill='white', font=proportional(CP437_FONT), y_offset=0, scroll_delay=0.03)

def listen(stdscr):
    user_input = ''
    while True:
        c = stdscr.getch()
        if (c == 10 or c == 13):
            display('message', user_input)
            user_input = ''
        elif (c == 263):
            user_input = user_input[:-1]
            display('input', user_input)
        else:
            user_input += chr(c)
            display('input', user_input)

def init(width, height):
    global device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=width, height=height, block_orientation=-90)
    device.clear()
    device.contrast(10)
    curses.wrapper(listen)

init(192, 8)