"""
Deploy chat button controller
"""
import sys
sys.dont_write_bytecode = True
from view.chat_view import ChatView

def accept( event, values, state):
    
    keep_going = True
    if event == 'Chat':
        des_obj = ChatView()
        des_obj.set_up_layout()
        des_obj.render()
        des_obj.accept_input()
    return keep_going 
    
    