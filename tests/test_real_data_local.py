from pytracking_cdm import SeqAnaObj

def test_g_SeqAnaObj(path_real_data):
    obj = SeqAnaObj(
        path_real_data,
        id_col="participant_id",
        aoi_col="row_label",
        off_aoi_str="nan",
        merge=True
    )

    print(obj.seq_df)
    print(obj.code_dct)
    print(obj.distance_matrix)

