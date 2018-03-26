
#if a == 0:
#    if b == 0:
#        if c == 0:
#            wynik = "nieskonczenie wiele"
#        else:
#            wynik = "brak"
#    else:
#        wynik = "jeden"
#else:
#    if(b * b - 4 * a * c) < 0:
#        wynik = "brak"
#    else:
#        if(b * b - 4 * a * c) > 0:
#            wynik = "sa dwa rozwiazania"
#        else:
#            wynik = "jeden"

a,b,c = (2,5,1)
wynik = ""

wynik = ( ( "nieskonczenie wiele" if c == 0 else "brak" ) if b == 0 else "Jedno"
                if a == 0 else
        "Brak" if (b * b - 4 * a * c) < 0 else
        ("dwa" if (b * b -4 * a * c) > 0 else "Jedno"
    )
)
print wynik
