# Notes

# 8/22/2025
Source for the table of contents code: https://discuss.streamlit.io/t/table-of-contents-widget/3470/8

## 3pm
Need to use line breaks `<br>` for the descriptions of the class features

## 3:30 - LLM Code
```
i = 0
while i < list_len:
    # Create a new row of columns, max 2 columns
    if i + 1 < list_len:
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**{names_list[i]}**")
            st.markdown(features_list[i], unsafe_allow_html=True)

        with col2:
            st.write(f"**{names_list[i+1]}**")
            st.markdown(features_list[i+1], unsafe_allow_html=True)
            
        i += 2
    else:
        # Handle the case where there's an odd number of items
        col1, _ = st.columns([1, 1])
        with col1:
            st.write(f"**{names_list[i]}**")
            st.markdown(features_list[i], unsafe_allow_html=True)
            
        i += 1
```

### How It Works
Looping with while: Instead of a for loop, a while loop is used to give you more control over the iteration step. The index i is manually incremented inside the loop.

Creating Column Pairs: The code first checks if there are at least two items left to display (i + 1 < list_len).

If true, it creates two columns with st.columns(2) and assigns them to col1 and col2.

It then places the data for names_list[i] and names_list[i+1] into col1 and col2 respectively.

The index is then incremented by 2 (i += 2) to move on to the next pair.

Handling Odd Numbers: The else block handles the scenario where there's an odd number of items in the list. In this case, only one column is created, and the final item is displayed within it.


## 8/18/2025
The iterrows() method returns a tuple for each row: (index, row_data)


## 8/13/25
```
df.to_csv('filename.csv', index=False)  # index=False avoids saving the index as a column
```


| PC Level | Attribute Limit |
| -------- | --------------- |
| 1        | 3               |
| 5        | 4               |
| 10       | 5               |
| 15       | 6               |
| 20       | 7               |


| Proficiency Level | Proficiency Bonus |
| ----------------- | ----------------- |
| 1 – Novice        | +2                |
| 2 – Adept         | +4                |
| 3 – Expert        | +6                |
| 4 – Master        | +8                |
| 5 – Grandmaster   | +10               |


| Character Level | Proficiency Level Limit |
| --------------- | ----------------------- |
| 1               | Novice                  |
| 5               | Adept                   |
| 10              | Expert                  |
| 15              | Master                  |
| 20              | Grandmaster             |



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