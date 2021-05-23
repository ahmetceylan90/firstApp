def jsonVeriEkle():
    from datetime import date
    personeller = [
    {
        "first": "Caesar",
        "last": "Ferry",
        "email": "Caesar.Ferry@nasir.com",
        "address": "67473 Reinhold Burg",
        "created": "October 14, 2013",
        "balance": "$1,980.53",
        "phones": [
            {
                "key": "gsm",
                "value": "055555555",
                "desc": "mobile"
            },
            {
                "key": "home",
                "value": "12344567788",
                "desc": "home phone"
            }
        ]

    }
    ]

    # Dışardan girdiğimiz değerleri personele ekle

    first = input("first")
    last = input("last")
    email = input("email")
    address = input("adres")
    balance = input("balance")


    personeller.append( 
    {"first": first,
     "last": last,
     "email": email,
     "address": address,
     "created": date.today(),
     "balance": balance
     }
    )

    print(personeller)

 


