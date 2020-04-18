import keyboard
import pyautogui
from time import sleep

def hello_world(program):
    keyboard.press_and_release("windows+r")
    sleep(0.5)
    pyautogui.typewrite("notepad")
    sleep(0.5)
    keyboard.press_and_release("return")
    sleep(0.5)
    pyautogui.typewrite(program)


print("1_C\n2_C++\n3_Python\n4_Java\n5_Javascreapt")
lang = int(input())
if lang == 1:
    program = '#include<stdio.h>\nint main()\n{\nprintf("Hellow World!");\nreturn 0;\n}'
if lang == 2:
    program = '#include<iostream>\nint main()\n{\ncout<<"Hello World!";\nreturn 0;\n}'
if lang == 3:
    program = 'print("Hello World!")'
if lang == 4:
    program = 'public class NAME {\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println("Hello World!");\n\t}\n}'
hello_world(program)
