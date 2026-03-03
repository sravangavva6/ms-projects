#!/bin/bash
# Environment setup for HIGGS Big Data Pipeline

echo "Setting up environment variables..."

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
export SPARK_HOME=/opt/spark
export HADOOP_HOME=/opt/hadoop

export PATH=$SPARK_HOME/bin:$HADOOP_HOME/bin:$JAVA_HOME/bin:$PATH

echo "JAVA_HOME=$JAVA_HOME"
echo "SPARK_HOME=$SPARK_HOME"
echo "HADOOP_HOME=$HADOOP_HOME"

echo "Environment setup complete."
