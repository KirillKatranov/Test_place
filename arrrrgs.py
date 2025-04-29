#Позиционные аргументы не могут стоять после kwargs аргументов



def my_print(a, *args, **kwargs):
    print(args)
    print(a)
    b += "1"
    print(b)
    print(c)
    #print(kwargs)
    #print(**kwargs)


if __name__ == "__main__":
    a, b, c  = "ab", "bc", "cd"
    my_print()
    #print(c)

