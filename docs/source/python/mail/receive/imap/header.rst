Analiza nagłówkow
=================

.. code-block:: Python
   :emphasize-lines: 12
   :linenos:

   from email import message_from_bytes
   from email.header import decode_header

   raw_email = email_data[0][1]  # Pobieramy "surowy" email

   # Teraz przekształcamy surowy email na wiadomość, którą możemy czytać
   email_message = message_from_bytes(raw_email)

   # Teraz, gdy mamy przetworzony e-mail, możemy pobrać różne jego części
   from_header = email_message['From']
   to_header = email_message['To']
   subject_header = decode_header(email_message['Subject'])[0][0]

   # Wypiszmy te pola
   print('From:', from_header)
   print('To:', to_header)
   print('Subject:', subject_header)


Zauważ, że używamy funkcji :python:`decode_header` na nagłówku Subject. Pomaga to z pewnymi problemami z kodowaniem,
które mogą wystąpić, ponieważ temat e-maila jest często kodowany, aby obsługiwać różne znaki nie-ASCII.
Taką konwersję należy również zastosować do pól From i To jeśli w wiadomościach e-mail mogą występować znaki specjalne.

Pamiętaj też, że ten kod nie obsługuje wiadomości z załącznikami, HTML-em czy jakąkolwiek inną modyfikacją poza zwykłym
tekstem. Jeśli chcesz obsługiwać różne typy e-maili, musisz rozszerzyć ten kod o obsługę tych przypadków.
Możesz tego dokonać za pomocą metod dostępnych dla obiektów Message z modułu email.
Sprawdź dokumentację Python dla więcej szczegółów.

Funkcja :python:`message_from_bytes()`
--------------------------------------

Funkcja :python:`message_from_bytes()` z biblioteki :python:`email` Pythona konwertuje surową wiadomość e-mail z formatu bajtów na
obiekt wiadomości, który jest łatwiejszy do obsługi w Pythonie.

Gdy odbierasz wiadomość e-mail za pomocą `:python:imaplib`, surowa wiadomość jest odpowiedzią serwera IMAP i jest w formacie
bajtów (to znaczy sekwencja bajtów). Taka forma jest trudna do obsługi bezpośrednio, ponieważ e-mail może zawierać
wiele różnych części, takich jak nagłówki, ciała, załączniki, a każda z tych części może mieć inny format kodowania.
Funkcja message_from_bytes() przekształca tę surową sekwencję bajtów na obiekt :python:`email.message.Message`,
który umożliwia łatwe manipulowanie i odczytanie różnych części wiadomości e-mail.
Innymi słowy, :python:`message_from_bytes()` analizuje surową wiadomość e-mail i tworzy strukturę,
która odzwierciedla różne części wiadomości.

Funkcja :python:`decode_header()`
---------------------------------

Funkcja :python:`decode_header()` z biblioteki :python:`email.header` w Pythonie jest używana do dekodowania nagłówka e-maila.
Nagłówki e-maila, takie jak temat (Subject), mogą być zakodowane, jeśli zawierają znaki specjalne lub non-ASCII.
W szczególności, nagłówki często używają kodowania `MIME \"quoted-printable\"` lub `base64`, aby obsłużyć takie znaki.
Poniżej znajduje się szczegółowe wyjaśnienie, co robi ta linia kodu:

- :python:`email_message['Subject']` - Pobiera wartość nagłówka Subject z przetworzonego e-maila.
- :python:`decode_header(email_message['Subject'])` - Dekodowanie wartości nagłówka. Zwraca listę par (dekodowany_string, charset),

gdzie `charset` to kodowanie użyte dla tego fragmentu nagłówka. Jeśli wiadomość była zakodowana w kilku częściach,
zwrócona lista będzie miała wiele par. Jeśli wiadomość nie była zakodowana, charset będzie `None`.

- :python:`[0]` - Bierze pierwszą parę z listy. Jeśli wiadomość była zakodowana w kilku częściach, bierze tylko pierwszą część.
- :python:`[0]` - Z pary (dekodowany_string, charset), bierze tylko dekodowany_string, ignorując charset.

Więc ostatecznie, :python:`subject_header` będzie zawierać dekodowany ciąg znaków dla pierwszej części nagłówka Subject.
Jeśli e-mail ma bardziej skomplikowany nagłówek Subject (zakodowany w kilku częściach), ten kod nie będzie działać poprawnie.
Jeśli chcesz obsłużyć skomplikowane nagłówki, musisz zaimplementować obsługę dla nich przez iterowania przez listę
zwrotną z :python:`decode_header()` i dekodowanie każdej części.

Zdarza się, że nagłówek wiadomości e-mail zawiera tekst w kilku różnych zestawach znaków.
Na przykład, możesz mieć nagłówek \"Subject", który składa się z fragmentów w języku angielskim, rosyjskim i chińskim,
a każdy z tych fragmentów jest kodowany w różnych zestawach znaków. Dlatego, gdy taki nagłówek zostanie zdekodowany,
:python:`decode_header()` zwróci listę par, z których każda zawiera zdekodowany tekst i używany zestaw znaków.

Takie sytuacje są rzadkie, ale mogą się zdarzyć, szczególnie w przypadku wiadomości e-mail z międzynarodowymi treściami.
Poniżej znajduje się przykład zdekodowanego nagłówka, który składa się z kilku różnych części:

:python:`decoded_header = decode_header("=?utf-8?B?SGVsbG8gV29ybGQ=?= =?iso-8859-1?Q?Bonjour_Monde?= =?gb2312?B?aW5nbWFpbA==?=")`

gdy go zdekodujemy otrzymamy

:python:`[('Hello World', 'utf-8'), ('Bonjour Monde', 'iso-8859-1'), ('ingmail', 'gb2312')]`

Tak więc mamy trzy różne fragmenty tekstu, każdy w innym zestawie znaków.
W takich przypadkach będziemy musieli zaimplementować obsługę takich nagłówków poprzez iterację przez listę zwróconą z
:python:`decode_header()` i dekodowanie każdego fragmentu.

inna sprawa to:

jak wysyłać nagłówki zakodowane na kilka sposobów
-------------------------------------------------

by wysłać wiadomość e-mail z nagłówkiem \"Subject", który składa się z różnych części kodowanych w różnych zestawach
znaków, musisz użyć funkcji :python:`email.header.make_header()`. Poniższy kod pokazuje, jak to zrobić:

.. code-block:: Python
   :linenos:

   from email.header import make_header
   from email.mime.text import MIMEText
   import smtplib

   # Tworzenie nagłówka składającego się z tekstów w różnych zestawach znaków
   subject = make_header([('Hello World', 'utf-8'), ('Bonsoir Monde', 'iso-8859-1')])
   # Utwórz wiadomość MIME z nagłówkiem
   msg = MIMEText('This is the body of the email.')
   msg['Subject'] = str(subject)
   msg['From'] = 'me@example.com'
   msg['To'] = 'you@example.com'

   # Utwórz klienta SMTP i wyślij wiadomość
   s = smtplib.SMTP('localhost')
   s.send_message(msg)
   s.quit()

Oto krótkie wyjaśnienie, co robi ten kod:

:python:`make_header()` tworzy obiekt nagłówka, który składa się z kilku fragmentów w różnych zestawach znaków.
Każdy fragment to para (string, charset).

Funkcja :python:`MIMEText()` tworzy wiadomość e-mail, której ciało to ciąg znaków przekazany jako argument.
Aby przypisać nasz złożony nagłówek Subject do wiadomości, używamy :python:`msg['Subject'] = str(subject)`.
Tutaj musimy użyć :python:`str()` aby dokonać konwersji z `Header` do `string`.

Następnie tworzymy klienta SMTP, który połączy się z lokalnym serwerem i wyśle wiadomość.

Upewnij się, że już skonfigurowałeś swój serwer SMTP, zanim wyślesz wiadomość tym kodem.
Jeśli wysyłasz przez Gmail, użyj adresu 'smtp.gmail.com'. Klient SMTP może również wymagać uwierzytelnienia,
w zależności od konfiguracji serwera. Plus nie zapominaj, że musisz zabezpieczyć swoje dane logowania.

Pamiętaj również, że korzystając z funkcji Pythona do wysyłania e-maili, musisz być ostrożny, aby nie wysłać spamu
ani nie naruszać praw prywatności, co mogłoby być niezgodne z prawem i polityką twojego dostawcy usług e-mail.

Odbiorca wiadomości e-mail otrzyma wiadomość z nagłówkiem \"Subject" zawierającym oba ciągi znaków
`(\"Hello World" i \"Bonsoir Monde")`, które powinny być poprawnie wyświetlane w ich oryginalnych zestawach znaków,
pod warunkiem, że klient poczty e-mail odbiorcy obsługuje te zestawy znaków.

Jeśli klient poczty e-mail odbiorcy obsługuje zakodowanie UTF-8 i ISO-8859-1, odbiorca zobaczy temat e-maila jako
\"Hello World Bonsoir Monde". Przestrzenie między różnymi fragmentami zostaną dodane automatycznie.

Jeśli klient poczty e-mail odbiorcy nie obsługuje jednego lub obu zestawów znaków, może dojść do błędów wyświetlania.
W takim przypadku tekst może być wyświetlany w formie nieczytelnej lub zastąpiony znakami zastępczymi.

Warto tutaj zwrócić uwagę na fakt, że podczas korzystania z różnych zestawów znaków dla różnych części nagłówka,
idealne jest zastosowanie zestawów znaków, które są powszechnie obsługiwane przez większość klientów poczty e-mail,
takich jak UTF-8.

.. note::Jednak tego rodzaju wielokrotne kodowanie jest rzadko uzywane.
   Przeważnie większość nagłówków e-mail, w tym \"Subject", jest kodowana w jednym zestawie znaków, a UTF-8
   jest szczególnie popularne ze względu na swoją uniwersalność.

   UTF-8 jest w stanie zakodować praktycznie wszystkie znaki
   używane we wszystkich językach na świecie, a ponadto jest obsługiwany przez niemal wszystkie współczesne systemy i platformy.

   Kodowanie nagłówka e-maila, który składa się z fragmentów w różnych zestawach znaków, jest rzadko spotykane i zazwyczaj
   nie jest konieczne. Może to jednak mieć miejsce w określonych sytuacjach, na przykład jeśli autor e-maila naprawdę musi
   korzystać z konkretnych zestawów znaków dla różnych części wiadomości e-mail.

   Jednak nawet wtedy, może być trudne do obsługi zarówno dla autora (musi on odpowiednio skonfigurować swój klient poczty
   e-mail lub skrypt wysyłający wiadomość), jak i dla odbiorcy (jego klient poczty e-mail musi obsługiwać te wszystkie
   zestawy znaków). W związku z tym praktyka ta jest rzadko stosowana.
