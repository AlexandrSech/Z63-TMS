"""
Testing pynput module
"""

from pynput.mouse import Button, Controller

mouse = Controller()
mouse.position =(37, 381)
mouse.press(Button.left)
mouse.release(Button.left)
