import pyautogui as pag
import pandas as pd

pag.PAUSE = 2.0

pag.press("win")
pag.write("google")
pag.press("enter")
pag.write("ola mundo")
pag.press("enter")
pag.click(x=358, y=328)