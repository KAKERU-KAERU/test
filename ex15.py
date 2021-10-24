from PyPDF2 import PdfFileWriter,PdfFileReader
from PyPDF2.pdf import PageObject

write=PdfFileWriter()
read=PdfFileReader(r'C:\Users\mizun\OneDrive\MyPythonProject\PDF\2122Jones_catalog.pdf',strict=False)

for i in range(0,64):
    p1=2*i
    page1=read.getPage(p1)
    width=page1.mediaBox.getWidth()
    height=page1.mediaBox.getHeight()
    new_page=PageObject.createBlankPage(width=width*2,height=height)

    new_page.mergePage(page1)

    p2=2*i+1
    page2=read.getPage(p2)
    new_page.mergeRotatedScaledTranslatedPage(page2,rotation=0,scale=1,tx=width,ty=0)

    write.addPage(new_page)

with open(r'ex4.pdf','wb') as f:
    write.write(f)
