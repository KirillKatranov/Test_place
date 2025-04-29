n = int(input())
spisok_cash = []
for i in range(n):
    cash = int(input())
    spisok_cash.append(cash)

#1.Я беру одну комбинацию
 #1.1 Определить максимальную степень двойки, которая помещается в это число
 #1.2 Ограничить значения степеней этим числом
 #1.3 Завожу циклы: в первом цикле бегу от 0 до макс числа, во втором от 1 до макс числа, в третьем от 2 до макс числа
 # 1.4 Считаю сумму   
#Смотрю уникальна ли она
#Если уникальна, то считаю её сумму
#Проверяю полученную сумму
result_list = []
for cash in spisok_cash:
    max_stepen = 0
    res = 1
    while res < cash:
        res *= 2
        max_stepen += 1
    max_stepen -= 1

    curren_sum = 0
    max_sum = 0
    for i in range(max_stepen + 1):
        for j in range(1, max_stepen + 1):
            for k in range(2, max_stepen + 1):
                if i != j and i != k and k != j:
                    curren_sum = pow(2, i) + pow(2,j) + pow(2, k)
                    if curren_sum > max_sum and curren_sum <= cash:
                        max_sum = curren_sum
    if max_sum == 0:
        result_list.append(-1)
    else:
        result_list.append(max_sum)
                    
for result in result_list:
    print(result)