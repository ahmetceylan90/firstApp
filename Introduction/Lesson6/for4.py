for i in range(3):
    sifre = input("şifre giriniz : ")
    
    if i == 2:
        print("3 kere yanlış gridniz")
    elif not sifre:
        print("şifreyi boş geçemezsiniz")
    elif len(sifre) in range(3,8):
        print("başarılı şekilde oluşturdunuz")
        break
