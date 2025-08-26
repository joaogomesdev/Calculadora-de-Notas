print("")
print("Seja muito bem vindo(a) à Calculadora de Notas!")
print("")
print("Aqui você terá acesso à dispositivos que pode te ajudar com as suas notas")
input("Para iniciar aperte [ENTER]")
print("")
print("Antes de iniciarmos, esse software é exclusivo para alunos que estão na ESCOLA.")
print("Para os alunos de faculdade, esse sistema não funciona")
print("Futuramente lançaremos um sistema para alunos de faculdade")
print("")
input("Aperte [ENTER] para continuar")
print("")
print("Em qual bimestre você está nesse momento? ")
bim = input("> ")
if bim == "4":
    print("Vamos começar pelo primeiro bimestre")
    a = float(input("Digite a primeira nota do primeiro bimestre: "))
    b = float(input("Digite a segunda nota do primeiro bimestre: "))
    print("")
    print("Vamos calcular agora o segundo bimestre")
    c = float(input("Digite aqui a primeira nota do segundo bimestre: "))
    d = float(input("Digite aqui a segunda nota do segundo bimestre: "))
    print("")
    print("Vamos calcular agora o terceiro bimestre")
    e = float(input("Digite aqui a primeira nota do terceiro bimestre: "))
    f = float(input("Digite aqui a segunda nota do terceiro bimestre: "))
    print("")
    print("Vamos calcular agora o quarto bimestre")
    g = float(input("Digite aqui a primeira nota do quarto bimestre: "))
    h = float(input("Digite aqui a segunda nota do quarto bimestre: "))
    m1b = (a + b)/2
    m2b = (c + d)/2
    m3b = (e + f)/2
    m4b = (g + h)/2
    mt = (m1b + m2b + m3b + m4b)/4
    print("")
    print("A sua média do primeiro bimestre foi: [", m1b ,"]")
    print("A sua média do primeiro bimestre foi: [", m2b ,"]")
    print("A sua média do primeiro bimestre foi: [", m3b ,"]")
    print("A sua média do primeiro bimestre foi: [", m4b ,"]")
    print("")
    print("A sua média esse ano foi: [", mt ,"]")
    print("")
    if m1b < 7:
        m1b7 = 7 - m1b
        print("No primeiro bimestre você precisa de [", m1b7 ,"] pontos para ficar acima da média")
    else:
        print("No primeiro bimestre você está acima da média!")
    if m2b < 7:
        m2b7 = 7 - m2b
        print("No segundo bimestre você precisa de [", m2b7 ,"] pontos para ficar acima da média")
    else:
        print("No segundo bimestre você está acima da média!")
    if m3b < 7:
        m3b7 = 7 - m3b
        print("No terceiro bimestre você precisa de [", m3b7 ,"] pontos para ficar acima da média")
    else:
        print("No terceiro bimestre você está acima da média!")
    if m4b < 7:
        m4b7 = 7 - m4b
        print("No quarto bimestre você precisa de [", m4b7 ,"] pontos para ficar acima da média")
    else:
        print("No quarto bimestre você está acima da média!")
    if mt < 28:
        print("Infelizmente a sua média foi menor que a média para passar. Você provavelmente ficará de recuperação")
    else:
        print("A sua nota foi maior que a média necessária para passar de ano. Parabéns, você passou de ano!")
elif bim == "3":
    print("Vamos começar pelo primeiro bimestre")
    a = float(input("Digite a primeira nota do primeiro bimestre: "))
    b = float(input("Digite a segunda nota do primeiro bimestre: "))
    print("")
    print("Vamos calcular agora o segundo bimestre")
    c = float(input("Digite aqui a primeira nota do segundo bimestre: "))
    d = float(input("Digite aqui a segunda nota do segundo bimestre: "))
    print("")
    print("Vamos calcular agora o terceiro bimestre")
    e = float(input("Digite aqui a primeira nota do terceiro bimestre: "))
    f = float(input("Digite aqui a segunda nota do terceiro bimestre: "))
    print("")
    m1b = (a + b)/2
    m2b = (c + d)/2
    m3b = (e + f)/2
    mt = (m1b + m2b + m3b)/3
    print("")
    print("A sua média do primeiro bimestre foi: [", m1b ,"]")
    print("A sua média do primeiro bimestre foi: [", m2b ,"]")
    print("A sua média do primeiro bimestre foi: [", m3b ,"]")
    print("")
    print("A sua média esse ano atualmente é: [", mt ,"]")
    print("")
    if m1b < 7:
        m1b7 = 7 - m1b
        print("No primeiro bimestre você precisa de [", m1b7 ,"] pontos para ficar acima da média")
    else:
        print("No primeiro bimestre você está acima da média!")
    if m2b < 7:
        m2b7 = 7 - m2b
        print("No segundo bimestre você precisa de [", m2b7 ,"] pontos para ficar acima da média")
    else:
        print("No segundo bimestre você está acima da média!")
    if m3b < 7:
        m3b7 = 7 - m3b
        print("No terceiro bimestre você precisa de [", m3b7 ,"] pontos para ficar acima da média")
    else:
        print("No terceiro bimestre você está acima da média!")
elif bim == "2":
    print("Vamos começar pelo primeiro bimestre")
    a = float(input("Digite a primeira nota do primeiro bimestre: "))
    b = float(input("Digite a segunda nota do primeiro bimestre: "))
    print("")
    print("Vamos calcular agora o segundo bimestre")
    c = float(input("Digite aqui a primeira nota do segundo bimestre: "))
    d = float(input("Digite aqui a segunda nota do segundo bimestre: "))
    print("")
    m1b = (a + b)/2
    m2b = (c + d)/2
    mt = (m1b + m2b)/2
    print("")
    print("A sua média do primeiro bimestre foi: [", m1b ,"]")
    print("A sua média do primeiro bimestre foi: [", m2b ,"]")
    print("")
    print("A sua média esse ano atualmente é: [", mt ,"]")
    print("")
    if m1b < 7:
        m1b7 = 7 - m1b
        print("No primeiro bimestre você precisa de [", m1b7 ,"] pontos para ficar acima da média")
    else:
        print("No primeiro bimestre você está acima da média!")
    if m2b < 7:
        m2b7 = 7 - m2b
        print("No segundo bimestre você precisa de [", m2b7 ,"] pontos para ficar acima da média")
    else:
        print("No segundo bimestre você está acima da média!")
elif bim == "1":
    print("Vamos começar pelo primeiro bimestre")
    a = float(input("Digite a primeira nota do primeiro bimestre: "))
    b = float(input("Digite a segunda nota do primeiro bimestre: "))
    print("")
    m1b = (a + b) / 2
    mt = (m1b)/2
    print("")
    print("A sua média do primeiro bimestre foi: [", m1b ,"]")
    print("")
    print("A sua média esse ano atualmente é: [", mt ,"]")
    print("")
    if m1b < 7:
        m1b7 = 7 - m1b
        print("No primeiro bimestre você precisa de [", m1b7 ,"] pontos para ficar acima da média")
    else:
        print("No primeiro bimestre você está acima da média!")
else:
    print("Esse bimestre não existe. Tente novamente mais tarde!")