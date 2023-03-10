import os
import glob
import uuid
import pandas as pd
import multiprocessing as mp


def process_file(path):
    df = pd.read_csv(
        path,
        names=['ticker', 'trade_date', 'open_price', 'low_price', 
            'high_price', 'close_price', 'volume']
    )
    df.to_json(
        f'data/nyse_all/nyse_json/part-{str(uuid.uuid1())}.json.gz',
        orient='records',
        lines=True,
        compression='gzip'
    )
    print(f'Number of records processed in {path} is {df.shape}')


def convert_files():
    os.makedirs('data/nyse_all/nyse_json', exist_ok=True)
    files = sorted(glob.glob('data/nyse_all/nyse_data/NYSE*.txt.gz'))
    with mp.Pool(4) as pool:
        pool.map(process_file, files)


if __name__ == '__main__':
    convert_files()