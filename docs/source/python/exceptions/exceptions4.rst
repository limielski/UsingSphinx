Grupy wyjątków oraz except*w Pythonie 3.11
==========================================

źródło : `dalsza część <https://realpython.com/python311-exception-groups/>`_

Radzenie sobie z wyjątkami jest ważną częścią programowania. Czasami błędy powstają z powodu błędów w kodzie. W takich przypadkach dobre komunikaty o błędach pomogą w skutecznym debugowaniu kodu. Innym razem błędy nie wynikają z winy Twojego kodu. Być może użytkownik próbuje otworzyć uszkodzony plik, być może sieć nie działa, a może brakuje uwierzytelnienia w bazie danych.

Zwykle w danym momencie występuje tylko jeden błąd. Możliwe, że gdyby Twój kod nadal działał, wystąpiłby inny błąd. Jednak Python zazwyczaj zgłasza tylko pierwszy napotkany błąd. Są jednak sytuacje, w których sensowne jest zgłoszenie kilku błędów na raz:

Kilka jednoczesnych zadań może zakończyć się niepowodzeniem w tym samym czasie.
Kod czyszczący może powodować własne błędy.
Kod może wypróbować kilka różnych alternatyw, z których wszystkie powodują wyjątki.
W Pythonie 3.11 dostępna jest nowa funkcja zwana grupami wyjątków . Umożliwia grupowanie niepowiązanych wyjątków i zawiera nową except*składnię ich obsługi. Szczegółowy opis jest dostępny w PEP 654: Grupy wyjątków iexcept* .

PEP 654 został napisany i zaimplementowany przez Irit Katriel , jednego z głównych programistów CPython, przy wsparciu asyncioopiekuna Yury'ego Selivanova i byłego BDFL Guido van Rossuma . Został on zaprezentowany i omówiony na szczycie języka Python w maju 2021 r.

W tej sekcji dowiesz się, jak pracować z grupami wyjątków. W następnej sekcji zobaczysz praktyczny przykład współbieżnego kodu, który wykorzystuje grupy wyjątków do zgłaszania i obsługi błędów z kilku zadań jednocześnie.

Obsługuj regularne wyjątki za pomocą except
-------------------------------------------

Zanim zapoznasz się z grupami wyjątków, zapoznasz się z działaniem regularnej obsługi wyjątków w Pythonie. Jeśli znasz już obsługę błędów w Pythonie, w tym podrozdziale nie dowiesz się niczego nowego. Jednak ta recenzja będzie kontrastować z tym, czego dowiesz się później o grupach wyjątków. Wszystko, co zobaczysz w tej podsekcji samouczka, działa we wszystkich wersjach Pythona 3, łącznie z Pythonem 3.10.

Wyjątki zakłócają normalny przebieg programu. Jeśli zostanie zgłoszony wyjątek, Python porzuca wszystko inne i szuka kodu, który obsługuje błąd. Jeśli nie ma takich procedur obsługi, program zatrzymuje się, niezależnie od tego, co robił.

Możesz sam zgłosić błąd, używając słowa kluczowego raise:

.. code-block:: python
   :linenos:

   raise ValueError(654)


Tutaj wyraźnie podnosisz a ValueError z opisem 654. Możesz zobaczyć, że Python udostępnia funkcję śledzenia , która informuje Cię o nieobsługiwanym błędzie.

Czasami zgłaszasz takie błędy w swoim kodzie, aby zasygnalizować, że coś poszło nie tak. Jednak częściej spotyka się błędy generowane przez sam Python lub jakąś bibliotekę, której używasz. Na przykład Python nie pozwala na dodanie ciągu znaków i liczby całkowitej i podnosi a, TypeErrorjeśli spróbujesz tego:

.. code-block:: python
   :linenos:

   "3" + 11

Większość wyjątków zawiera opis, który może pomóc w ustaleniu, co poszło nie tak. W tym przypadku informuje Cię, że drugi termin również powinien być ciągiem znaków.

Do obsługi błędów używasz bloków try … except. Czasami używasz ich po prostu do zarejestrowania błędu i kontynuowania działania. Innym razem uda Ci się naprawić błąd lub zamiast tego obliczyć inną wartość.

Krótki try… except blok może wyglądać następująco:

.. code-block:: python
   :linenos:

try:
    raise ValueError(654)
except ValueError as err:
    print(f"Got a bad value: {err}")

Obsługujesz ValueErrorwyjątki, drukując komunikat na konsoli. Pamiętaj, że ponieważ poradziłeś sobie z błędem, w tym przykładzie nie ma śladu zwrotnego. Jednak inne typy błędów nie są obsługiwane:

.. code-block:: python
   :linenos:

   try:
       "3" + 11
   except ValueError as err:
       print(f"Got a bad value: {err}")

Mimo że błąd występuje w bloku try… except, nie jest on obsługiwany, ponieważ nie ma exceptklauzuli pasującej do TypeError. W jednym bloku możesz obsłużyć kilka rodzajów błędów:

.. code-block:: python
   :linenos:

   try:
       "3" + 11
   except ValueError as err:
       print(f"Got a bad value: {err}")
   except TypeError as err:
       print(f"Got bad types: {err}")


Ten przykład obsłuży oba wyjątki ValueError i TypeError.

Wyjątki są zdefiniowane w hierarchii . Na przykład a ModuleNotFoundErrorjest rodzajem ImportError, które jest rodzajem Exception.

.. note:: Ponieważ większość wyjątków dziedziczy po Exception, możesz spróbować uprościć obsługę błędów, używając tylko except bloków Exception. Zwykle jest to zły pomysł. Chcesz, aby bloki wyjątków były jak najbardziej szczegółowe, aby uniknąć nieoczekiwanych błędów i zakłócania obsługi błędów.

Pierwsza except klauzula pasująca do błędu uruchomi obsługę wyjątku:

.. code-block:: python
   :linenos:

   try:
       import no_such_module
   except ImportError as err:
       print(f"ImportError: {err.__class__}")
   except ModuleNotFoundError as err:
       print(f"ModuleNotFoundError: {err.__class__}")


Kiedy próbujesz zaimportować moduł, który nie istnieje, Python wywołuje plik ModuleNotFoundError. Jednakże, ponieważ ModuleNotFoundErrorjest to rodzaj ImportError, obsługa błędów wyzwala except ImportErrorklauzulę. Pamiętaj, że:

exceptWywołana zostanie co najwyżej jedna klauzula
Wywołana zostanie pierwsza except pasująca klauzula
Jeśli już wcześniej pracowałeś z wyjątkami, może się to wydawać intuicyjne. Jednak później zobaczysz, że grupy wyjątków zachowują się inaczej.

Chociaż w danym momencie aktywny jest co najwyżej jeden wyjątek, możliwe jest łączenie powiązanych wyjątków. To łączenie zostało wprowadzone w PEP 3134 dla Pythona 3.0. Jako przykład przyjrzyj się, co się stanie, jeśli podczas obsługi błędu zgłosisz nowy wyjątek:

.. code-block:: python
   :linenos:

   try:
       "3" + 11
   except TypeError:
       raise ValueError(654)


Zwróć uwagę na linię During handling of the above exception, another exception occurred. Przed tą linią znajduje się jeden ślad, reprezentujący oryginał TypeErrorspowodowany przez Twój kod. Następnie pod linią znajduje się kolejny ślad, reprezentujący nową informację ValueError, którą podniosłeś podczas obsługi pliku TypeError.

To zachowanie jest szczególnie przydatne, jeśli zdarzy się, że masz problem w kodzie obsługi błędów, ponieważ otrzymujesz wtedy informacje zarówno o pierwotnym błędzie, jak i o błędzie w programie obsługi błędów.

Możesz także samodzielnie połączyć wyjątki w łańcuch, używając instrukcji raise…from . Chociaż możesz używać wyjątków łańcuchowych do zgłaszania kilku wyjątków jednocześnie, pamiętaj, że mechanizm ten jest przeznaczony dla wyjątków, które są ze sobą powiązane, szczególnie gdy jeden wyjątek ma miejsce podczas obsługi innego.

Różni się to od przypadku użycia, do obsługi którego zaprojektowano grupy wyjątków. Grupy wyjątków będą grupować wyjątki, które nie są ze sobą powiązane, w tym sensie, że występują niezależnie od siebie. Podczas obsługi wyjątków łańcuchowych można przechwycić i obsłużyć tylko ostatni błąd w łańcuchu. Jak się wkrótce dowiesz, możesz przechwycić wszystkie wyjątki w grupie wyjątków.

Grupuj wyjątki z ExceptionGroup
-------------------------------

W tej podsekcji poznasz nową klasę ExceptionGroup dostępną w Pythonie 3.11. Po pierwsze, zauważ, że ExceptionGroup jest również rodzajem Exception:

.. code-block:: python
   :linenos:

>>> issubclass(ExceptionGroup, Exception)
True

Podobnie ExceptionGroup jak podklasa Exception, do pracy z nią możesz używać zwykłej obsługi wyjątków Pythona. Możesz podnieść ExceptionGroup z raise, chociaż prawdopodobnie nie będziesz tego robić zbyt często, chyba że implementujesz jakąś bibliotekę niskiego poziomu. Możliwe jest również złapanie ExceptionGroup z except ExceptionGroup. Jednakże, jak dowiesz się w następnym podrozdziale , zazwyczaj lepiej będzie zastosować nową except*składnię.

W przeciwieństwie do większości innych wyjątków, grupy wyjątków podczas inicjalizacji przyjmują dwa argumenty:

* Zwykły opis
* Sekwencja podwyjątków
* Sekwencja podwyjątków może obejmować inne grupy wyjątków, ale nie może być pusta:

.. code-block:: python
   :linenos:

   >>> ExceptionGroup("one error", [ValueError(654)])
   ExceptionGroup('one error', [ValueError(654)])

   >>> ExceptionGroup("two errors", [ValueError(654), TypeError("int")])
   ExceptionGroup('two errors', [ValueError(654), TypeError('int')])

   >>> ExceptionGroup("nested",
   ...     [
   ...         ValueError(654),
   ...         ExceptionGroup("imports",
   ...             [
   ...                 ImportError("no_such_module"),
   ...                 ModuleNotFoundError("another_module"),
   ...             ]
   ...         ),
   ...     ]
   ... )
   ExceptionGroup('nested', [ValueError(654), ExceptionGroup('imports',
     [ImportError('no_such_module'), ModuleNotFoundError('another_module')])])

   >>> ExceptionGroup("no errors", [])
   Traceback (most recent call last):
     ...
   ValueError: second argument (exceptions) must be a non-empty sequence


W tym przykładzie tworzysz instancję kilku różnych grup wyjątków, co pokazuje, że grupy wyjątków mogą zawierać jeden wyjątek, kilka wyjątków, a nawet inne grupy wyjątków. Grupy wyjątków nie mogą być jednak puste.

Twoje pierwsze spotkanie z grupą wyjątków będzie prawdopodobnie polegać na jej prześledzeniu. Śledzenia grup wyjątków są sformatowane tak, aby wyraźnie pokazać strukturę w grupie. Po podniesieniu grupy wyjątków zobaczysz ślad:

.. code-block:: python
   :linenos:

   >>> raise ExceptionGroup("nested",
   ...     [
   ...         ValueError(654),
   ...         ExceptionGroup("imports",
   ...             [
   ...                 ImportError("no_such_module"),
   ...                 ModuleNotFoundError("another_module"),
   ...             ]
   ...         ),
   ...         TypeError("int"),
   ...     ]
   ... )
     + Exception Group Traceback (most recent call last):
     |   ...
     | ExceptionGroup: nested (3 sub-exceptions)
     +-+---------------- 1 ----------------
       | ValueError: 654
       +---------------- 2 ----------------
       | ExceptionGroup: imports (2 sub-exceptions)
       +-+---------------- 1 ----------------
         | ImportError: no_such_module
         +---------------- 2 ----------------
         | ModuleNotFoundError: another_module
         +------------------------------------
       +---------------- 3 ----------------
       | TypeError: int
       +------------------------------------


`dalsza część <https://realpython.com/python311-exception-groups/>`_