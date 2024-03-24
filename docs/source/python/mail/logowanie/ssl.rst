Logowanie SSL
=============

Używanie kontekstu
------------------

Korzystanie z kontekstu SSL, zwłaszcza gdy używasz python:`smtplib.SMTP_SSL`, jest zalecane w celu zapewnienia bezpieczeństwa połączenia. Kontekst SSL umożliwia ustawienie dodatkowych opcji zabezpieczeń, takich jak weryfikacja certyfikatu, co może być kluczowe dla zapewnienia autentyczności i integralności połączenia.

Oto kilka sytuacji, w których warto użyć kontekstu SSL:

1. **Weryfikacja certyfikatu**: Jeśli chcesz, aby Twój kod weryfikował certyfikat serwera SMTP, co pomaga w zapobieganiu atakom typu Man-in-the-Middle (MitM).

2. **Ustawianie niestandardowych parametrów zabezpieczeń**: Kontekst SSL umożliwia ustawienie niestandardowych parametrów, takich jak niestandardowe ścieżki do certyfikatów, protokoły SSL/TLS dozwolone lub wyłączone, itp.

3. **Zabezpieczenie połączenia**: Używanie kontekstu SSL z python:`smtplib.SMTP_SSL` pomaga w zapewnieniu, że połączenie z serwerem SMTP jest zabezpieczone już na początku.

W przykładzie, który podałeś, python:`context` jest tworzony z użyciem python:`ssl.create_default_context()`, który domyślnie uwzględnia certyfikaty CA zainstalowane w systemie, a także korzysta z biblioteki `certifi`, aby dodać pewność, że certyfikaty CA są aktualne i zgodne z najnowszymi standardami bezpieczeństwa. Następnie ten kontekst SSL jest używany w połączeniu z python:`smtplib.SMTP_SSL` wewnątrz bloku python:`with` dla zapewnienia bezpiecznego połączenia z serwerem SMTP.

Więc ogólnie rzecz biorąc, kontekst SSL jest przydatny, gdy chcesz zapewnić bezpieczne połączenie z serwerem SMTP i/lub skonfigurować niestandardowe opcje zabezpieczeń.

.. code-block:: python
   :emphasize-lines: 10, 12
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
   context = ssl.create_default_context(cafile=certifi.where())
   # Utwórz połączenie z serwerem SMTP z użyciem SSL
   server = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context)

   # Zaloguj się do konta Gmail
   server.login(email_address, password)

bez uzycia kontekstu
--------------------

Wyróżnione dwie linie zastepujemy tylko jedną, wyrzucając utworzenie zmiennej :python:`context` i usuwając parametr
:python:`context` z funkcji w drugiej wyróżnionej linii kodu.

czyli cały kod wygląda nastepująco:

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
