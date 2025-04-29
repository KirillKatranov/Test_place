n, m = input().split()
n = int(n)
m = int(m)


days = []
days_str = input().split()
days = [int(item) for item in days_str]


day1 = days[0]
day2 = days[1]



list_difference = []
count_good_day = 0
for day in days[2:]:
    if count_good_day < m:
        if day in range(day1, day2 + 1):
            count_good_day += 1
        elif day < day1:
            list_difference.append(day1 - day)
        elif day > day2:
            list_difference.append(day - day2)

correctirovka = 0 
while count_good_day < m:
    correctirovka += min(list_difference)
    count_good_day += 1

print(correctirovka)




    
