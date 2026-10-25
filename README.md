# Low-Level-Design-Python

A collection of low-level design (LLD) implementations in Python. The repository focuses on popular design patterns (under the designs/ folder) and common LLD interview problems and similar real-world designs.

## Contents

- Design patterns (creational, structural, behavioral)
- LLD interview questions (e.g., parking lot, elevator, etc.)

## Folder Structure

```
designs/
	builder/
	decorator/
	facade/
	factory/
	observer/
	singleton/
	state/
	strategy/
```

Each pattern folder contains a small, runnable Python example.

## Design Pattern

Design patterns are reusable building blocks for solving common design problems.
## Design Patterns Index

### Creational Patterns
- Control how objects are created.
- [Builder](designs/builder/main.py): Use when an object has many optional fields or complex construction.
- [Factory](designs/factory/main.py): Use when callers should not care which concrete class gets created.
- [Singleton](designs/singleton/main.py): Use when you need a single global instance.

### Structural Patterns
- Deal with how objects are composed and connected.
- [Decorator](designs/decorator/main.py): Use when you need to add optional behavior at runtime without subclass explosion.
- [Facade](designs/facade/main.py): Use when you want to hide internal complexity behind a simple entry point.

### Behavioral Patterns
- Control how objects interact.
- [Strategy](designs/strategy/main.py): Use when you want to replace if/else logic with interchangeable behaviors.
- [Observer](designs/observer/main.py): Use when multiple components must react to a single event.
- [State](designs/state/main.py): Use when behavior depends on state and transitions get complex.


## How to Run

Use Python 3.10+ for any pattern:

```
python designs/<pattern>/main.py
```

Example:

```
python designs/factory/main.py
```

## Goals

- Provide concise, readable examples of common patterns.
- Keep implementations simple and interview-friendly.
- Add popular LLD problems with clean object models.

## License

MIT