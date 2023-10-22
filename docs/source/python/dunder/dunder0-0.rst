What Does if __name__ == "__main__" Do in Python?
=================================================

https://realpython.com/if-name-main-python/

Table of Contents

* In Short: It Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module
* How Does the Name-Main Idiom Work?
* When Should You Use the Name-Main Idiom in Python?
* When Should You Avoid the Name-Main Idiom?
* In What Way Should You Include the Name-Main Idiom?
* Is the Idiom Boilerplate Code That Should Be Simplified?
* Conclusion

----

Polecane video :ref:`What Does if __name__ == "__main__" Mean in Python? <dunder0-0-video>`

.. note::
   w środowisku kodu najwyższego poziomu wartość __name__zawsze wynosi "__main__". Środowisko kodu najwyższego poziomu to często moduł przekazywany do interpretera Pythona jako argument plikowy, jak widzieliśmy powyżej. Istnieją jednak inne opcje, które mogą stanowić środowisko kodu najwyższego poziomu:

   * Zakres monitu interaktywnego
   * Moduł lub pakiet Pythona przekazywany do interpretera Pythona z opcją -m, która oznacza moduł
   * Kod Pythona odczytywany przez interpreter Pythona ze standardowego wejścia
   * Kod Pythona przekazywany do interpretera Pythona z opcją -c, która oznacza polecenie

   Jeśli chcesz dowiedzieć się więcej o tych opcjach, zapoznaj się z dokumentacją Pythona, aby dowiedzieć się, czym jest środowisko kodu najwyższego poziomu . Dokumentacja ilustruje każdy z tych punktów za pomocą zwięzłego fragmentu kodu.


Python ustawia wartość :ref: `globalną<scope0-0#globals>` __name__ modułu na taką, "__main__"jeśli interpreter Pythona uruchamia Twój kod w środowisku kodu najwyższego poziomu :

.. note::
   „Kod najwyższego poziomu” to pierwszy moduł Pythona określony przez użytkownika, który zaczyna działać. Jest „najwyższego poziomu”, ponieważ importuje wszystkie pozostałe moduły potrzebne programowi. ( `Źródło <https://docs.python.org/3/library/__main__.html#what-is-the-top-level-code-environment>`_ )
