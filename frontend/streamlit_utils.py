import re
import streamlit as st    

def num_check(num):
    regex = r"^[0-9]+$"
    if re.match(regex, num):
        return True
    else:
        return False
    
def check_yes_no(answer):
    pattern = r'^\s*(?i)(si|no)\s*$'
    if re.match(pattern, answer):
        return True
    else:
        return False