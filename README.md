# EarlwarDataManager

Example local_settings.py
```python
import os
from EarlwarDataManager.settings import *
PATH = "C:/work/Earlwar/Assets/_Project/Resources/Data/"
STATICFILES_DIRS = STATICFILES_DIRS + [os.path.join(PATH, 'JSONSchemas')]