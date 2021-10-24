from openpyxl import load_workbook
import pathlib
from openpyxl.drawing.image import Image
import qrcode

fp_xlsx=r'C:\Users\mizun\OneDrive\MyPythonProject\scraping_practice01.xlsx'
wb=load_workbook(fp_xlsx)
ws=wb.active

fp=pathlib.Path(r'png_image\download.jfif')#any ongg file will do (dummy)
size=(100,100)

for i,record in enumerate(ws.values):
    if i ==0:continue

    url=record[1]
    image=qrcode.make(url).resize(size)
    image.save(fp)

    image=Image(fp)
    row=i+1
    ws.add_image(image,f'D{row}')#select the row   EX)E{row}

wb.save(fp_xlsx)
fp.unlink#delete the dummy png