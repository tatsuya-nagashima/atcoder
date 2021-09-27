from decimal import Decimal,ROUND_HALF_UP
X = input()
a = Decimal(str(X))
b = a.quantize(Decimal('0'), rounding=ROUND_HALF_UP)
print(b)