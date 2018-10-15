##pandasplit

split pandas data


## usage:

### split_by_value

```python
import pandas as pd

import pandasplit as ps

df = pd.DataFrame([1,1,2,2,2,3,4,5], columns=['A'])
x = ps.split_by_value(df, 'A', 2)
print(x)

```

### split_by_count

```python
import pandas as pd

import pandasplit as ps

df = pd.DataFrame([1,1,2,2,2,3,4,5], columns=['A'])
x = ps.split_by_count(df, 'A', 2)
print(x)

```