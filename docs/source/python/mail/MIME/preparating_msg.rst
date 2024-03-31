Przygotowanie wiadomości
========================

.. code-block:: Python
   :linenos:

   from email.mime.text import MIMEText
   msg = MIMEText("Witaj!")
   msg['Subject'] = "Przykładowa wiadomość"
   msg['From']='John Mueller <John@JohnMuellerBooks.com>'
   msg['To'] = 'John Mueller <John@JohnMuellerBooks.com>'

   msg.as_string()

:python:`msg.as_string()` utworzy nastepującą wiadomość tekstową

.. code-block:: shell

   'Content-Type: text/plain; charset="utf-8"\nMIME-Version: 1.0\nContent-Transfer-Encoding: base64\nSubject:
   =?utf-8?b?UHJ6eWvFgmFkb3dhIHdpYWRvbW/Fm8SH?=\nFrom: John Mueller <John@JohnMuellerBooks.com>\nTo: John Mueller
   <John@JohnMuellerBooks.com>\n\nV2l0YWogxZp3aWVjaWUh\n'`

text/plain wskazuje, że jest to zwykła wiadomośc tekstowa do wyboru może być text/html, gdyby była to wiadomość w formacie html.

Są możliwe inne możliwości:
`listę standardowych typów i podtypów znajdziesz na stronie: <https://www.freeformatter.com/mime-types-list.html>`_

.. note:: Metoda kodowania i tworzenia nagłówkow jest wykonywana automatycznie, ale możemy wpłynąć na metode kodowania.

set_param - informacjie w nagłówkach
------------------------------------

W przypadku metody `as_bytes()` nie można bezpośrednio określić metody kodowania, ponieważ ta metoda służy jedynie
do przekształcenia obiektu wiadomości MIME do postaci bajtowej. Metoda kodowania jest stosowana automatycznie,
w zależności od zawartości wiadomości i jej nagłówków, aby zapewnić poprawność przekazu danych.

Jednakże, możesz wpłynąć na metodę kodowania poprzez manipulację zawartością wiadomości i jej nagłówkami.
Na przykład, jeśli chcesz użyć konkretnego rodzaju kodowania dla treści wiadomości lub załącznika, możesz to zrobić,
odpowiednio ustawiając nagłówek Content-Transfer-Encoding. Oto przykładowy kod, który ilustruje,
jak to zrobić dla treści tekstu:

.. code-block:: python
   :emphasize-lines: 13, 14
   :linenos:

   from email.mime.text import MIMEText

   # Tworzenie wiadomości MIMEText
   msg = MIMEText("Tekst wiadomości do zakodowania")

   # Ustawienie nagłówków
   msg['Subject'] = "Temat wiadomości"
   msg['From'] = 'nadawca@example.com'
   msg['To'] = 'odbiorca@example.com'

   # Ustawienie metody kodowania dla treści
   msg.set_param('charset', 'utf-8')
   msg.set_param('Content-Transfer-Encoding', 'quoted-printable')

   # Przekształcenie wiadomości do postaci bajtowej
   msg_bytes = msg.as_bytes()

   # Wypisanie zakodowanej wiadomości bajtowej
   print(msg_bytes)

Stosuje się w tym celu metodę :python:`set_param()`

bez zastosowania metody set_param

.. parsed-literal::

   Content-Type: text/plain; charset="utf-8"
   MIME-Version: 1.0
   Content-Transfer-Encoding: base64
   Subject: =?utf-8?q?Temat_wiadomo=C5=9Bci?=
   From: leszekimielski@gmail.com
   To: leszekimielski@gmail.com

   VGVrc3Qgd2lhZG9tb8WbY2kgZG8gemFrb2Rvd2FuaWE=

po zastosowaniu

.. parsed-literal::

   MIME-Version: 1.0
   Content-Transfer-Encoding: base64
   Subject: =?utf-8?q?Temat_wiadomo=C5=9Bci?=
   From: leszekimielski@gmail.com
   To: leszekimielski@gmail.com
   Content-Type: text/plain; charset="utf-8";
    content-transfer-encoding="quoted-printable"

   VGVrc3Qgd2lhZG9tb8WbY2kgZG8gemFrb2Rvd2FuaWE=

Zmiana domyslengo kodowania
---------------------------

Nie powinno się jednak tego robić. Najlepiej zachowac spójność wszystkch kodowań.
W ponizszym kodzie w funkcji MIMEText ustalane jest domyslne kodowanie jako 'ISO-8859-2'
oraz domyślny zbiór znaków tez jako 'ISO-8859-2'. Dla spójności nie powinno sie stosować zbioru znaków, które nie pokrywaja się ze sposobem kodowania, gdyż prowadzi to do błedów.

Nastepnie zmieniany jest standard kodowania dla ciała wiadomości na Quoted-Printable.
Dlatego przy rozkodowywaniu posłuzylismy sie modułem quopri a następnie zdekodowaliśmy tekst do 'ISO-8859-2'

.. code-block::
   :emphasize-lines: 13
   :linenos:

   from email.mime.text import MIMEText
   from email.charset import Charset
   import quopri

   # Tworzenie wiadomości MIMEText
   msg = MIMEText("Tekst wiadomości do zakodowania\nSomething to send".encode('ISO-8859-2'), _charset='ISO-8859-2')

   # Ustawienie nagłówków
   msg['Subject'] = "Temat wiadomości"
   msg['From'] = 'leszekimielski@gmail.com'
   msg['To'] = 'leszekimielski@gmail.com'

   # Ustalanie metody kodowania dla treści
   my_charset = Charset('ISO-8859-2')
   my_charset.header_encoding = 'B'  # For headers, use BASE64 encoding.
   my_charset.body_encoding = 'Q'  # For body, use QP (Quoted-Printable) encoding.
   msg.set_charset(my_charset)

   # Przekształcenie wiadomości do postaci bajtowej
   msg_bytes = msg.as_bytes()
   print(msg_bytes)
   msg_bytes = quopri.decodestring(msg_bytes).decode('ISO-8859-2')
   print(msg_bytes)


i wynik


.. parsed-literal::

   MIME-Version: 1.0
   Content-Type: text/plain; charset="iso-8859-2"
   Content-Transfer-Encoding: quoted-printable
   Subject: =?utf-8?q?Temat_wiadomoĹci?From: leszekimielski@gmail.com
   To: leszekimielski@gmail.com

   Tekst wiadomości do zakodowania
   Something to send
