Logowanie TLS
=============


bez szyfrowanego nawiązania komunikacji
---------------------------------------

.. code-block:: python
   :linenos:

   import smtplib
   from email.mime.text import MIMEText
   from email.mime.multipart import MIMEMultipart

   # Konfiguracja serwera SMTP Gmail
   smtp_server = 'smtp.gmail.com'
   smtp_port = 587

   # Dane logowania do konta Gmail
   email_address = 'twojadres@gmail.com'
   password = 'twojehaslo'


   # Utwórz połączenie z serwerem SMTP z użyciem TLS
   server = smtplib.SMTP(smtp_server, smtp_port)
   server.starttls()

   # Zaloguj się do konta Gmail
   server.login(email_address, password)


z szyfrowanym nawiązaniem komunikacji
--------------------------------------

.. code-block:: python
   :linenos:

   import smtplib
   from email.mime.text import MIMEText
   from email.mime.multipart import MIMEMultipart

   # Konfiguracja serwera SMTP Gmail
   smtp_server = 'smtp.gmail.com'
   smtp_port = 465

   # Dane logowania do konta Gmail
   email_address = 'twojadres@gmail.com'
   password = 'twojehaslo'

    # Utwórz połączenie z serwerem SMTP z użyciem SSL
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)

    # Zaloguj się do konta Gmail
   server.login(email_address, password)
