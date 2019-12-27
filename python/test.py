
from matplotlib.font_manager import fontManager  
import os 
fonts = [font.name for font in fontManager.ttflist if os.path.exists(font.fname) and os.stat(font.fname).st_size>1e6]  
for font in fonts:  
    print(font)