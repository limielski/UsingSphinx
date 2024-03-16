Git w skrócie
=============

Ściągawka
---------

Operacje związane z repozytorium lokalnym:
------------------------------------------

.. list-table::
   :widths: 25 30 45
   :header-rows: 1

   * - Cel Działania
     - Polecenia Git
     - Wyjaśnienie
   * - dodawanie do repozytorium
     - ``git add plik``
     - dodaje plik do repozytorium. możemy podać cały katalog. Jesli chcemy dodać bieżący podajemy znak kropki``.``
   * - wycofanie z repozytorium
     - ``git reset plik``
     - dodany plik jest wycofywany z repozytorium

.. list-table::
   :widths: 25 30 45
   :header-rows: 1

   * - Cel Działania
     - Polecenie Git (Lokalne)
     - Wyjaśnienie
   * - Klonowanie
     - ``git clone <url_repozytorium>``
     - Tworzy kopię zdalnego repozytorium na lokalnym komputerze.
   * - Tworzenie nowej gałęzi
     - ``git branch <nazwa_nowej_gałęzi>``
     - Tworzy nową, lokalną gałąź w repozytorium.
   * - Przejście na inną gałąź
     - ``git checkout <nazwa_gałęzi>``
     - Przenosi HEAD (aktualną gałąź) na wskazaną gałąź.
   * - Usuwanie gałęzi
     - ``git branch -d <nazwa_gałęzi>``
     - Usuwa lokalną gałąź.
   * - Wyświetlanie listy gałęzi
     - ``git branch``
     - Wyświetla listę dostępnych gałęzi.
   * - Wyświetlanie stanu repozytorium
     - ``git status``
     - Informuje o stanie repozytorium, wskazuje zmiany do zatwierdzenia, itp.
   * - Wyświetlanie historii commitów
     - ``git log``
     - Wyświetla historię commitów na bieżącej gałęzi.
   * - Tworzenie commita
     - ``git commit -m "Opis zmian"``
     - Zatwierdza zmiany i tworzy nowy commit w historii.


Operacje związane z repozytorium zdalnym "origin":
--------------------------------------------------

.. list-table::
   :widths: 25 30 45
   :header-rows: 1

   * - Cel Działania
     - Polecenie Git (Origin)
     - Wyjaśnienie
   * - Aktualizacja
     - ``git fetch origin``
     - Pobiera informacje o zmianach z repozytorium "origin".
   * - Pobieranie i scalanie
     - ``git pull origin <gałąź>``
     - Pobiera zmiany z repozytorium "origin" i scalają je z bieżącą gałęzią.
   * - Przesyłanie zmian
     - ``git push origin <gałąź>``
     - Przesyła zmiany z bieżącej gałęzi do repozytorium "origin".
   * - Wyświetlanie historii commitów na zdalnym repozytorium
     - ``git log origin/<gałąź>``
     - Wyświetla historię commitów na repozytorium "origin".


Operacje związane z repozytorium zdalnym "upstream" (lub innym zdalnym repozytorium):
-------------------------------------------------------------------------------------


.. list-table::
   :widths: 25 30 45
   :header-rows: 1

   * - Cel Działania
     - Polecenie Git (Upstream)
     - Wyjaśnienie
   * - Aktualizacja
     - ``git fetch upstream``
     - Pobiera informacje o zmianach z repozytorium "upstream" lub innego zdalnego repozytorium.
   * - Pobieranie i scalanie
     - ``git pull upstream <gałąź>``
     - Pobiera zmiany z repozytorium "upstream" i scalają je z bieżącą gałęzią.
   * - Wyświetlanie historii commitów na zdalnym repozytorium
     - ``git log upstream/<gałąź>``
     - Wyświetla historię commitów na repozytorium "upstream" lub innym zdalnym repozytorium.
