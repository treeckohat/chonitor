op = float(input("What is the original price? "))
off = op * .2
fp = op - off
fp = round(fp, 2)
print(f"Sale price of ${fp}")