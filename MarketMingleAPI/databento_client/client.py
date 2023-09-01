# Import Libraries
import databento as db
import os
from dotenv import load_dotenv
from datetime import datetime

# Load .env File 
load_dotenv()

class DatabentoClient:
    def __init__(self, data_params):
        self.client = db.Historical()
        self.data_params = data_params

    def data_cost(self):
        cost = self.client.metadata.get_cost(
            dataset=self.data_params.dataset,
            symbols=self.data_params.symbols,
            schema=self.data_params.schema,
            start=self.data_params.start,
            end=self.data_params.end,
            stype_in = self.data_params.stype_in,
        )

        print(f"\nThe cost of this data pull will be ${cost}\n")

    def data_size(self):
        """
         Returns data size in GBs
        """
        size = self.client.metadata.get_billable_size(
            dataset=self.data_params.dataset,
            symbols=self.data_params.symbols,
            schema=self.data_params.schema,
            start=self.data_params.start,
            end=self.data_params.end,
            stype_in = self.data_params.stype_in,
        )

        print(f"\n Bytes: {size} | KB:{size/10**3} | MB: {size/10**6} | GB: {size/10**9}\n")

        return size/10**9

    def req_historical_data(self):
        """

        Use for all historical data requests. Based on the size of request streaming or batch download will be used.

        """
        if self.data_size() > 4:
            self.req_historical_data_batch()
        else:
            print("\n Data Below 4 GB : Streaming Data\n")
            
            # try:
            #     data = self.client.timeseries.get_range (
            #         dataset=self.data_params.dataset,
            #         symbols=self.data_params.symbols,
            #         schema=self.data_params.schema,
            #         start=self.data_params.start,
            #         end=self.data_params.end,
            #         stype_in=self.data_params.stype_in,
            #         stype_out="instrument_id",
            #     )
            #     df = data.to_df()
            #     print(df)

            # except db.BentoClientError as e:
            #     print(e)

    def req_historical_data_batch(self):
        """
        Called from req_historical_data if batch download required.
        """
        print("\n Data Above 4 GB : Batch Downloading Data\n")
        # try:
        #     details = self.client.batch.submit_job(
        #         dataset=self.data_params.dataset,
        #         symbols=self.data_params.symbols,
        #         schema=self.data_params.schema,
        #         start=self.data_params.start,
        #         end=self.data_params.end,
        #         encoding="dbn",
        #     )
        #     print(details)

        # except db.BentoClientError as e:
        #     print(e)

