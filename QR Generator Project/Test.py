# from matplotlib.colors import is_color_like
from colour import Color

def check_color(picked):
        try:
            picked = picked.replace(" ", "")
            Color(picked) 
            return True
        except ValueError:
            return False