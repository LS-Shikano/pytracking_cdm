 ## API Reference

### Classes
 +[SeqAnaObj](#SeqAnaObj)

***SeqAnaObj***<a name="SeqAnaObj"></a>
Initializing this class transforms a folder of csv files containing row wise fixations to a dataframe of sequences and then generates a matrix of levenshtein distances from these sequences. 
#### Attributes
- seq_df: A pandas dataframe of one sequence per row per individual or trial, depending on params
- code_dct: Dictionary with the aoi labels as keys and their encoded sequence chars as values.
- distance_matrix: A numpy ndarray (matrix) of levenshtein distances.