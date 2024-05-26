num = int(input("أدخل الرقم الذي تريد حساب ضربه التراكمي له: "))

factorial = 1
for i in range(1, num+1):
    factorial = factorial * i

print(f"الضرب التراكمي لـ {num} هو: {factorial}")
