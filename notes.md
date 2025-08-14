# Notes

## 8/13/25
```
df.to_csv('filename.csv', index=False)  # index=False avoids saving the index as a column
```

## 07/31/25
```python
import pandas as pd
from ast import literal_eval

# Read the TSV file
df = pd.read_csv('your_file.tsv', sep='\t')

# Convert the string lists to actual lists
df['your_column'] = df['your_column'].apply(literal_eval)

# Save back to TSV if needed
df.to_csv('output_file.tsv', sep='\t', index=False)
```


~~going to have to use string manipulation to create/read usable lists from the csv files. Using ";" as in-cell separaters.~~

## 07/29/25
Creature sizes are stored as integers. 0 = Medium, -1 = Small. Stored as a list because some Ancestries can choose their size