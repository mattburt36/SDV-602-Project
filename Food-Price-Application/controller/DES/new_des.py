"""
New DES button controller
"""
import sys
sys.dont_write_bytecode = True

def accept( event, values, state):
    from view.DES_view import DES_View
    
    keep_going = True
    if event == 'New DES':
        des_obj = DES_View()
        des_obj.layout_screen()
        des_obj.create()
        des_obj.await_input()
    return keep_going 