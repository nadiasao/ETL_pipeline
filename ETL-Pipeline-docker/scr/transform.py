def identify_remove_duplicates(df):
    if df.duplicated().sum() > 0:

        print('# of duplicated rows:', df.duplicated().sum())

        df_cleaned = df.drop_duplicates(keep='first')

        print(" shape of data before removing duplicates:", df.shape)
        print("shape of data after removing duplicates:", df_cleaned.shape)

    else:
        print("No duplicated data found")
        df_cleaned = df
    return df_cleaned