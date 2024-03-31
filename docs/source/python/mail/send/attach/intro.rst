Wstęp
-----
`MIMEMultipart, MIMEText, MIMEBase, payloads for sending email with file attachment <https://stackoverflow.com/questions/38825943/mimemultipart-mimetext-mimebase-and-payloads-for-sending-email-with-file-atta>`_

`Sending Emails in Python - Tutorial with Code Examples <https://thepythonguru.com/sending-emails-in-python-tutorial-with-code-examples/>`_

Często termin attach w kontekście e-maili jest kojarzony ze załącznikami takimi jak dokumenty, obrazy itp.

Jednakże w kontekście tworzenia wiadomości e-mail za pomocą modułu email.mime w Pythonie, metoda attach jest używana
nie tylko do dołączania załączników w sensie fizycznych plików, ale także do dołączania różnych części wiadomości e-mail.

W przypadku MIMEText, attach służy do dołączania części tekstowej wiadomości e-mail.

Tworzy to sekcję w ciele wiadomości e-mail, a nie załącznik w tradycyjnym sensie.
Więc kiedy robisz :python:`msg.attach(MIMEText(body, 'plain', _charset='utf-8'))`, dołączasz treść tekstową do
wiadomości e-mail.

Jeśli chcesz dodać załącznik w sensie pliku do wiadomości e-mail, musisz użyć MIMEBase lub MIMEApplication lub jednej
z innych klas związanych z MIME. Tutaj jest przykładowy sposób, jak to zrobić:

.. code-block:: python
   :linenos:

   from email.mime.application import MIMEApplication

   # Wczytanie pliku, który chcesz załączyć
   with open("sciezka/do/pliku", "rb") as file:
       attach_file = MIMEApplication(file.read(), Name="nazwa_pliku")

   # Dołączanie pliku do wiadomości
   msg.attach(attach_file)

W powyższym kodzie MIMEApplication jest używane do tworzenia części wiadomości e-mail, która reprezentuje załącznik.

W tym konkretnym przypadku załącznik jest odczytywany z pliku.

Jeśli załączysz plik do wiadomości e-mail za pomocą powyższego kodu, odbiorca otrzyma e-mail z plikiem jako załącznikiem.

Będzie mógł pobrać ten plik i otworzyć go za pomocą odpowiedniego oprogramowania na swoim komputerze.

Załącznik będzie widoczny w sekcji "Załączniki" wiadomości e-mail w programie pocztowym odbiorcy.
Większość programów pocztowych (takich jak Outlook, Gmail, itp.) umożliwia pobieranie załączonych plików na dysk twardy.
Zauważ, że rodzaj załączonego pliku (czy jest to dokument tekstowy, obraz, plik PDF, itp.) nie ma wpływu na sposób
przesłania wiadomości. Meta-dane tego pliku (np. nazwa i rozszerzenie) są zachowywane w załączniku,
a oprogramowanie odbiorcy używa tych meta-danych do asocjacji załącznika z odpowiednimi programami na komputerze odbiorcy.
