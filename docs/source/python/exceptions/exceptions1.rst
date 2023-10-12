How to Catch Multiple Exceptions in Python
==========================================

Aby umożliwić podjęcie działań w przypadku wystąpienia błędu, implementujesz obsługę wyjątków, pisząc kod wychwytujący i radzący sobie z wyjątkami. Lepsze to niż awaria kodu i przestraszenie użytkownika. Do obsługi wyjątków służy tryinstrukcja. Umożliwia to monitorowanie kodu pod kątem wyjątków i podejmowanie działań w przypadku ich wystąpienia.

Większość  instrukcji `try` używa bloków `try…except`  w następujący sposób:

Blok `try` zawiera kod, który chcesz monitorować pod kątem wyjątków. Wszelkie wyjątki zgłoszone w ramach `try` będą kwalifikować się do obsługi.

`except`. Następnie następuje jeden lub więcej bloków try. Tutaj definiujesz kod, który będzie wykonywany, gdy wystąpią wyjątki. W Twoim kodzie wszelkie zgłoszone wyjątki wyzwalają powiązaną klauzulę except. Pamiętaj, że jeśli masz wiele klauzul except, program uruchomi tylko pierwszą , która wyzwala, a następnie zignoruje resztę.

Aby dowiedzieć się, jak to działa, napisz blok try  monitorujący trzy linie kodu. Dołączasz dwa bloki except, po jednym dla każdego wyjątki ValueError i ZeroDivisionError, aby obsłużyć je w przypadku ich wystąpienia:

.. literalinclude:: code/handler_statement.py
   :linenos:
   :tab-width: 4


Dobra wiadomość jest taka, że Twój kod nigdy się nie zawiesza. Dzieje się tak, ponieważ Twój kod pomyślnie obsłużył wyjątki.

Po pierwsze, podałeś akceptowalne dane. Kiedy spojrzysz na dane wyjściowe, zobaczysz, że program przepływa tylko przez try. Nie wywołałeś żadnej z exceptklauzul, ponieważ Python nie zgłosił żadnych wyjątków.

Następnie powodujesz a ValueError, wprowadzając ciąg. Dzieje się tak, ponieważ float()funkcja nie może przekonwertować pliku "five"na plik float. Przebieg programu staje się teraz trywtedy except ValueError. Pomimo podniesienia ValueError, Twój kod poradził sobie z tym z wdziękiem. Twoi użytkownicy nie będą już doświadczać niepokojącej awarii.

W ostatnim uruchomieniu testowym próbujesz podzielić przez 0. Tym razem powodujesz, ZeroDivisionErrorbo Pythonowi nie podoba się twój entuzjazm dla sfer Riemanna i nieskończoności . Tym razem przebieg programu jest trynastępujący except ZeroDivisionError. Ponownie, Twój kod z wdziękiem poradził sobie z wyjątkiem. Większość użytkowników będzie z tego zadowolona, choć matematycy mogą być rozczarowani.

Po zakończeniu obsługi błędów działanie programu będzie zwykle kontynuowane z dowolnym kodem poza tryinstrukcją. W tym przypadku nie ma żadnego, więc program po prostu się kończy.

W ramach ćwiczenia możesz spróbować wprowadzić ciąg znaków jako pierwsze wejście i liczbę jako drugie. Czy potrafisz przewidzieć, co się stanie, zanim spróbujesz?


.. note::
   Twój kod przechwytuje tylko ZeroDivisionErrorlub ValueErrorwyjątki. Jeśli zostaną podniesione inne, nastąpi awaria jak poprzednio. Można to obejść, tworząc końcową except Exceptionklauzulę wychwytującą wszystkie inne wyjątki. Jest to jednak zła praktyka, ponieważ możesz wychwycić wyjątki, których się nie spodziewałeś. Lepiej jawnie wychwycić wyjątki i dostosować sposób ich obsługi.

Do tego momentu sprawdziłeś, jak indywidualnie wychwytywać wyjątki za pomocą instrukcji try. W pozostałej części tego samouczka dowiesz się, jak wychwycić wiele wyjątków. Czas zanurkować nieco głębiej.