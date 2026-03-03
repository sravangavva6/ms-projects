"""
Run Spark-based ML pipeline for HIGGS dataset classification.
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.ml.feature import Imputer, VectorAssembler, StandardScaler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml import Pipeline

def main():
    spark = SparkSession.builder.appName("HIGGS-Pipeline").getOrCreate()

    df = (
        spark.read
        .option("header", "true")
        .option("sep", ",")
        .option("inferSchema", "true")
        .csv("HIGGS_small.csv")
    )

    feature_cols = [f"f{i}" for i in range(1, 29)]

    imputer = Imputer(
        inputCols=feature_cols,
        outputCols=feature_cols,
        strategy="median"
    )

    df = imputer.fit(df).transform(df)

    df = df.withColumn(
        "energy_interaction",
        F.col("f1") * F.col("f2") * F.col("f3")
    )

    all_features = feature_cols + ["energy_interaction"]

    assembler = VectorAssembler(
        inputCols=all_features,
        outputCol="features_raw"
    )

    scaler = StandardScaler(
        inputCol="features_raw",
        outputCol="features",
        withStd=True
    )

    rf = RandomForestClassifier(
        featuresCol="features",
        labelCol="label",
        numTrees=50
    )

    pipeline = Pipeline(stages=[assembler, scaler, rf])

    train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

    model = pipeline.fit(train_df)

    preds = model.transform(test_df)
    preds.select("label", "prediction").show(10)

    spark.stop()

if __name__ == "__main__":
    main()
