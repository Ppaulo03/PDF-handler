import sys
import PyPDF2


def verify_pdf(pdfs):
    input = []
    for item in pdfs:
        try:
            with open(item, 'rb') as file:
                reader = PyPDF2.PdfFileReader(file)
            input.append(item)
        except FileNotFoundError:
            print(f'{item} não encontrado')
        except PyPDF2.utils.PdfReadError:
            print(f'{item} não é um PDF ou está corrompido')
        except IsADirectoryError:
            print(f'Não foi possivel acessar {item} pois é um diretório')
    return input


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')


input = verify_pdf(sys.argv[1:])
pdf_merger(input)
