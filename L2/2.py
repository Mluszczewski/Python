a,b,c = (2,5,1)
wynik = ""

wynik = ( ( "nieskonczenie wiele" bool and [c] or [b][0]  else "brak" ) bool and [b] or [a][0] else "Jedno"
                bool and [a] or [c][0] else
        "Brak" if (b * b - 4 * a * c) < 0 else
        ("dwa" if (b * b -4 * a * c) > 0 else "Jedno"
    )
)
print wynik
