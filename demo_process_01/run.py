import pandas

# %sql dwh

# result_df = %sql select product_id, category_name from products p left join categories c on p.category_id = c.category_id;

result_df.head()

result_df['my_new_column'] = result_df['mortgage_due'] + result_df['credit_card_due']

result_df.head()

result_df.to_parquet('~/data/my_semi_table1.parquet')
