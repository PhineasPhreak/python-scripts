## python-scripts
**Resize the terminal with Python?**
```python
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=100))
```
