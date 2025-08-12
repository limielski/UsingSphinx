# UsingSphinx
12.07.2025 How to use Sphinx, generate docs ...
## Lik zewnętrzny
źródło : `dalsza część <https://realpython.com/python311-exception-groups/>`_
to samo co [dalsza część](https://realpython.com/python311-exception-groups/)

## kod z pliku + numeracja

```rst
.. literalinclude:: code/multiple_exceptions.py
   :linenos:
   :tab-width: 4
```

## Odnosniki wewnetrzne
```rst
Polecane video :ref:`What Does if __name__ == "__main__" Mean in Python? <dunder0-0-video>`
```

`<dunder0-0-video>` jest etykietą, labelem oznaczająca, że odwołujemy sie do miejsca oznaczonego w jakimś innym pliku poprzez

`.. _dunder0-0-video:`

## Spis treści

```rst
.. toctree::
   :maxdepth: 2

   dunder-list-index
   dunder0-0
   dunder0-0-video
   dunder1-0
```

gdzie wymienione pozycje to nazwy plików
