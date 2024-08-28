import glob
import os
import pypdf
from tqdm import tqdm

if __name__ =="__main__":
    current_dir = os.path.abspath(os.path.dirname(__file__))
    all_pdf = glob.glob(os.path.join(current_dir, '*.pdf'))
    all_pdf = list(
        filter(
            lambda x:os.path.splitext(os.path.basename(x))[0].isnumeric(), 
            all_pdf))
    all_pdf.sort(key=lambda x:int(os.path.splitext(os.path.basename(x))[0]))
    assert len(all_pdf) != 0

    output_pdf = pypdf.PdfWriter()
    for _ in tqdm(all_pdf, desc='合并pdf'):
        input_pdf = pypdf.PdfReader(
            stream=open(_, 'rb'))
        for i in range(len(input_pdf.pages)):
            output_pdf.insert_page(
                input_pdf.pages[i], 
                index=len(output_pdf.pages)
            )
    output_pdf.write(open('merge.pdf', 'wb'))
    output_pdf.close()