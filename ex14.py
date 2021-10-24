from PyPDF2 import PdfFileMerger
from PyPDF2.pagerange import PageRange

def split(base_file,pages,splited_file):
    merger=PdfFileMerger()
    merger.append(base_file,pages=pages)
    merger.write(splited_file)
    merger.close()

source=r'PDF\a1.pdf'
split(source,PageRange(':128'),r'x1.pdf')#set the page and filename1
split(source,PageRange('128:'),r'x2.pdf')#set the page and filename2

