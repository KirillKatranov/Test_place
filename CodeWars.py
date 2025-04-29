from math import isqrt, sqrt


def digitize(n):
    return [symbol for symbol in reversed(str(n))]


def remove_char(s):
    return s[1:-1:]


def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


def dna_to_rna(dna: str):
    return dna.replace("T", "U")


def sum_array(a):
    return sum(a,5)


def string_to_array(string: str):
    return string.split(" ")


def abbrev_name(name: str):
    name1, surname = name.split(" ")  
    return f"{name1[0].upper()}.{surname[0].upper()}"
    

def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()


def no_space(x: str):
    return x.replace(" ", "")


def make_negative( number: int ):  
    return int("".join(["-", str(number)])) if str(number)[0] != "-" else int(number)


def make_negative( number ):
    return -abs(number)


def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo" 
    

def summation(num):
    return sum(range(1, num + 1))


def printer_error(s):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    count = 0
    for symbol in s:
        if symbol not in alphabet:
            count += 1
    return f"{count}/{len(s)}"
            

def my_find_short(s: str)-> int:
    list_string = s.split(" ")
    l = min(list_string, key=len)
    return l # l: shortest word length

def pro_find_short(s):#Лучше
    return min(len(x) for x in s.split())


def find_next_square(sq: int):
    # Return the next square if sq is a square, -1 otherwise
    sqrt_n = isqrt(sq)
    if pow(sqrt_n, 2) == sq:
        return pow(sqrt_n + 1, 2)
    else:
        return -1


def my_xo(s: str) -> bool:
    x_count = 0
    o_count = 0
    for symbol in s:
        if symbol.lower() == 'x':
            x_count += 1
        elif symbol.lower() == 'o':
            o_count += 1
    return x_count == o_count 
        

def pro_xo(s:str):
    s = s.lower()
    return s.count('x') == s.count('o')




def validate_pin(pin: str) -> bool:
    #Валидация произвольной строки, должно быть строка из 4 или 6 целых чисел
    if pin.isdigit():
        return len(pin) == 4 or len(pin) == 6
    else:
        return False


def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())


def number(bus_stops):
    people_in_buss = 0
    people_out_buss = 0
    for station in bus_stops:
        people_in_buss += station[0]
        people_out_buss += station[1]
    return people_in_buss - people_out_buss


def get_middle(s: str) -> str:
    if len(s) % 2:
        return s[len(s) // 2]
    else: 
        return s[(len(s) // 2) - 1] + s[(len(s)) // 2]


def remove_exclamation_marks(s: str) -> str:
    return s.replace('!', "")

def find_average(numbers: list) -> float:
    return sum(numbers)/len(numbers) if numbers else 0


def get_count(sentence):
    return sum([s for s in sentence.split() if s in ['a', 'e', 'i', 'o', 'u']])

def solution(string: str) -> str:
    return str(s for s in reversed(string))

def square_digits(num: int):
    return str([i*i for i in map(int, str(num))])

def sum_two_smallest_numbers(numbers: list):
    a = min(numbers)
    numbers.remove(a)
    b = min(numbers)
    numbers.remove(a)
    return a + b


def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

def likes(names):
    if not len(names):
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} like this"
    
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
    
def two_sum(numbers, target):
    for i in range(len(numbers) - 1):
        for j in range(1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
	


if __name__ == "__main__":
    find_even_index([1,2,3])
   
