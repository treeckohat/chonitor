n = int(input("Limit? "))
count = int(1)
x = "true"
sqlist = []
while x == "true":
    sq = count*count
    if sq <= n:
        sqlist.append(sq)
    if sq > n:
        x = "false"
    count = count+1
print(f"The square numbers less than or equal to to {n} are {sqlist}")