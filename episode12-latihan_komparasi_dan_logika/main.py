# Episode latihan logika dan komparasi

# Membuat gabungan area rentang dari angka

# ++++++++++3--------10++++++++++

inputUser = float(input("masukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:"))


#++++++++++++3---------
isKurangDari = (inputUser < 3)
print ("kurang dari 3 =", isKurangDari)

#memeriksa lebih dari 10
#++++++++++++3---------
isLebihDari = (inputUser > 10)
print ("lebih dari 10 =", isLebihDari)

#+++++3-----------10+++++2

isCorrect = isKurangDari or isLebihDari
print ("angka yang anda masukkan:", isCorrect)


#-----3+++++++++10-----
#kasus irisan
print ("\n",10*"=","\n")
inputUser = float(input("masukkan angka yang bernilai\nlebih dari dari 3\ndan \nkurang besar dari 10\n:"))

#-----3++++++
# lebih dari 3
isLebihDari =  inputUser > 3 
print ("Lebih dari 3 = ",isLebihDari)

#++++++10-----
# kurang dari 10
isKurangDari = inputUser < 10
print ("Kurang dari 10 = ",isKurangDari)

#-----3+++++++++10-----
isCorrect = isKurangDari and isLebihDari
print ("angka yang anda masukkan:", isCorrect)


#PR 1 ----0++++5----8++++11----

#-----0+++++5-----8++++11-----
#kasus irisan
print ("\n",10*"=","\n")
inputUser = float(input("masukkan angka yang bernilai\nlebih dari dari 0 \nkurang besar dari 5\nserta \nlebih dari 8 \nkurang dari 11 \n:"))

#-----0++++++
# lebih dari 0
isLebihDariA =  inputUser > 0 
print ("Lebih dari 0 = ",isLebihDariA)

#++++++5-----
# kurang dari 5
isKurangDariA = inputUser < 5
print ("Kurang dari 5 = ",isKurangDariA)

#-----8++++++
# lebih dari 8
isLebihDariB =  inputUser > 8 
print ("Lebih dari 8 = ",isLebihDariB)

#++++++11-----
# kurang dari 11
isKurangDariB = inputUser < 11
print ("Kurang dari 11 = ",isKurangDariB)

#-----0++++5----8+++++11-----
isCorrect = isKurangDariA and isLebihDariA or isKurangDariB and isLebihDariB
print ("angka yang anda masukkan:", isCorrect)


#PR 2 ++++0-----5+++++8------11+++++

#++++0-----5+++++8------11+++++
#kasus irisan
print ("\n",10*"=","\n")
inputUser = float(input("masukkan angka yang bernilai\nkurang dari 0 \nlebih besar dari 5\nserta \nkurang 8 \nlebih dari 11 \n:"))

#++++++0-------
# kurang dari 0
isKurangDariA =  inputUser < 0 
print ("Kurang Dari 0 = ",isKurangDariA)

#-----5+++++
# lebih dari 5
isLebihDariA = inputUser > 5
print ("Lebih dari 5 = ",isLebihDariA)

#+++++8-------
# kurang dari 8
isKurangDariB =  inputUser < 8 
print ("Kurang dari 8 = ",isKurangDariB)

#-----11+++++
# Lebih dari 11
isLebihDariB = inputUser > 11
print ("Lebih dari 11 = ",isLebihDariB)

#++++0-----5+++++8------11+++++
isCorrect = isLebihDariA or isKurangDariA or isLebihDariB or isKurangDariB
print ("angka yang anda masukkan:", isCorrect)
