h = 168
w = 69.5
try:
    bmi = w / (h / 100) ** 2
    if bmi < 18 or bmi > 23:
        raise Exception('BMI 不合格:' + str(bmi))
except Exception as e:
    print(e)
else:
    print(bmi)
