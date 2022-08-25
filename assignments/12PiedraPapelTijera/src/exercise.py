def main():
    # Escribe tu código abajo de esta línea
    ana= input('Ana, dame piedra(a) papel(p) o tijera (t)')
    juan=input('Juan, dame piedra(a) papel(p) o tijera (t)')
    if ana==juan:
        print('Empate')
    elif ana =='a' and juan=='t':
        print('Ana gana')
    elif ana == 'p' and juan == 'a':
        print('Ana gana')
    elif ana== 't' and juan== 'p':
        print('Ana gana')
    elif ana =='t' and juan=='a':
        print('Juan gana')
    elif ana =='a' and juan == 'p':
        print('Juan gana')
    elif ana== 'p' and juan== 't':
        print('juan gana')
    elif ana!=juan:
    print('los caracteres deben de ser a, p, t')
    
    


if __name__ == '__main__':
    main()
