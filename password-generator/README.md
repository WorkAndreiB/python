# Password generator

## Python imports explanation

- password-generator is the project/distribution directory.
- src is where Python source code lives.
- password_generator is the actual Python package

When I install the project, setuptools makes the package inside src importable.



```
from .pass_generator import generate_password
``` 
from inside __init__.py exposes generate_password function directly through password_generator package