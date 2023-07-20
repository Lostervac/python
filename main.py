meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
            
if word in meme_dict.keys():
    print("o kelimenin anlamı bu", meme_dict[word])
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("bu sözlükte aradığınız kelime yok,").
