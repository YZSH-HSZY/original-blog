import pypdf as pd

with open(
    r"D:\book\school_paper\format\11075_080901_2016112132_46_徐雅琦.pdf",
    'rb') as f:
    pdf = pd.PdfReader(f)
    all_text = [pdf.pages[i].extract_text() 
                for i in range(len(pdf.pages))]
    
    all_text = ''.join(all_text)
    print(len(all_text))