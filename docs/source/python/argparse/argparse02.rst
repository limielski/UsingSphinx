ArgumentParser()
================

zestawienie argumentow
----------------------


+-----------------------+-------------------------------------------------------------+------+
| usage                 | Opis użycia prog. Wygenerowany na podstawie argum.          | None |
+-----------------------+-------------------------------------------------------------+------+
| description           | Tekst przed pomocą arg.                                     | None |
+-----------------------+-------------------------------------------------------------+------+
| epilog                | Tekst po pomocą arg.                                        | None |
+-----------------------+-------------------------------------------------------------+------+
| parents               | Lista obiektów `ArgumentParser` w parserze.                 | []   |
+-----------------------+-------------------------------------------------------------+------+
| formatter_class       | Klasa dostosowuje wyjście pomocy.                           | Help |
+-----------------------+-------------------------------------------------------------+------+
| prefix_chars          | Zbiór znaków, poprzedza opcjonalne arg.                     | '-'  |
+-----------------------+-------------------------------------------------------------+------+
| fromfile_prefix_chars | Znaki, poprzedzające pliki, z dodatkowymi arg.              | None |
+-----------------------+-------------------------------------------------------------+------+
| argument_default      | Globalna domyślna wartość dla arg.                          | None |
+-----------------------+-------------------------------------------------------------+------+
| conflict_handler      | Strategia rozwiązania sprzeczności między arg.              | 'erro|
+-----------------------+-------------------------------------------------------------+------+
| add_help              | Dodaje opcję `-h`/`--help` do parsera.                      | True |
+-----------------------+-------------------------------------------------------------+------+
| allow_abbrev          | Pozwala skr. długich opcji.                                 | True |
+-----------------------+-------------------------------------------------------------+------+
| version               | Określa wersję aplikacji po podaniu opcji `--version` / `-v`|      |
+-----------------------+-------------------------------------------------------------+------+
| exit_on_error         | Czy parser kończy działanie z info o błędzie.               | True |
+-----------------------+-------------------------------------------------------------+------+

przykład
--------

.. code-block:: python
   :linenos:

   import argparse

   parser = argparse.ArgumentParser(
      prog='PraceDomowe',
      description='Example of cli application using argparse module',
      epilog='Copyright (c) 2024 by Leszek Imielski'
   )

   parser.add_argument('path') # argument obowiązkowy
   parser.add_argument('target')
   parser.add_argument('-w', '--width', type=int, help='Width of the image', default=300)
   parser.add_argument('-e', '--height', type=int, help='width of the screen', default=300)
   parser.add_argument('--name', help='Name of the person')

   args = parser.parse_args()
   for arg in vars(args):
      print(arg, getattr(args, arg))
