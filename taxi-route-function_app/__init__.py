from io import StringIO
import logging
import pandas as pd
import datetime
import azure.functions as func



def main(inputblob: func.InputStream, outputblob: func.Out[str]):
    logging.warning(f"Started processing file {str(inputblob.name)}")
    file_content = inputblob.read().decode("utf-8")
    df = pd.read_csv(StringIO(file_content)) 

    Q1, Q2, Q3, Q4 = 0, 0, 0, 0
    center_lat = 40.735923
    center_lon = -73.990294

    for i in range(len(df)):
        rec_lon, rec_lat = df.iloc[i]["pickup_longitude"], df.iloc[i]["pickup_latitude"]
        if (rec_lon > center_lon and rec_lat > center_lat):
            Q1 += 1
        elif(rec_lon <= center_lon and rec_lat > center_lat):
            Q2 += 1
        elif(rec_lon > center_lon and rec_lat <= center_lat):
            Q3 += 1
        else:
            Q4 += 1
    
    outputblob.set(f"File uri: {str(inputblob.uri)}\nQ1: {str(Q1)} \nQ2: {str(Q2)} \nQ3: {str(Q3)} \nQ4: {str(Q4)}")
    logging.warning(f"Q1: {str(Q1)} \nQ2: {str(Q2)} \nQ3: {str(Q3)} \nQ4: {str(Q4)} \nFinished processing file {str(inputblob.name)}")    
