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

   'Content-Type: text/plain; charset="utf-8"\nMIME-Version: 1.0\nContent-Transfer-Encoding: base64\nSubject: =?utf-8?b?UHJ6eWvFgmFkb3dhIHdpYWRvbW/Fm8SH?=\nFrom: John Mueller <John@JohnMuellerBooks.com>\nTo: John Mueller <John@JohnMuellerBooks.com>\n\nV2l0YWogxZp3aWVjaWUh\n'`

text/plain wskazuje, że jest to zwykła wiadomośc tekstowa do wyboru może być text/html, gdyby była to wiadomość w formacie html.

Są możliwe inne możliwości `listę standardowych typów i podtypów znajdziesz na stronie: <https://www.freeformatter.com/mime-types-list.html>`_
