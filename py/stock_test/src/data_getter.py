try:
    import argparse
    import traceback
    import os

    import yfinance as yf
    import pandas as pd
    import datetime

    import requests
    from requests_cache import CacheMixin, SQLiteCache
    from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
    from pyrate_limiter import Duration, RequestRate, Limiter

    class CachedLimiterSession(CacheMixin, LimiterMixin, requests.Session):
        pass

    def main():
        cli = argparse.ArgumentParser()
        [cli.add_argument(i) for i in ["period", "interval", "max_num"]]

        cli_args = cli.parse_args()
        
        session = CachedLimiterSession(
            limiter=Limiter(RequestRate(2000, Duration.SECOND*60*60)),
            bucket_class=MemoryQueueBucket,
            backend=SQLiteCache("yfinance.cache"),
        )

        tickers = [i.rstrip() for i in open("tickers/all.tk", "r")]

        for i in range(0, min(len(tickers), int(cli_args.max_num))):
            ticker_object = yf.Ticker(tickers[i], session=session)
            
            history = ticker_object.history(interval=cli_args.interval, period=cli_args.period)
            print("Got history for: " + tickers[i])
            history.to_csv("data/" + tickers[i] + ".csv", sep=",")
            print("Created history CSV for: " + tickers[i])

        return

    if __name__ == "__main__":
        main()
        print("data_getter.py terminated")
        os.system("pause")
except Exception as error:
            print(traceback.format_exc())
os.system("pause")