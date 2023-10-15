Efektywne podnoszenie wyjątków w Twoim w kodzie
===============================================


https://realpython.com/python-raise-exception/

W swojej podróży z Pythonem natkniesz się na sytuacje, w których musisz zasygnalizować, że coś dzieje się nie tak w Twoim kodzie. Może na przykład plik nie istnieje, połączenie sieciowe lub z bazą danych nie powiedzie się albo kod otrzyma nieprawidłowe dane wejściowe. Powszechnym podejściem do rozwiązania tych problemów jest zgłoszenie wyjątku , powiadamiającego użytkownika o wystąpieniu błędu.  Do tego właśnie służy instrukcja Pythona ``raise`` .

.. note::
   Uwaga: w Pythonie nie wszystkie wyjątki są błędami. Wbudowany wyjątek `StopIteration <https://docs.python.org/3/library/exceptions.html#StopIteration>`_ jest tego doskonałym przykładem. Python wewnętrznie używa tego wyjątku do zakończenia iteracji po :ref:`iteratorach <iteratorsAndIterables0>`. Wyjątki Pythona reprezentujące błędy mają przyrostek Error dołączony do ich nazw.

   Python ma również określoną kategorię wyjątków, które reprezentują `ostrzeżenia <https://docs.python.org/3/library/exceptions.html#warnings>`_ dla programisty. Ostrzeżenia przydadzą się, gdy trzeba ostrzec użytkownika o jakimś stanie w programie. Jednakże warunek ten może nie uzasadniać zgłoszenia wyjątku i zakończenia programu. Typowym przykładem ostrzeżenia jest  komunikat `DeprecationWarning <https://docs.python.org/3/library/exceptions.html#DeprecationWarning>`_ wyświetlany w przypadku korzystania z przestarzałych funkcji.