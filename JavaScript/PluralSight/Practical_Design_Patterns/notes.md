# Practical Design Patterns


## What is a Design Pattern?

  * Many people write procedural spaghetti code in JS.
  * Let's avoid that

  * design patterns - tried and tested patterns for elegant implementations

  * All about problems and solutions

  Ex

| Problem       | Solution       |
| ------------- |-------------|
| Service layer      | module pattern |
| Overcomplicated Object Interface     | Facade Pattern |
| Visibility Into State Changes | Observer Pattern|

  * A design pattern is a proven concept
  * Not an obvious solution
  * It describes a relationship (9 times/10)
  * Significant human component
  * Good because it **allows us to avoid re-solving the same problem** and **gives us common vocabulary**

  ### Types of Patterns

  #### Creational Patterns

  * Deal with the creation of new instances of an object


1. Constructor
2. Module   
  *These 2 are only really 'design patterns' in JS*
3. Factory
4. Singleton

  #### Structural Patterns
    * Deal with the makeup of the actual objects themselves


1. Decorator
2. Facade
3. Flyweight

  #### Behavioral Pattern

    * How objects behave/interact


1. Command
2. Mediator
3. Observer

### Review of inheritance
  `Object.create(object.prototype)`

## Creational Design Patterns
  * Used to construct new Objects
  * Adapting creation to situation

### Constructor Pattern
  * Create new objects w object scope

  * In JS, putting `new` before any function call creates an object w said function as constructor, links to an object prototype, binds 'this' to new object scope, implicitly returns 'this'

  * Problem w/ declaring functions in JS constructor: function recreated with every instance

  * Solution: prototype, an encapsulation of properties that an object links to. Put methods on the prototype instead of directly in the object

### Module Pattern

  * a group of like methods
  * like a toolbox
  * Wrap in a function to create private variables
  * Usually only need one - to provide services (the methods)
  * Revealing Module pattern: Define methods outside of return value and only list methods in return, like documentations

### Factory Pattern

  * Pattern used to simplify object creation
  * Creates objects based on need - e.g. Repository creation

### Singleton

  * Pattern used to restrict an object to one instance of that object across the app
  * A singleton remembers the last time you used it and hands it back
  * Node uses CommonJS, which makes the creation of singletons a bit simpler
  * Since node caches a module when exported, exporting an invoked function gives
  you a singleton instance of that function's return value

## Structural Design patterns

* Concerned w/ how objects are made up and simplifying relationships b/t objects
