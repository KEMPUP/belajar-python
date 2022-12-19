# belajar Casting
# merubah dari sati tipe ke tipe lain
# tipe data = int, float, str, bool

## INTEGER
print("===integer===")
data_int = 9
print("data = ", data_int, ",type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0
print("data = ", data_float, ",type = ", type(data_float))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))

## FLOAT
print("===float===")
data_float = 9.5
print("data = ", data_float, ",type = ", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai int = 0
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))

## BOOLEAN
print("===boolean===")
data_bool = True
print("data = ", data_bool, ",type = ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) 
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_float, ",type = ", type(data_float))

## STRING
print("===string===")
data_str = "10"
print("data = ", data_str, ",type = ", type(data_str))

data_int = int(data_str) #string harus angka, apabila karakter huruf pasti error
data_bool = bool(data_str) #akan false jika nilai str = 0
data_float = float(data_str) #string harus angka, apabila karakter huruf pasti error
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_bool, ",type = ", type(data_bool))
print("data = ", data_float, ",type = ", type(data_float))