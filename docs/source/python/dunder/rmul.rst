.. _rmul:

rmul
====

https://www.geeksforgeeks.org/__rmul__-in-python/

For every operator sign, there is an underlying mechanism. This underlying mechanism is a special method that will be called during the operator action. This special method is called magical method. For every arithmetic calculation like +, -, `*`, /, we require 2 operands to carry out operator functionality.

Examples:

‘+’ ? ‘__add__’ method

‘_’ ? ‘__sub__’ method

‘*’ ? ‘__mul__’ method


As the article is limited to multiplication functionality, we will see about multiplication procedure here. To perform the multiplication functionality, we have to tie up the operator sign to either left/right operand. Before, going to __rmul__ method, we will see about __mul__ method, which helps us to understand multiplication functionality vividly.

__mul__()
^^^^^^^^^

Let’s take an expression x*y where x is an instance of a class A. To perform the __mul__ method, the operator looks into the class of left operand(x) for the present of __mul__ i.e., operator(*) will check the class A for the presence of ‘__mul__’ method in it. If it has __mul__ method, it calls x.__mul__(y). Otherwise, it throws the ‘TypeError: unsupported operands’ error message.

Example 1:
.. code-block::

   class Foo(object):

      def __init__(self, val):
         self.val = val

      def __str__(self):
         return "Foo [% s]" % self.val

   class Bar(object):

      def __init__(self, val):
         self.val = val

      def __str__(self):
         return "Bar [% s]" % self.val

   # Driver Code
   f = Foo(5)
   b = Bar(6)
   print(f * b)

`TypeError, unsupported operand type(s) for *: 'Foo' and 'Bar'`

In the above example, the first operand is f and its class Foo(). As Foo() has no __mul__ method, it doesn’t understand how to multiply. So, it will show up TypeError message. If we check the other class Bar(), even it has no __mul__ method. So, even if we reverse the multiplication to (b*f), it will throw the same error

Example 2: Lets add the __mul__ method in Foo class.

.. code-block::

   class Foo(object):

      def __init__(self, val):
         self.val = val

      def __mul__(self, other):
         return Foo(self.val * other.val)

      def __str__(self):
         return "Foo [% s]" % self.val

   class Bar(object):

      def __init__(self, val):
         self.val = val

      def __str__(self):
         return "Bar [% s]" % self.val

   # Driver Code
   f = Foo(5)
   b = Bar(6)
   print(f * b)


`Foo 30`


As it is already mentioned, the operator by default looks into the left operand’s class, and here it finds the __mul__ method. Now it knows what to do and resulted 30 f.__mul__(b) = 5.__mul__(6). If we reverse the multiplication to (b*f), it throws up the issue again, as it looks into left operand’s class(Bar()) which doesn’t have any __mul__ method. b.__mul__(f) will throws the issue as b’s class Bar() doesn’t have __mul__ method.

__rmul__
^^^^^^^^

A slight difference between __mul__ and __rmul__ is, Operator looks for __mul__ in left operand and looks for __rmul__ in right operand. For example, x*y. Operator looks for __rmul__ method in the y’s class definition. If it finds the __rmul__ method, it will show up with the result, otherwise throws the TypeError error message

Example 1: Let’s take the above example with a small modification.

.. code-block::

   class Foo(object):

      def __init__(self, val):
         self.val = val

      def __str__(self):
         return "Foo [% s]" % self.val


   class Bar(object):

      def __init__(self, val):
         self.val = val

      def __rmul__(self, other):
         return Bar(self.val * other.val)

      def __str__(self):
         return "Bar [% s]" % self.val

   # Driver code
   f = Foo(5)
   b = Bar(6)

   print(f * b)

`Bar 30`


In the above example, it assumes f*b as b.__rmul__(f) as __rmul__ method is present in Bar() class of the instance b. If we reverse the multiplication to (b*f). The notation will be f.__rmul__(b). If it doesn’t have __rmul__ method, it can’t understand what to notate and throws up TypeError message.’

These type of operators, that require 2 operands, it will by default carry both __mul__ and __rmul__ method. To perform multiplication with both normal and reverse multiplication, see the below example.

Example 2:


.. code-block::

   class Foo(object):

      def __init__(self, val):
         self.val = val

      def __str__(self):
         return "Foo [% s]" % self.val


   class Bar(object):

      def __init__(self, val):
         self.val = val

      def __rmul__(self, other):
         return Bar(self.val * other.val)

      def __mul__(self, other):
         return self.__rmul__(other)

      def __str__(self):
         return "Bar [% s]" % self.val


   # Driver Code
   f = Foo(5)
   b = Bar(6)

   print(b * f)
   print(f * b)


.. code-block::

   Bar [30]
   Bar [30]
