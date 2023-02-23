import pandas

# %sql memory

# result_df = %sql select * from '~/sample_data/credit_history.parquet' limit 100;

result_df.head()

result_df['my_new_column'] = result_df['mortgage_due'] + result_df['credit_card_due']

result_df.head()

result_df.to_parquet('~/data/my_semi_table1.parquet')
