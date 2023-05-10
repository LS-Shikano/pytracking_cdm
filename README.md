# pytracking-cdm
Package for internal use at the Center for Data and Methods. 

The package contains tools for doing sequence analysis on eyetracking fixation data.

## Getting Started
```bash
pip install pytracking-cdm
```

## Usage
To generate a distance matrix from a folder containing one csv per subject:
```python
from pytracking-cdm import SeqAnaObj
obj = SeqAnaObj("folder/path", id_col='id', aoi_col='aoi', sep_col='trial')
```

