import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.oled import OLED
from kmk.modules.rgb import RGB
from kmk.modules.layers import Layers

i2c = busio.I2C(scl=board.SCL, sda=board.SDA)
oled_address = 0x3C
keyboard = KMKKeyboard()

keyboard.col_pins = (board.D11, board.D10, board.D9)
keyboard.row_pins = (board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

oled_mod = OLED()
keyboard.modules.append(oled_mod)

rgb_mod = RGB(
    pixel_pin=board.D7,
    num_pixels=1,
    hue_default=180,
    brightness_default=0.3,
    animation_speed=2,
    animation_mode="swirl",
)
keyboard.modules.append(rgb_mod)

keyboard.keymap = [
    [KC.A, KC.B, KC.C,
     KC.D, KC.E, KC.F,
     KC.G, KC.H, KC.I]
]

keyboard.go()