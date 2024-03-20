Funkcja mail.uid
================

+---------------------------------------------------------------+
| Polecenie | Opis                                              |
+===========+===================================================+
| 'SEARCH'  | Wyszukuje wiadomości spełniające kryteria.        |
+-----------+---------------------------------------------------+
| 'FETCH'   | Pobiera konkretną porcję danych wiadomości.       |
+-----------+---------------------------------------------------+
| 'STORE'   | Modyfikuje flagi wiadomości.                      |
+-----------+---------------------------------------------------+
| 'COPY'    | Kopiuje wiadomości z bieżącego skrzynki do innej. |
+-----------+---------------------------------------------------+
| 'MOVE'    | Przenosi wiadomości z bieżącego skrzynki do innej.|
+-----------+---------------------------------------------------+

W przypadku 'FETCH', 'STORE', 'COPY', i 'MOVE' drugi argument metody uid jest używany do przekazania zakresu wiadomości, do których ma zastosowanie polecenie. Zakres ten jest reprezentowany jako ciąg, i może obejmować jeden UID ('1'), zakres UID ('1:3'), lub wielokrotny UID oddzielony przecinkami ('1,3').
Na przykład:
mail.uid('STORE', '1', '+FLAGS (\\Deleted)'): Oznacza wiadomość o UID 1 jako usuniętą.
mail.uid('FETCH', '1', '(BODY[TEXT])'): Pobiera treść wiadomości o UID 1.
mail.uid('COPY', '1', 'INBOX'): Kopiuje wiadomość o UID 1 do skrzynki odczytanej.
mail.uid('MOVE', '1', 'INBOX'): Przenosi wiadomość o UID 1 do skrzynki odczytanej.
Pamiętaj, że te polecenia IMAP są skierowane do serwera, więc rzeczywistość ich działania może zależeć od konkretnego serwera i jego konfiguracji.
