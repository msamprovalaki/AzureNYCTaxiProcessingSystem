# AzureNYCTaxiProcessingSystem

## Overview

In recent years, the vast increase in mobile phone data has facilitated the development of applications. With the abundance of sensors in each device, there is now an enormous amount of information available. The challenge has shifted to processing and utilizing this information effectively.

To address the storage and processing of large datasets, numerous distributed frameworks have been developed. These frameworks leverage multiple simple computers for data storage and processing instead of relying on a large and costly server. Simultaneously, more companies are turning to cloud-based solutions for their data processing needs, with cloud providers offering ready-made solutions for storage, processing, analytics, pub-sub systems, and more.

This project focuses on utilizing the Microsoft Azure cloud platform to implement a data processing system for taxi trajectory data in New York City. Each CSV file corresponds to a month's worth of data, and at the end of the month, the system administrator is tasked with implementing queries on this data using tools provided by the Azure cloud environment.

## Implemented Queries on Databricks

The following queries have been implemented using Databricks, a cloud-based big data analytics platform:

### 1. Quarter-wise Taxi Trip Analysis

- Calculate the number of taxi trips starting in each quarter around the point (40.735923, -73.990294).

    ```
    {Q1}->300
    {Q2}->500
    ...
    ```

### 2. Detailed Trip Information

- Print details of trips that were longer than 1 km, lasted more than 10 minutes, and had more than two passengers.

### 3. Popular Hours and Starting Quarters

- For the trips from the previous question, print the top 5 most popular start hours and starting quarters.

    ```
    12:43 → 12pm
    ...
    ```

### 4. Streaming Implementation

- Implement the Quarter-wise Taxi Trip Analysis (Question 1) to work in streaming mode. Automatically trigger processing when a mini-batch of trips is uploaded to Azure Blob Storage, and store the results.

### 5. Geospatial Analysis

- Given a pair of coordinates, find the number of routes that started within a 5 km radius of that point and cost more than $10. Display the results hourly.

    ```
    10pm → 5
    ...
    ```

