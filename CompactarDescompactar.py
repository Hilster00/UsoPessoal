import zipfile
import os

def compactar_com_senha(pasta_para_compactar, destino_zip, senha):
    with zipfile.ZipFile(destino_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for raiz, _, arquivos in os.walk(pasta_para_compactar):
            for arquivo in arquivos:
                zipf.write(os.path.join(raiz, arquivo), os.path.relpath(os.path.join(raiz, arquivo), pasta_para_compactar))
    with open(destino_zip, 'rb') as f:
        zip_data = f.read()
        with zipfile.ZipFile(destino_zip, 'a', compression=zipfile.ZIP_DEFLATED) as zf:
            zf.setpassword(bytes(senha, 'utf-8'))
    os.remove(destino_zip)


def descompactar_com_senha(arquivo_zip, destino, senha):
    try:
        with zipfile.ZipFile(arquivo_zip) as zf:
            zf.extractall(path=destino, pwd=bytes(senha, 'utf-8'))
        print('Descompactado com sucesso!')
    except Exception as e:
        print(f'Erro ao descompactar: {e}')


pasta_para_compactar = 'caminho/para/sua/pasta'
destino_zip = 'caminho/para/sua/pasta.zip'
destino = 'caminho/para/descompactar'
senha = 'sua_senha'


compactar_com_senha(pasta_para_compactar, destino_zip, senha)
descompactar_com_senha(arquivo_zip, destino, senha)
