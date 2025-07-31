# Notes

## 07/31/25
```
import pandas as pd
import ast

# Read CSV
df = pd.read_csv('input.csv')

# Convert string lists to Python lists
df['your_column'] = df['your_column'].apply(ast.literal_eval)

# Save back to CSV
df.to_csv('output.csv', index=False)
```

## 07/29/25
Creature sizes are stored as integers. 0 = Medium, -1 = Small. Stored as a list because some Ancestries can choose their size