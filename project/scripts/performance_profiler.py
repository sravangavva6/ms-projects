"""
Basic performance profiling for Spark ML pipelines.
"""

import time
from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("HIGGS-Performance-Profiler").getOrCreate()

    start = time.time()

    df = (
        spark.read
        .option("header", "true")
        .option("sep", ",")
        .option("inferSchema", "true")
        .csv("HIGGS_small.csv")
    )

    record_count = df.count()

    end = time.time()

    print("Performance Summary")
    print("-------------------")
    print(f"Total Records: {record_count}")
    print(f"Load & Count Time (seconds): {end - start:.2f}")

    spark.stop()

if __name__ == "__main__":
    main()
