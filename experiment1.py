import pathlib
import requests
import datetime
import pytz
from bs4 import BeautifulSoup
import os
import time
import pandas as pd
import time
from PIL import ImageGrab
from selenium import webdriver
from PIL import Image

#ImageGrab.grab().save(r'C:\Users\mizun\OneDrive\MyPythonProject\image_folder\SNOWAD.jpg')
filename=r"C:\Users\mizun\OneDrive\MyPythonProject\image_folder\SNOWAD.jpg"

imagefile = Image.open(filename)
imagefile = imagefile.crop((0, 178, 2729, 1720))
imagefile.save(filename)