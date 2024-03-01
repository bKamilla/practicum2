#practicum2

weightf = int(input("Введите вес в фунтах:"))
heightd = int(input("Введите высоту в дюймах:"))
heightm = 0.0254 * heightd
weightkg = weightf * 0.454
IMT = weightkg / (heightm * heightm)
print(round(IMT, 2))
