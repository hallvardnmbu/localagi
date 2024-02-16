Local AGI (Artificial General Intelligence)
===========================================

Welcome to the Local AGI package! This is a fun project that simulates an Artificial General
Intelligence (AGI) running locally on your machine.

What is AGI?
------------

AGI is a type of artificial intelligence that has the ability to understand, learn, adapt, and
implement knowledge in a wide range of tasks, much like a human being. It's the holy grail of AI
research, aiming to create a machine with the ability to perform any intellectual task that a human
being can do.

Running localagi
----------------

Import the package through `pip install localagi`, and run it directly from the terminal by typing
`localagi`:

```
    pip install localagi

    localagi
```

Enjoy your journey with Local AGI!

Running through the terminal is the intended way to use Local AGI, but you can also use the Python
API as such:

```python
    import localagi

    localagi.load()

    question = "What is the meaning of life?"
    response = localagi.prompt(question)
```
