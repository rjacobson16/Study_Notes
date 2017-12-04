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

