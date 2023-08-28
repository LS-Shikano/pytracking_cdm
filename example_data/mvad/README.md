## Source
McVicar, Duncan and Anyadike-Danes, Michael (2002). Predicting Successful and Unsuccessful Transitions from School to Work by Using Sequence Methods, Journal of the Royal Statistical Society. Series A (Statistics in Society), 165, 2, pp. 317–334. 

## Data Processing
```python
id_column = 'id'
months_columns = df.columns[df.columns.str.contains(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.\d{2}$')]
transposed_df = pd.melt(df, id_vars=[id_column], value_vars=months_columns, var_name='month', value_name='label')

print(transposed_df)
transposed_df['month'] = pd.to_datetime(transposed_df['month'], format='%b.%y')

```
