Nama = "Altarik Saputra"
Nim = 26241097
a = int(input("Digit A: "))
b = int(input("Digit B: "))

digit1 = a >= 5
digit2 = b >= 5

print("Masukan Nama:", Nama)
print("Masukan NIM:", Nim)
print("Kondisi 1:", digit1)
print("Kondisi 2:", digit2)
print("============Hasil============")
print("NOT:", not digit1)
print("AND", digit1 and digit2)
print("OR:", digit1 or digit2)
print("XOR:", digit1 ^ digit2)
