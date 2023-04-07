data = "ini adalah string"
print (data)
print (type(data))

#cara membuat string

#1. cara membuat string

'''
    1. dengan menggunakan single quote ''
    2. dengan menggunakan double quote ""
'''

data = 'menggunakan single quote'
print (data)

data = "menggunakan double quote"
print (data)

print ('"Halo, apa kabar?"')
print ("'Halo, apa kabar?'")
print ("ini adalah hari jum'at")

#2. Menggunakan tanda \

#membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day isn\'t it?')

#backlash
print('C:\\user\\ucup')

#tab
print('ucup \t\t\totong, jadi semakin jauh')

#backspace
print('ucup \botong, semakin deketan')

#newline
print("baris pertama. \nbaris kedua.") #LF -> Line feed
print("baris pertama. \rbaris kedua.") #CR -> Carriage return
print("baris pertama. \r\nbaris kedua.") #CR -> Carriage return line feed

#3. String literal atau raw

#hati-hati
print('C:\new folder') #pathnya akan salah

#menggunakan raw string
print(r'c:\new \t \b folder') #semua akan dianggap string

#Multiline literal string
print("""
Nama: ucup
kelas: 3 SD 
""")

#Multiline literal string dan RAW
print(r"""
Nama: ucup
kelas: 3 SD\new normal
website: www.ucup.com/newID 
""")