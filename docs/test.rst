=====================
Test syntax highlight
=====================

Python:

.. code-block:: python

    #!/usr/bin/env python
    """Test file for Python syntax highlighting in editors / IDEs.
    Meant to cover a wide range of different types of statements and expressions.
    Not necessarily sensical or comprehensive (assume that if one exception is
    highlighted that all are, for instance).
    Extraneous trailing whitespace can't be tested because of svn pre-commit hook
    checks for such things.
    """
    # Comment
    # OPTIONAL: XXX catch your attention
    # TODO(me): next big thing
    # FIXME: this does not work

    # Statements
    from __future__ import with_statement  # Import
    from sys import path as thing

    print(thing)

    assert True  # keyword


    def foo():  # function definition
        return []


    class Bar(object):  # Class definition
        def __enter__(self):
            pass

        def __exit__(self, *args):
            pass

    foo()  # UNCOLOURED: function call
    while False:  # 'while'
        continue
    for x in foo():  # 'for'
        break
    with Bar() as stuff:
        pass
    if False:
        pass  # 'if'
    elif False:
        pass
    else:
        pass

    # Constants
    'single-quote', u'unicode'  # Strings of all kinds; prefixes not highlighted
    "double-quote"
    f"format {string}"
    """triple double-quote"""
    '''triple single-quote'''
    r'raw'
    ur'unicode raw'
    'escape\n'
    '\04'  # octal
    '\xFF'  # hex
    '\u1111'  # unicode character
    1  # Integral
    1L
    1.0  # Float
    .1
    1+2j  # Complex

    # Expressions
    1 and 2 or 3  # Boolean operators
    2 < 3  # UNCOLOURED: comparison operators
    spam = 42  # UNCOLOURED: assignment
    2 + 3  # UNCOLOURED: number operators
    []  # UNCOLOURED: list
    {}  # UNCOLOURED: dict
    (1,)  # UNCOLOURED: tuple
    all  # Built-in functions
    GeneratorExit  # Exceptions

Shell:

.. code-block:: sh

    #!/usr/bin/sh

    cat << EOF
    The current working directory is: $PWD
    You are logged in as: $(whoami)
    EOF

C++:

.. code-block:: cpp

    // 'Hello World!' program 
    
    #include <iostream>
    
    int main(){
        std::cout << "Hello World!" << std::endl;
        return 0;
    }

.. code-block:: cpp

    template<typename T> concept C1 = sizeof(T) != sizeof(int);
    
    template<C1 T> struct S1 { };
    template<C1 T> using Ptr = T*;
    
    S1<int>* p;                         // error: constraints not satisfied
    Ptr<int> p;                         // error: constraints not satisfied
    
    template<typename T>
    struct S2 { Ptr<int> x; };          // error, no diagnostic required
    
    template<typename T>
    struct S3 { Ptr<T> x; };            // OK, satisfaction is not required
    
    S3<int> x;                          // error: constraints not satisfied
    
    template<template<C1 T> class X>
    struct S4 {
    X<int> x;                         // error, no diagnostic required
    };
    
    template<typename T> concept C2 = sizeof(T) == 1;
    
    template<C2 T> struct S { };
    
    template struct S<char[2]>;         // error: constraints not satisfied
    template<> struct S<char[2]> { };   // error: constraints not satisfied

Javascript:

.. code-block:: js

    let person = 'Mike';
    let age = 28;

    function myTag(strings, personExp, ageExp) {
    let str0 = strings[0]; // "That "
    let str1 = strings[1]; // " is a "
    let str2 = strings[2]; // "."

    let ageStr;
    if (ageExp > 99){
        ageStr = 'centenarian';
    } else {
        ageStr = 'youngster';
    }

    // We can even return a string built using a template literal
    return `${str0}${personExp}${str1}${ageStr}${str2}`;
    }

    let output = myTag`That ${ person } is a ${ age }.`;

    console.log(output);
    // That Mike is a youngster.

.. code-block:: js

    let s = 'Please yes\nmake my day!'

    s.match(/yes.*day/);
    // Returns null

    s.match(/yes[^]*day/);
    // Returns ["yes\nmake my day"]

Rust:

.. code-block:: rust

    impl <A: TraitB + TraitC, D: TraitE + TraitF> MyTrait<A, D> for YourType {}

    // Expressing bounds with a `where` clause
    impl <A, D> MyTrait<A, D> for YourType where
        A: TraitB + TraitC,
        D: TraitE + TraitF {}

.. code-block:: rust

    use std::fmt::Debug;

    trait PrintInOption {
        fn print_in_option(self);
    }

    // Because we would otherwise have to express this as `T: Debug` or 
    // use another method of indirect approach, this requires a `where` clause:
    impl<T> PrintInOption for T where
        Option<T>: Debug {
        // We want `Option<T>: Debug` as our bound because that is what's
        // being printed. Doing otherwise would be using the wrong bound.
        fn print_in_option(self) {
            println!("{:?}", Some(self));
        }
    }

    fn main() {
        let vec = vec![1, 2, 3];

        vec.print_in_option();
    }

