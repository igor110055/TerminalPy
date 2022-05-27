from dotenv import load_dotenv
from Database_SQL.aws_sql_connect import AWS_SQL, DummyData


# Connection
db_connection = AWS_SQL(load_dotenv)

def assets(connector,asset_config):
    urls_to_fetch = []
    for asset_id in asset_config:
        query =  f"SELECT live_data_url from {connector.DBNAME}.binance_assets WHERE id={asset_id}"
        connector.cursor.execute(query)
        table = connector.cursor.fetchall()
        urls_to_fetch.append({
                'url':table[0][0],
                'asset_id':asset_id
            })

    return urls_to_fetch

def return_all_asset_URLs(connector):
    # Connection
    db_connection = DummyData(load_dotenv)
    urls_to_fetch = []
    query =  f"SELECT * from {db_connection.DBNAME}.assets"
    db_connection.cursor.execute(query)
    table = db_connection.cursor.fetchall()
    urls_to_fetch.append({
            'URL':table[0][0],
            'Ticker': table[0][0],
            'Exchange': table[0][0]
        })
    return urls_to_fetch