# Guide for Python

`[]  = schváleno`, `[x] = neschváleno`

## Inspirace

- https://github.com/realpython/python-guide

## Working with File System

It is strongly recommended to use the `pathlib` library.

## Module

### Pravidla

- Modul musí obsahovat informaci o kódování `# -*- coding: utf-8 -*-`.

- Modul musí obsahovat dokumentační komentář.

- Modul musí obsahovat magickou proměnnou `__all__` s exportovanými objekty.
  Proměnná `__all__` musí být zapsána jako n-tice a nesmí obsahovat objekty s názvem začínajícím podtržítkem.

    ```python
    __all__ = [...] # bad
    __all__ = (...) # good
    ```
  - `__all__` obsahuje jen třídy a funkce bez podtržítek.
    ```python
     __all__ = ("_Protected", "_protected")      # bad
     __all__ = ("CONSTANT", "Class", "function") # good
    ```
  - `__all__` obsahuje všechny třídy bez podtržítek, které jsou v modulu obsaženy.
  - `__all__` obsahuje jako poslední prvek `DONT_USE_WILD_IMPORT`.


 Tip: Pište názvy funkcí, tříd a konstant prefixované s podtržítkem, dokud není jasné, že jde o veřejnou funkci, kterou uvádíme v __all__.
 Je vždy snažší odebrat podtržítko než naopak zpětně neveřejné objekty doplnit podtržítkem. 

### String

Používej F-strings https://www.python.org/dev/peps/pep-0498/

### Členění modulu

```
# -*- coding: utf-8 -*-

""" Module documantation comment"""
 
__all__ = (function, class)

# Public objects

function
class

# Private objects

_function
_class
````


## Testování

- [] Používej balík [pytest](https://docs.pytest.org/en/latest/contents.html) pro psaní samostatných (jednotkových) testů.
- [] Používej modul [doctest](https://docs.python.org/3/library/doctest.html) pro prototypování a příklad, jak kód používat.
- [] 

## Formátování

- [] Používej balík [black](https://black.readthedocs.io/en/stable/) pro automatické formátování kódu. 

## Vytvoření projektu

## První věci k rozhodnutí

- Dělám knihovnu anebo aplikaci? 

### Základní struktura projektu (balíku)

Pro vytvoření balíčku použijeme např. *coockiecutter*.

Každý projekt obsahuje tyto adresáře a soubory:

- `README.{md|rst}`
- `LICENSE`
- `.editorconfig`
- `setup.py` + `setup.cfg`
- `.gitignore`
- `Pipfile` + `Pipfile.lock`
- `tests/`
- `pytest.ini`
- `examples/`

Použití *git hooks*.

## Vytvoření balíčku


## Testování (Pytest)

- Každá veřejná třída, metoda, funkce má dokumentační komentář.
- Každý dokumentační komentář je testován pomocí modulu doctest nebo pytest.

### `pytest.mark`

Pokud chceme použít modul-level marker:

```python
import pytest
pytestmark = pytest.mark.mymarkername
```

Spuštění provedeme 

```bash
py.test -m mymarkname
```

### `pytest.parametrize`


# Založení projektu

Pro založení projektu, vytvoření virtálního prostředí a správu závislostí používáme nástroj Pipenv https://poetry.eustace.io/
(Dříve jsme oužívali Pipenv, který se nám v mnoha ohledech neosvědčil). Tím se můžeme zbavit souborů setup.py, setup.cfg, MANIFEST a podobně 

- http://andrewsforge.com/article/python-new-package-landscape/


