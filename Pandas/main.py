import numpy as np
import pandas as pd

data = {
    "Name": ["John", "Jane", "Jim", "Jill"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

dataframe = pd.DataFrame(data, index=["a", "b", "c", "d"])

dataframe["Position"] = ["Manager", "Developer", "Designer", "Developer"]

new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "City": "Pasig", "Position": "Intern"}])
dataframe = pd.concat([dataframe, new_row])

print(dataframe) 