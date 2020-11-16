from abstraction import SendEmail
from inheritance import *
from typing import Awaitable, Callable, TypeVar

def main_0():
    send_email = SendEmail()
    # send_email.send_email()
    username = send_email.username
    _username = send_email._username
    # __username = send_email.__username

    send_email.username = 'AAAAAAAAAA'
    send_email._username = 'AAAAAAAAAA'
    send_email.__username = 'AAAAAAAAAA'
    send_email._authenticate()
    # send_email('Passed message')

def main_1():
    text_box = globals()['TextBox']()
    text_box.mytree()

    draw_ui_control(text_box)

    check_box = CheckBox()
    text_box.equal(check_box)
    draw_ui_control(text_box)

def draw_ui_control(control):
    """
    Gets the control type and draws itself
    """
    control.draw()

def main_2():
    music = 'teste.mp3'


main_1()
print()