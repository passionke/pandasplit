import pandas as pd
import numpy as np 
import pandasplit as ps
df = pd.DataFrame(np.random.randn(100, 4), columns ='A B C D'.split())
ps.split_by_count(df, "A", 3, "count")
