def elem_ord(l):
    '''
    Determina daca o lista este ordonata crescator
    :param l: lista de numere
    :return: True daca este sau False daca nu
    '''
    for x in range(len(l)-1):
        for y in range(x+1, len(l)):
            if l[y] < l[x]:
                return False
    return True


def test_elem_ord():
    assert elem_ord([]) is True
    assert elem_ord([2, 5, 6]) is True
    assert elem_ord([3, 4, 1]) is False


def get_longest_sorted_asc(l):
    '''
    Determina cea mai lunga subsecventa ordonata cresc
    :param l: lista
    :return: cea mai lunga subsecventa
    '''
    subsecventa_Max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if elem_ord(l[i:j+1]) and len(l[i:j+1]) > len(subsecventa_Max):
                subsecventa_Max = l[i:j+1]
    return subsecventa_Max


def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([]) == []
    assert get_longest_sorted_asc([2]) == [2]


def nr_div(n):
    '''
    Determina numarul de divizori ai unui numar dat n
    :param n: numarul n dat
    :return: numarul de divizori
    '''
    nrd = 0
    for d in range(1, n+1):
         if n % d == 0:
            nrd += 1
    return nrd


def test_nr_div():
    assert nr_div(0) == 0
    assert nr_div(10) == 4
    assert nr_div(13) == 2
    assert nr_div(19) == 2


def get_longest_same_div_count(l):
    '''
    Determina cea mai lunga subsecventa cu toate numerele cu aceelasi numar de divizori
    :param l: lista de numere
    :return: cea mai lunga subsecventa
    '''
    subsecventa_Max = []
    ok = 1
    for i in range(len(l)-1):
        ok = 1
        for j in range(i+1, len(l)):
            if nr_div(l[i]) == nr_div(l[j]):
                if ok == 1 and len(l[i:j+1]) > len(subsecventa_Max):
                    subsecventa_Max = l[i:j+1]
            else:
                ok = 0
    return subsecventa_Max
# 18, 12, 6, 3, 19, 17, 20


def test_get_longest_same():
    assert get_longest_same_div_count([]) == []
    assert get_longest_same_div_count([5, 11, 10, 20]) == [5, 11]
    assert get_longest_same_div_count([18, 12, 6, 3, 19, 17, 20]) == [3, 19, 17]


def prim(x):
    '''
    Determina daca un numar este prim
    :param x: un numar intreg
    :return: True, daca x este prim sau False daca nu este
    '''
    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def test_prim():
    assert prim(-1) is False
    assert prim(0) is False
    assert prim(1) is False
    assert prim(2) is True
    assert prim(4) is False
    assert prim(5) is True


def toate_elem_nr_prime(l):
    '''
    Determina daca toate elemente dintr-o lista sunt prime
    :param l: lista de elemente
    :return: True daca toate sunt prime sau False daca nu sunt
    '''
    for x in l:
        if prim(x) == 0:
            return False
    return True


def test_toate_elem_nr_prime():
    assert toate_elem_nr_prime([]) is True
    assert toate_elem_nr_prime([3,5,7]) is True
    assert toate_elem_nr_prime([7,1,4]) is False


def get_longest_all_primes(l):
    '''
    Determina cea mai lunga subsecventa cu toate elementele numere prime
    :param l: lista de numere
    :return: cea mai lunga subsecventa de numere prime
    '''
    subsecventa_Max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if toate_elem_nr_prime(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_Max):
                subsecventa_Max = l[i:j + 1]
    return subsecventa_Max

def test_get_longest_all_primes():
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([4,6,9]) == []
    assert get_longest_all_primes([3,4,5]) == [3]
    assert get_longest_all_primes([9,7,11,17,10]) == [7,11,17]


def citireLista():
    l = []
    stringdat = input("Dati elemente pentru lista separate prin virgula: ")
    elementestring = stringdat.split(",")
    for x in elementestring:
        l.append(int(x))
    return l


def printMenu():
    print("1. Citire date")
    print("2. Determinare cea mai lungă subsecvență cu elementele ordonate cresc")
    print("3. Determinare cea mai lungă subsecvență cu toate numerele cu aceelasi numar de divizori")
    print("4. Determinare cea mai lungă subsecvență cu toate elementele prime")
    print("x Iesire")


def main():
    test_elem_ord()
    test_get_longest_sorted_asc()
    test_get_longest_same()
    test_prim()
    test_toate_elem_nr_prime()
    test_get_longest_all_primes()
    l = []
    while True:
        printMenu()
        optiune = input("dati op: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(get_longest_sorted_asc(l))
        elif optiune == "3":
            print(get_longest_same_div_count(l))
        elif optiune == "4":
            print(get_longest_all_primes(l))
        elif optiune == "x":
            break
        else:
            print("Gresit")

main()