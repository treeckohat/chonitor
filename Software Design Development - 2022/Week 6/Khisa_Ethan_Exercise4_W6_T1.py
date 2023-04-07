def com(sale):
    sale_com = sale*.1
    return sale_com

n1 = input("Who is the first person? ")
s1 = int(input(f"How much did {n1} make? "))
n2 = input("Who is the second person? ")
s2 = int(input(f"How much did {n2} make? "))
n3 = input("Who is the third person? ")
s3 = int(input(f"How much did {n3} make? "))

sc1 = round(com(s1), 2)
sc2 = round(com(s2), 2)
sc3 = round(com(s3), 2)

com_dict = {n1:f"${sc1}", n2:f"${sc2}", n3:f"${sc3}"}
print(f"The total commisions of each of the salepeople are {com_dict}")