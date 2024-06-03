import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }
            
for i in range(5):
    time.sleep(0.6)
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    time.sleep(0.3)
    
    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(meme_dict[word])
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print("No se encuentra la palabra")
