Co to jest SSL i TLS
====================

SSL (Secure Sockets Layer) i TLS (Transport Layer Security) to protokoły kryptograficzne używane do zapewnienia bezpieczeństwa komunikacji w sieci. Obie mają na celu zapewnienie bezpiecznej komunikacji między dwiema stronami przez sieć, taką jak Internet, poprzez szyfrowanie danych przesyłanych między nimi.

SSL to starsza wersja protokołu, która została opracowana przez firmę Netscape w latach 90-tych. Pierwotnie używane w przeglądarkach internetowych, SSL stało się standardem de facto dla bezpiecznej komunikacji w sieci. SSL 2.0 i 3.0 miały wiele znanych luk bezpieczeństwa.

TLS to następca protokołu SSL. Pierwszy protokół TLS 1.0, faktycznie był niewielkim upgrade'em SSL 3.0.
Od tamtej pory, TLS przeszedł wiele uaktualnień, najnowszą wersją jest TLS 1.3.

Główne różnice między SSL a TLS to:
-----------------------------------

* Poziom bezpieczeństwa: TLS zapewnia lepsze bezpieczeństwo niż SSL. Jest to wynikiem ulepszonych funkcji szyfrowania i funkcji hashowania.
* Szybkość handshake: Handshake TLS 1.3 jest szybszy niż handshake w TLS 1.2 lub SSL, ponieważ wymaga mniej rund komunikacji między klientem a serwerem.
* Wersje i kompatybilność: SSL jest starszą wersją protokołu, a najnowsze przeglądarki internetowe nie obsługują już SSL 2.0/3.0 z powodu luk bezpieczeństwa. TLS jest nowocześniejszy i jest obsługiwany przez wszystkie nowoczesne przeglądarki internetowe.

Podsumowując, oba protokoły zapewniają bezpieczne połączenie internetowe, ale TLS jest bezpieczniejszy i szybszy niż SSL.
W praktyce, terminy SSL i TLS są często używane zamiennie, ale rzeczywiste połączenia bezpieczne są zazwyczaj obsługiwane przez protokół TLS.

SSL/TLS a python
================

to jest tekst


.. note:: Nazwa SMTP_SSL w bibliotece Pythona może wprowadzać w błąd, ale faktycznie używa ona TLS, jeśli jest dostępny

   Większość nowoczesnych serwerów SMTP obsługuje TLS, więc kiedy używasz SMTP_SSL, faktycznie używasz TLS.
   Więc chociaż nazwa zawiera "SSL", w praktyce SMTP_SSL często oznacza "SMTP z TLS".

   Nalezy pamietac o uzywanych portach dla SSL lub TLS

   * smtp_port = 587  # TLS
   * smtp_port = 465  # SSL
