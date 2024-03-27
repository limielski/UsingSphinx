Problemy
========


SSL: CERTIFICATE_VERIFY_FAILED
------------------------------


(ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)

Komunikat błędu to:

(ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)).

Błąd ten występuje, gdy nieudane jest nawiązanie połączenia SSL z powodu niepowodzenia weryfikacji certyfikatu SSL.
Zwykle dzieje się to, gdy próbujesz nawiązać bezpieczne połączenie z serwerem (w tym przypadku serwerem SMTP) i nie można zweryfikować certyfikatu SSL serwera.

Weryfikacja może się nie powieść z kilku powodów.

* Certyfikat może być samopodpisany
* wygasł
* wydany przez nieuznaną instytucję certyfikującą
* Twój system nie posiada niezbędnych certyfikatów do zatwierdzenia certyfikatu serwera itp.

Inną możliwością jest brak dostępu lokalnego środowiska Python do koniecznych certyfikatów głównych do walidacji certyfikatu serwera. Wydaje się, że uruchamiasz Python na macOS - Apple zmienił lokalizację systemowych certyfikatów głównych w jednym ze swoich aktualizacji, co może powodować ten błąd w module ssl Pythona.

Instalatory Python.org dla macOS zawierają własne kopie OpenSSL i dlatego nie używają systemowego magazynu certyfikatów, więc musisz zainstalować certyfikaty samodzielnie:

Rozwiązania problemu
--------------------

Instalacja certyfikatów w Pyhonie na mac os
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Otwórz Terminal i uruchom polecenie:

.. code-block:: bash

   `/Applications/Python\ 3.12/Install\ Certificates.command`

To polecenie używa skryptu instalacyjnego certyfikatów Pythona (dołączonego do instalatorów Python.org od wersji 2.7.9 i późniejszych, zobacz https://bugs.python.org/issue20916 dla kontekstu. Nie mają one dostępu do certyfikatów SSL systemu macOS, stąd ten dodatkowy krok).

Instalacja pakietu certifi

.. code-block:: bash

   pip3 install certifi

i nastepnie w kodzie programu umieść dodatkowo

.. code-block:: python
   :emphasize-lines: 1, 7, 9
   :linenos:

   import certifi

   sender = 'sender@email.com'
   receiver = 'receiver@email.com'
   password = 'password12345'

   context = ssl.create_default_context(cafile=certifi.where())

   with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
       server.login(sender, password)
       server.sendmail(sender, receiver, message)
       print("Email sent successfully")

Umieszczenie zmiennej w .bash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Rozwiązanie z StackOverflow: <https://stackoverflow.com/a/57795811/5503488>`_
Run this to set the appropriate variables.
This is a combination of the answers that have already been given here. Put it in your ~/.bash_profile to make it permanent.

.. code-block:: bash

   CERT_PATH=$(python -m certifi)
   export SSL_CERT_FILE=${CERT_PATH}
   export REQUESTS_CA_BUNDLE=${CERT_PATH}
