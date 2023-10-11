import math

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# def distance(x1, y1, x2, y2):
# dx = x2 - x1
#  dy = y2 - y1
#   return math.sqrt(dx**2 + dy**2)
# print(distance(x1, x2, y1, y2))


# a = float(input())
# n = int(input())
# def power(a, n):
#   if n == 0:
#        return 1
#   result = 1
#  abs_n = abs(n)
# for i in range(abs_n):
#    result *= a
# if n < 0:
#    return 1 / result
# else:
#    return result
# print(f"{a}^{n} = {power(a, n)}")

#n = int(input())
#def fin(n):
#    if n <= 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return fin(n - 1) + fin(n - 2)
#print(fin(n))

#def is_year_leap(a):
#    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
#        return True
#    else:
#        return False
#a = int(input("Введите год: "))
#print(is_year_leap(a))

#a = int(input())
#def square(a):
#    per = 4 * a
#    plo = a * a
#    x = 2
#    square_root = math.sqrt(x)
#    diag = a * x
#    return per, plo, diag
#print(square(a))

#a = int(input("Введите номер месяца: "))
#def season(a):
#    if a <= 2 or a == 12:
#         return "Зима"
#    elif a > 2 and a < 6:
#         return "Весна"
#    elif a >= 6 and a < 9:
#         return "Лето"
#    else:
#         return "Осень"
#print(season(a))


#def vklad():
#    years = int(input("Введите на какой срок(год):"))
#    a = int(input("Сколько рублей хотите вложить?: "))
#    for i in range(years):
#        pro = a / 10
#        a = a + pro
#    return a
#print(vklad())

#def is_prime():
#    num = int(input())
#    if num <= 1:
#        trfa = False
#    else:
#        trfa = True
#        for i in range(2, int(num ** 0.5) + 1):
#            if num % i == 0:
#                trfa = False
#    if trfa:
#        return True
#    else:
#        return False
#print(is_prime())

day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

def is_valid_date(day, month, year):
    if year < 1 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        days_in_month[2] = 29
    if day < 1 or day > days_in_month[month]:
        return False
    return True
if is_valid_date(day, month, year):
    print("Дата существует в календаре.")
else:
    print("Дата не существует в календаре.")