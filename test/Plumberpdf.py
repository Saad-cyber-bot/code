import tabula
import pandas as pd
import pdfplumber
import re

re_value = "TOTAL NET PRICE"

with pdfplumber.open("SE-NSJ-PRT-010@itab.com_20241022_135529.pdf") as pdf_file:
    pages = pdf_file.pages
    for page in pages:
        print(page)
        for line in page.extract_text().split("\n"):
            if re.search(re_value, line):
                print("".join(line.split()[5:]))
            #print(line)


