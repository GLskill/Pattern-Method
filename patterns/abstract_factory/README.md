# The ABS Factory method

#### The ABC (Abstract Base Classes) Factory Method is a design pattern used in object-oriented programming (OOP) to create objects without specifying the exact class of object that will be created. It falls under the creational design patterns category. This pattern provides an interface for creating objects, but allows subclasses to alter the type of objects that will be created.

Here's how the ABC Factory Method pattern typically works:

Abstract Factory Interface: An abstract class or interface defines the method(s) to create objects. This interface does not provide the implementation of these methods, but only declares their signatures.

Concrete Factories: Concrete classes implement the abstract factory interface. Each concrete factory provides a specific implementation for creating objects.

Product Interface: An abstract class or interface defines the common interface for the objects created by the factory methods.

Concrete Products: Concrete classes implement the product interface. These are the actual objects that are created by the factory methods.

Client: The client code interacts with the factory methods through the abstract factory interface. It does not need to know the exact class of objects being created, only the factory interface.