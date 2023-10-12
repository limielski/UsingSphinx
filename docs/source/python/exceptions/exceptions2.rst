Jak złapać jeden z kilku możliwych wyjątków Pythona
===================================================

Łapanie poszczególnych wyjątków w oddzielnych exceptklauzulach jest najlepszym rozwiązaniem, jeśli chcesz wykonać różne czynności obsługi na różnych przechwytywanych wyjątkach. Jeśli okaże się, że wykonujesz te same działania w odpowiedzi na różne wyjątki, możesz stworzyć prostszy, bardziej czytelny kod, obsługując wiele wyjątków w jednej exceptklauzuli. Aby to zrobić, określ wyjątki jako krotkę w exceptinstrukcji.

Załóżmy, że podoba Ci się pomysł, aby Twój wcześniejszy kod był w stanie obsłużyć oba wyjątki w jednym wierszu. Aby to zrobić, decydujesz się przepisać swój kod w następujący sposób:

.. literalinclude:: code/multiple_exceptions.py
   :linenos:
   :tab-width: 4

Tym razem, jeśli złapiesz wyjątek ValueErrorlub ZeroDivisionError, obsłużysz go za pomocą tej samej except klauzuli. exceptJeśli chcesz, możesz także dołączyć dodatkowe klauzule dotyczące innych wyjątków. Działałyby one dla ciebie w taki sam sposób, jak wcześniej.

Następnie możesz przetestować tę wersję swojego kodu, korzystając z tych samych przypadków testowych, co poprzednio:

.. code-block:: bash

   $ python multiple_exceptions.py
   What is your first number? 10
   What is your second number? 5
   10.0 divided by 5.0 is 2.0

   $ python multiple_exceptions.py
   What is your first number? 10
   What is your second number? "five"
   There was an error

   $ python multiple_exceptions.py
   What is your first number? 10
   What is your second number? 0
   There was an error

W pierwszym teście try wykonywany jest tylko blok, ponieważ nie zgłosiłeś żadnych wyjątków. Twój drugi i trzeci przypadek testowy zgłaszają odpowiednio a ValueErrori . ZeroDivisionErrorZłapałeś każdego z nich w tym samym except zdaniu. W obu przypadkach przebieg programu jest try wtedy except (ValueError, ZeroDivisionError). Ponownie, Twój kod przetrwa wyjątki bez awarii.

Chociaż jesteś zadowolony, że procedura obsługi bezpiecznie obsługuje oba wyjątki w ten sam sposób, chciałbyś dokładnie wiedzieć, który wyjątek jest zgłaszany. W dalszej części dowiesz się, jak to zrobić.

