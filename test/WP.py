import pandas as pd


def clean_text(text):
    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return cleaned_lines


def split_line_to_columns(line):
 
    parts = line.split()
    
 
    print(f"Processing Line: {line}")
    print(f"Split Parts: {parts} (Length: {len(parts)})")
    
    if len(parts) == 9:
        number = parts[1]
        hs_code = parts[2]
        quantity = parts[3].replace(",", ".")
        net_weight = parts[4].replace(",", ".")
        gross_weight = parts[5].replace(",", ".")
        value = parts[6].replace(",", ".")
        invoice_number = parts[7]
        country = parts[8]
        return number, hs_code, quantity, net_weight, gross_weight, value, invoice_number, country
    else:
        return None, None, None, None, None, None, None, None  


pdf_text = """
PLATE N
OUTPUT
Number    12NC HS CODE Quantity Net Weight Gross WeightValue Invoice
(NO VAT) NOKInvoice numercountry of
origin
1 869991581640 85166050 1.000 9.300 11.200 3.119,20 4637007827 IT
2 869991609380 84184080 1.000 89.000 91.816 3.880,08 4637007824 TR
3 859991560710 85166080 1.000 33.000 35.000 3.279,20 4637007829 IT
4 859991560710 85166080 1.000 33.000 35.000 3.279,20 4637007830 IT
5 859991671020 84182199 1.000 50.000 52.000 3.515,63 4637007825 IT
6 869991641850 84501111 1.000 75.900 77.400 2.439,31 4637007826 IT
7 859991560710 85166080 1.000 33.000 35.000 3.279,20 4637007831 IT
8 859991613710 84181080 1.000 57.000 59.000 4.019,23 4637007822 IT
9 859991659950 85166080 1.000 26.900 28.200 3.599,20 4637007828 PL
10 859991659990 85166080 1.000 27.550 28.850 3.469,66 4637007823 PL
11 869991581640 85166050 1.000 9.300 10.300 2.949,12 4637007823 IT
12 869991663290 84221100 1.000 35.500 37.500 3.748,47 4637007823 PL
"""


cleaned_lines = clean_text(pdf_text)


data = []
for line in cleaned_lines:
    
    if "12NC" in line or "PLATE" in line or "origin" in line or "OUTPUT" in line:
        continue
    
    
    number, hs_code, quantity, net_weight, gross_weight, value, invoice_number, country = split_line_to_columns(line)
    
    
    if number and hs_code and quantity and net_weight and gross_weight and value and invoice_number and country:
        data.append([number, hs_code, quantity, net_weight, gross_weight, value, invoice_number, country])


if data:
    df = pd.DataFrame(data, columns=["Number", "HS Code", "Quantity", "Net Weight", "Gross Weight", "Value", "Invoice Number", "Country"])
    
    
    output_filename = "output_data.xlsx"
    df.to_excel(output_filename, index=False)
    print(f"Data has been successfully written to '{output_filename}'.")
else:
    print("No valid data found to be written.")
