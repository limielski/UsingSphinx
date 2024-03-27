Porty
=====

Porty 25 i 587 są oba standardowymi portami używanymi do przesyłania wiadomości e-mail, ale różnią się w tym, jak są używane i jakie mają restrkcje.

Port 25 jest tradycyjnym portem używanym do przesyłania wiadomości e-mail (protokół SMTP) od czasów, kiedy szyfrowanie nie było jeszcze powszechnie stosowane. Problemy zaczęły się pojawiać, gdy port 25 zaczął być nadużywany do wysyłania spamu i prowadzenia innych złosliwych działań.

Dlatego wiele usług internetowych (szczególnie usługodawcy Internetu) zaczęło blokować połączenia wychodzące na porcie 25 jako środek zapobiegawczy. To po części przyczyniło się do wprowadzenia portu 587.

Port 587 jest portem "Submission" (przesyłania), który został specjalnie zaprojektowany dla przesyłania wiadomości e-mail przez klientów pocztowych. Zasada działania portu 587 jest taka, że wymaga on autentykacji przed wysłaniem wiadomości e-mail, co pomaga zapobiegać nadużyciom.

Kolejną zaletą portu 587 jest to, że często jest używany do połączeń zabezpieczonych dzięki STARTTLS, co pomaga zabezpieczyć komunikację e-mail.

Podsumowując, port 587 ma następujące zalety w stosunku do portu 25:

* Wymaga autentykacji przed wysyłaniem wiadomości, co pomaga zapobiegać nadużyciom.
* Często jest używany do zabezpieczonych połączeń z metodą STARTTLS.
* Mniej prawdopodobne, że jest zablokowany przez dostawców internetowych z powodu nadużyć związanych z portem 25.
