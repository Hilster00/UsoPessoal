import pdfkit

def html_pdf(html_file, pdf_file):
    try:
        pdfkit.from_file(html_file, pdf_file)
        print("HTML convertido para PDF com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao converter HTML para PDF: {e}")

