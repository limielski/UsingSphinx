Wstęp
=====

Biblioteka `argparse` to narzędzie, które umożliwia łatwe parsowanie argumentów wiersza poleceń w programach Python. Pozwala programistom tworzyć interfejsy wiersza poleceń, które są intuicyjne dla użytkowników i umożliwiają im dostosowywanie zachowania programu poprzez przekazanie argumentów i opcji.

Argparse oferuje wiele funkcji, które ułatwiają zarządzanie argumentami wiersza poleceń. W tym samouczku dowiesz się, jak korzystać z Argparse cheatsheet i jak zbudować interfejs wiersza poleceń dla swojego programu Python.

.. code-block:: python
   :linenos:

   import argparse


Podstawowe użycie argparse
--------------------------

Główne zadanie argparse polega na parsowaniu argumentów wiersza poleceń.
Aby to zrobić, musisz zdefiniować parser i określić, jakie argumenty i opcje chcesz obsłużyć.

Oto przykład prostego programu, który korzysta z argparse do obsługi argumentu wiersza poleceń:

.. code-block:: python
   :linenos:

   import argparse

   parser = argparse.ArgumentParser()
   parser.add_argument("name", help="Your name")
   args = parser.parse_args()

   print("Hello, " + args.name + "!")

W tym przykładzie definiujemy parser i dodajemy argument `name` do niego. Argument ten jest wymagany, co oznacza, że użytkownik musi go podać podczas uruchamiania programu. Następnie parsujemy argumenty wiersza poleceń przy użyciu metody `parse_args()`, która zwraca obiekt zawierający przekazane argumenty.

Aby uruchomić ten program i przekazać swoje imię jako argument wiersza poleceń, wpisz poniższą komendę:

.. code-block:: bash

   python program.py Antoś

Otrzymasz odpowiedź ``Hello, John!``, która wyświetli się na ekranie.


Opcje wiersza poleceń
---------------------

Argparse umożliwia również obsługę opcji wiersza poleceń. Opcje to flagi, które zmieniają zachowanie programu. Mogą mieć wartość lub być obecne lub nieobecne.

Oto przykład programu, który korzysta z opcji wiersza poleceń:

.. code-block:: python
   :linenos:

   import argparse

   parser = argparse.ArgumentParser()
   parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
   args = parser.parse_args()

   if args.verbose:
       print("Verbose mode enabled")
   else:
       print("Verbose mode disabled")


W tym przykładzie dodajemy opcję ``-v`` lub ``--verbose``, która jest flagą. Jeśli ta flaga jest obecna, włączony jest tryb szczegółowy, co oznacza, że program wyświetli dodatkowe informacje. Jeśli flaga nie jest obecna, tryb szczegółowy jest wyłączony.

Aby uruchomić ten program w trybie szczegółowym, wpisz poniższą komendę:

.. code-block:: bash

   python program.py -v


Otrzymasz odpowiedź ``Verbose mode enabled``. Jeśli nie chcesz uruchamiać programu w trybie szczegółowym, po prostu nie dodawaj flagi ``-v`` do komendy.
