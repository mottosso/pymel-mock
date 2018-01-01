# pymel-mock

Accelerate Maya start-up time and prevent accidental use.

- [Download](https://raw.githubusercontent.com/mottosso/pymel-mock/master/pymel.py)

<br>

### About

Launching Maya takes about 20 seconds on a modern machine, PyMEL is responsible for half of that time.

If you aren't using PyMEL, then this mock can..

1. Accelerate Maya start-up time by 10 seconds
2. Prevent your artists from growing a dependency on it

**Normal Maya session**

```python
import pymel.core as pm
pm.createNode("transform")
```

**Mocked Maya session**

```python
import pymel.core as pm
pm.createNode("transform")
# AttributeError: 'module' object has no attribute 'createNode' # 
```

Notice how it still imports, but doesn't carry any of the relevant members around.

<br>

### Usage

Maya needs to know that *this* `pymel` is the one to import.

```python
import sys
sys.path.insert(0, "/path/to/pymel-mock")
import pymel
```

> To avoid PEP8 warning E402, you can use `__import__()` instead.

Alternatively, you may try one of `pymel.py` on in one of these locations.

- `PYTHONPATH`
- `<documents>/maya/scripts`
- Anywhere, and add parent directory to `Maya.env`

**Example**

```bash
$ wget https://raw.githubusercontent.com/mottosso/pymel-mock/master/pymel.py
$ set PYTHONPATH=%cd%;%PYTHONPATH%
$ c:\program files\autodesk\maya2018\bin\maya.exe
```

**However** keep in mind Maya may scramble `sys.path`, making *this* `pymel.py` appear after the one shipped with Maya. The former approach is safest.

<br>

### Limitations

Up till Maya 2017, PyMEL was a bundled bystander to Maya. But lately, some of Maya is written using it; most notably MASH. If you use MASH, then this mock will disable some of its functionality.

<br>

### Todo

Rather than permanently eliminate all of PyMEL, it'd be better to import it only when it is actually being used. Originally, PyMEL performs initialisation on import, which is what's causing the added startup time. But if that initialisation could instead happen on first call to any member, then it'd only happen when relevant.