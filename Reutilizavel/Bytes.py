def bytes_da_string(texto):
    bytes_str = [repr(char) for char in texto]
    return ', '.join(bytes_str)

if __name__=="__main__":
  texto = "Olá, mundo!"
  print(f"Bytes da string \" {texto} \": {bytes_da_string(texto)}")
