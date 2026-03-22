import pandas as pd
from dataguardian import diagnose

data = {
    "user_id": [1, 2, 3, 4, 5],
    "age": [22, 35, 28, 40, 30],
    "salary": [32000, 75000, 48000, 88000, 61000],
    "target": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

diagnose(df, target="target")