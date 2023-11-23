import psycopg2
import pandas as pd

def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect
def extract_transaction_data(dbname, host, port, user, password):
    # connect to redshift
    connect = connect_to_redshift(dbname, host, port, user, password)

    # query to extract online transactions data
    query = """SELECT ot.invoice,
                     ot.stock_code,
                     ot.quantity, 
                     ot.price, 
                     ot.price*ot.quantity as total_order_value,
                     cast(invoice_date as DateTime) as invoice_date,
                     ot.customer_id,
                     ot.country,
                     case when s.description is null then 'unknown'
                          else s.description end as description               
            from bootcamp.online_transactions ot
            left join (select *
                        from bootcamp.stock_description
                        where description <>'?') as s
                        on ot.stock_code=s.stock_code
            where ot.customer_id <>'' and ot.stock_code not in ( 'BANK CHARGES', 'POST','D','M','CRUK')"""
    online_trans_w_desc = pd.read_sql(query, connect)
    print(online_trans_w_desc.shape)

    return online_trans_w_desc
