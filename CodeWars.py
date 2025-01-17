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



if __name__ == "__main__":
    pass