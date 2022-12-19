import time
start_time = time.time()

print("Hello")
print("World")
print("Hello world")

# ini komentar
"""ini adalah 
komen multiline
untuk memberi komentar di beberapa baris"""
kampret = 100 #ini komen bisa ditulis di belakang perintah
print(kampret)


print(time.time() - start_time, "detik")
# kita bisa mengcompile python ke
# yang namanya bytecode
# cara mengcompile, buka terminal dan ketik
# python3 -m py_compile main.py
