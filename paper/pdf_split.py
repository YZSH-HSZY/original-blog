import os
from pypdf import PdfWriter, PdfReader
from tqdm import tqdm

split_src_pdf = 'A constant-time SLAM back-end in the continuum between global mapping and submapping application to visual stereo SLAM.pdf'

output_dir = r'output_split_3'
os.makedirs(output_dir, exist_ok=True)

with open(split_src_pdf, 'rb') as read_f:
    src_pdf = PdfReader(read_f)
    for _ in tqdm(range(len(src_pdf.pages)),desc='pdf分割'):
        a_page_output_name = os.path.join(output_dir, str(_) + '.pdf')
        
        a_page_output_pdf = PdfWriter()
        a_page_output_pdf.insert_page(src_pdf.pages[_])
        a_page_output_pdf.write(
            open(a_page_output_name, 'wb')
        )
        a_page_output_pdf.close()

