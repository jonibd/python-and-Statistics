from PyPDF2 import PdfMerger
All_pdf=["project/pdf1.pdf","project/pdf2.pdf"]

OurMerger = PdfMerger()

for New_Pdf in All_pdf:
    OurMerger.append(New_Pdf)

OurMerger.write("merge.pdf")

OurMerger.close()