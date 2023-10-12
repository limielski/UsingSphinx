Zidentyfikuj, który wyjątek Pythona został przechwycony
=======================================================

Jeśli znasz koncepcje programowania obiektowego , wiesz, że klasy to szablony definiujące zawartość i możliwości obiektów, które tworzysz lub tworzysz z nich instancje . Kiedy Twój kod zgłasza wyjątek Pythona, w rzeczywistości tworzy instancję objectz klasy , która definiuje wyjątek. Na przykład, gdy zgłaszasz ValueErrorwyjątek, tworzysz instancję klasy ValueError.

Chociaż do pracy z wyjątkami nie jest potrzebna dogłębna wiedza z zakresu programowania obiektowego, należy pamiętać, że różne obiekty wyjątków istnieją tylko dlatego, że są tworzone z różnych klas.

Decydujesz się spróbować zidentyfikować indywidualne wyjątki złapane w poprzednim kodzie:

.. literalinclude:: code/exception_identification.py


Tutaj dokonałeś pewnych zmian w programie obsługi. Nadal przechwytuje oba ValueErrori ZeroDivisionErrorwyjątki, ale tym razem przypisujesz obiekt wyjątku do zmiennej o nazwie error. Dzięki temu będziesz mógł to przeanalizować.

Aby znaleźć klasę an Exception, użyj type(). Jeśli wydrukujesz .'__name__' atrybut klasy, zobaczysz dokładnie, który wyjątek obsłużył Twój kod. Teraz możesz dowiedzieć się, które wyjątki wystąpiły:

.. code-block::

   $ python exception_identification.py
   What is your first number? 10
   What is your second number? 5
   10.0 divided by 4.0 is 2.0

   $ python exception_identification.py
   What is your first number? 10
   What is your second number? "five"
   A ValueError has occurred.

   $ python exception_identification.py
   What is your first number? 10
   What is your second number? 0
   A ZeroDivisionError has occurred.


Pierwszy test przynosi ulgę, bo pokazuje, że Twoja aktualizacja nadal działa. Drugi i trzeci test zgłaszają wyjątki. Jak widać, Twój kod poprawnie zidentyfikował zarówno wyjątki, ValueError jak i ZeroDivisionError.

Załóżmy, że zdecydujesz się ulepszyć swój kod, zezwalając na mnożenie. Decydujesz się również na ręczne wywołanie a, RuntimeError jeśli użytkownik zażąda nieobsługiwanej operacji lub zrobi coś nieoczekiwanego, na przykład wprowadzi znak powrotu karetki:

.. literalinclude:: code/exception_identification_with_structural_pattern_matching.py


Tym razem użyjesz operator modułów mul()i true div() funkcji do wykonywania mnożenia i dzielenia. Przekazujesz je do swojej calculate() funkcji wraz z dwiema liczbami. Twoja calculate()funkcja następnie wywołuje operator funkcję modułu, którą jej przekazałeś, która wykonuje obliczenia. Działa to tylko wtedy, gdy wpiszesz dwie liczby i / albo * dla operacji.

Chociaż można zakodować bezpośrednio calculate()użycie operatora * or /, użycie operator funkcji modułu upraszcza kod funkcji i zapewnia rozszerzalność.

Jeśli użytkownik wprowadzi nieprawidłowy operator, kod jawnie wywoła RuntimeError. Jak każdy inny wyjątek, spowoduje to awarię kodu, jeśli go nie obsłużysz.

Klauzula except twojego modułu obsługi ponownie zawiera krotkę wyjątków, które chcesz przechwycić. Odwołujesz się do wyjątku, tak jak poprzednio, za pomocą zmiennej o nazwie error. Najpierw procedura obsługi wypisuje nazwę klasy wyjątku, niezależnie od zgłoszonego wyjątku. Następnie używasz tego match bloku do wydrukowania komunikatu w oparciu o konkretny obsługiwany wyjątek.

Wybierasz dopasowanie wzorca strukturalnego zamiast wielu elif klauzul zapewniających schludność. Wyjątek polegający na tym, że errorodniesienia do zmiennych są porównywane z różnymi case klauzulami. Wykonywany jest tylko pierwszy pasujący caseblok, a pozostałe są ignorowane. Wybrany caseblok następnie drukuje komunikat, po którym następuje error. Włączenie error do ciągu f powoduje wydrukowanie domyślnego komunikatu śledzenia wyjątku w celu uzyskania dodatkowego kontekstu.

Jeśli try klauzula nie zgłasza już żadnych wyjątków, program ignoruje ją except i kontrola przechodzi na else klauzulę. Używasz go tutaj, aby wydrukować wynik obliczenia.

Teraz ponownie testujesz calculate(), używając normalnych danych wejściowych:

.. code-block::

   $ python exception_identification_with_structural_pattern_matching.py
   What is your first number? 10
   What is your second number? 4
   Enter either * or /: /
   10.0 / 4.0 = 2.5

   $ python exception_identification_with_structural_pattern_matching.py
   What is your first number? 10
   What is your second number? 5
   Enter either * or /: *
   10.0 * 5.0 = 50.0


Jak widać, dzielenie nadal działa, podobnie jak nowa funkcja mnożenia. Rozwiń poniższą sekcję, aby zobaczyć, co się stanie, gdy utworzysz wyjątki.

.. raw:: html

   <details>
       <summary>Kliknij, aby pokazać/ukryć</summary>
       Tutaj znajduje się ukryta zawartość.
      <pre>
         $ python exception_identification_with_structural_pattern_matching.py
      What is your first number? 10
      What is your second number? 5
      Enter either * or /: +
      A RuntimeError has occurred
      You have entered an invalid symbol: '+' is an unsupported operation

      $ python exception_identification_with_structural_pattern_matching.py
      What is your first number? 10
      What is your second number? 5
      Enter either * or /:
      A RuntimeError has occurred
      You have entered an invalid symbol: '' is an unsupported operation

      $ python exception_identification_with_structural_pattern_matching.py
      What is your first number? 10
      What is your second number? "five"
      A ValueError has occurred
      You have not entered a number: could not convert string to float: '"five"'

      $ python exception_identification_with_structural_pattern_matching.py
      What is your first number? 10
      What is your second number? 0
      Enter either * or /: /
      A ZeroDivisionError has occurred
      You can't divide by zero: float division by zero
      </pre>
      <br>

      Spójrz na dwie ostatnie linie każdego testu. Twoje procedury obsługi wyjątków pomyślnie wykonały swoją pracę.

      Tym razem wykonujesz szerszy zakres testów. Najpierw próbujesz dodać, a potem nie określasz operacji. Obydwa skutkują RuntimeError. Twoje testy końcowe są identyczne z tymi, które przeprowadziłeś wcześniej. Jak widać, Twój kod nie ulega awarii i poprawnie identyfikuje zgłoszony wyjątek.

      Dlaczego nie przetestować tego kodu dokładniej, aby utrwalić zrozumienie? Możesz także zagłębić się w operatormoduł i wykorzystać go do rozszerzenia poprzedniego przykładu o obsługę dodawania, odejmowania lub innych operacji, które chcesz.
   <br>
   </details>


   Teraz, gdy wiesz, jak identyfikować różne Exceptionobiekty za pomocą ich klas, następnie dowiesz się, jak używać hierarchii wyjątków Pythona , aby uprościć obsługę wyjątków poprzez obsługę wyjątku ich rodzica.


