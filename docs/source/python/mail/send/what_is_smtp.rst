SMTP
====

Co to jest SMTP?
SMTP to protokół używany do wysyłania wiadomości e-mail i, jak wiemy, Python udostępnia bibliotekę „ smtplib”
do interakcji z nim. Będąc importując bibliotekę i nawiązując połączenie z serwerem e-mail. Poniżej znajdują się
następujące kroki, aby wysłać e-maile:

Krok 1: Przede wszystkim należy zaimportować bibliotekę „smtplib”.

Krok 2: Po utworzeniu sesji będziemy używać jej instancji SMTP do enkapsulacji połączenia SMTP.

:python:`s = smtplib.SMTP('smtp.gmail.com', 587)`

Krok 3: W tym przypadku musisz przekazać pierwszy parametr lokalizacji serwera i drugi parametr używanego portu.
W przypadku Gmaila używamy portu o numerze 587.

Krok 4: Ze względów bezpieczeństwa przełącz teraz połączenie SMTP w tryb TLS. TLS (Transport Layer Security)
szyfruje wszystkie polecenia SMTP. Następnie, ze względów bezpieczeństwa i uwierzytelnienia, musisz przekazać
dane logowania do konta Gmail w instancji logowania. Kompilator wyświetli błąd uwierzytelnienia,
jeśli wprowadzisz nieprawidłowy identyfikator e-mail lub hasło.

Krok 5: Zapisz wiadomość, którą chcesz wysłać, w zmiennej, powiedzmy, wiadomość. Używając instancji sendmail()
wyślij wiadomość. sendmail() używa trzech parametrów: nadawca_email_id, odbiorca_email_id i message_to_be_sent.
Parametry muszą być w tej samej kolejności.
