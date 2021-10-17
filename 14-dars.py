#                                   14- dars dictionary Lugat


# #otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida
# # kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). 
# #Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 
# # 1954-yilda, Samarqand viloyatida tug'ilgan

opam = {
        'ismi': 'muborak',
        't_yil': 1993,
        'shaxri': 'Tashkent'
        
        }
t_yil =opam['t_yil']
shax = opam['shaxri']

print(f"Opamning ismi {opam['ismi'].title()}, {t_yil}-yilda, {shax.title()} shaxrfda tugilgan")


# #Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom 
 # #jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining 
 # #sevimli taomi osh
 
taomlar = {
    'ali': "osh",
    'vali': "lavash",
    'kali': "xonim",
    "boltavoy": 'shorva',
    'teshavoy': 'makaron'
    
    }

taom = taomlar['teshavoy']
print(f'Teshavoy yaxshi koradigan ovqat {taom}')

## Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani)
# # kiriting (masalan integer, float, string, if, else va hokazo) va har birining 
# # tarjimasini yozing.


modellar = {
    'samsung': 'A52',
    'iphone': '13 pro max',
    'redmi': 'mi 56 pro',
    'nokia': '6303',
    'artel': '12 pro max',
    
    }

kalit = input("Modelingizni tanlang: ")
malumot = modellar.get(kalit)
if malumot == None:
    print("Bunday Model yo'q")

else:
    print(f"{kalit.title()} bu siz tanlagan {malumot} Modelni oxirgilaridan")

































