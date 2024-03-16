Podstawy Gita
=============

3. Inicjalizacja repozytorium Git:

   .. code-block:: bash

      git init

4. Utwórz kopię roboczą repozytorium za pomocą `git clone`.

5. Dodawanie zmian do indeksu:

   .. code-block:: bash

      git add nazwa_pliku

6. Zapisz zmiany w lokalnym repozytorium:

   .. code-block:: bash

      git commit -m "Opis zmian"

7. Sprawdź stan repozytorium:

   .. code-block:: bash

      git status

8. Wycofywanie pliku z repozytorium

   .. code-block:: bash

      git reset plik
9. Utworzenie nowej gałęzi i przełączenie się na nią

   .. code-block:: bash

      git checkout mybranch

10. Wysłanie zmian na github, ale wczesniej utworzenie tej samej gałęzi co lokalnie,

   - jesli wcześniej tego nie zrobiono

   .. code-block::

      git push --set-upstream origin mybranch

   - jesli wcześniej to zrobiono wystarczy samo

   .. code-block::

      git push
