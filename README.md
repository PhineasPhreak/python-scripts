## python-scripts
### Documentation :
Python Packages : [Pypi.org](https://pypi.org/)<br>
Python Doc : [Docs Python 3 and 2.7](https://docs.python.org/3/)<br>

**Resize the terminal with Python?**
```python
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=100))
```
