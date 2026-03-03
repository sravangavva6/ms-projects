"""
Basic unit tests for the HIGGS Spark ML pipeline.
These tests focus on data ingestion, schema validation,
and pipeline execution sanity checks.
"""

import pytest
from pyspark.sql import SparkSession
from pyspark.ml.feature import Imputer, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml import Pipeline
from pyspark.sql import functions as F


@pytest.fixture(scope="session")
def spark():
    spark = (
        SparkSession.builder
        .appName("HIGGS-Test-Pipeline")
        .master("local[*]")
        .getOrCreate()
    )
    yield spark
    spark.stop()


def test_data_loading(spark):
    df = (
        spark.read
        .option("header", "true")
        .option("sep", ",")
        .option("inferSchema", "true")
        .csv("HIGGS_small.csv")
    )
    assert df.count() > 0
    assert "label" in df.columns


def test_no_null_labels(spark):
    df = (
        spark.read
        .option("header", "true")
        .option("sep", ",")
        .option("inferSchema", "true")
        .csv("HIGGS_small.csv")
    )
    null_labels = df.filter(F.col("label").isNull()).count()
    assert null_labels == 0


def test_pipeline_fit(spark):
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

    assembler = VectorAssembler(
        inputCols=feature_cols,
        outputCol="features"
    )

    rf = RandomForestClassifier(
        featuresCol="features",
        labelCol="label",
        numTrees=10
    )

    pipeline = Pipeline(stages=[assembler, rf])

    model = pipeline.fit(df)
    assert model is not None
