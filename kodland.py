meme_sozlugu = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SCAMMER": "Kandıran kişiye denir",
            "NP": "önemli değil ,birşey değil ",
            "TYSM": "Çok teşekkür ederim",
            }
kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if kelime in meme_sozlugu.keys():
    print("kelime sözlükte var")
else:
    print("kelime sözlükte yok")
