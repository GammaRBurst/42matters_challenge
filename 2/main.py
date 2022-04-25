# -*- coding: utf-8 -*-
"""Task 2: word count."""


__version__ = '1.0'
__author__ = 'GammaRayBurst'


import os

from pyspark import SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as F


def main() -> None:
    # Create configuration to download from AWS S3.
    conf = SparkConf()
    conf.set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.2.0')
    conf.set(
        'spark.hadoop.fs.s3a.aws.credentials.provider',
        'org.apache.hadoop.fs.s3a.AnonymousAWSCredentialsProvider'
    )

    # Create Spark session.
    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    # Download data frame.
    df = spark.read.text('s3a://products-42matters/test/biographies.list.gz')

    # Include only lines that begin with 'BG:',
    # separate all text at every whitespace,
    # write every word on a different line,
    # get rid of the lines.
    df = df \
        .filter(df.value.startswith('BG:')) \
        .withColumn('value', F.split('value', r'\s')) \
        .select('*', F.explode('value').alias('exploded_value')) \
        .drop('value')

    # Exclude all words that are empty strings and 'BG:',
    # group them by word,
    # count them,
    # sort them in descending order.
    word_count = df \
        .filter(df.exploded_value != 'BG:') \
        .filter(df.exploded_value != '') \
        .groupBy('exploded_value') \
        .count() \
        .sort('count', ascending=False)

    # Export result into CSV file.
    if os.path.isdir('result'):
        # Execution in Docker.  The 'result' directory can be set to export
        # the file to the host.
        word_count.toPandas().to_csv('result/word_count.csv', index=False)
    else:
        # Execution in local machine.
        word_count.toPandas().to_csv('word_count.csv', index=False)
    return None


if __name__ == '__main__':
    main()
