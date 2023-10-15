Itertools in Python 3, By Example
=================================

https://realpython.com/python-itertools/

Nazywano ją „klejnotem” i „najfajniejszą rzeczą w historii”, a jeśli o niej nie słyszałeś, oznacza to, że tracisz jeden z najwspanialszych zakątków standardowej biblioteki Pythona 3: itertools.

Istnieje kilka doskonałych zasobów pozwalających dowiedzieć się, jakie funkcje są dostępne w itertool smodule. Same dokumenty są doskonałym miejscem na rozpoczęcie . Podobnie jest z tym postem .

Rzecz w itertools tym, że nie wystarczy po prostu znać definicje funkcji, które zawiera. Prawdziwa siła tkwi w komponowaniu tych funkcji w celu stworzenia szybkiego, wydajnego pod względem pamięci i dobrze wyglądającego kodu.

W tym artykule przyjęto inne podejście. Zamiast przedstawiać itertools ci jedną funkcję na raz, skonstruujesz praktyczne przykłady, które mają zachęcić cię do „myślenia iteratywnego”. Ogólnie rzecz biorąc, przykłady zaczną się od prostych i stopniowo będą zwiększać złożoność.

Słowo ostrzeżenia: ten artykuł jest długi i przeznaczony dla średnio-zaawansowanych programistów Pythona. Zanim zagłębisz się w szczegóły, powinieneś mieć pewność, że używasz iteratorów i generatorów w Pythonie 3, wielokrotnego przypisania i rozpakowywania krotek. Jeśli tak nie jest lub chcesz odświeżyć swoją wiedzę, przed przeczytaniem dalej rozważ zapoznanie się z poniższymi informacjami:

* `Iteratory Pythona: wprowadzenie krok po kroku <https://dbader.org/blog/python-iterators>`_
* `Wprowadzenie do generatorów Pythona <https://realpython.com/introduction-to-python-generators/>`_
* Rozdział 6 `sztuczek w Pythonie: książka Dana Badera <https://www.amazon.co.uk/dp/1775093301/?tag=adnruk-21>`_
* `Wielokrotne przypisywanie i rozpakowywanie krotek poprawiają czytelność kodu Pythona <https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/>`_

* `Functions: Iterables and Iterators <https://realpython.com/lessons/functions-iterables-and-iterators/>`_