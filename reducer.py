#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators.
http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

hduser@ubuntu:/usr/local/hadoop$ bin/hadoop jar contrib/streaming/hadoop-*streaming*.jar \
-file /home/hduser/mapper.py  \
-mapper /home/hduser/mapper.py \
-file /home/hduser/reducer.py   \
-reducer /home/hduser/reducer.py \
-input /user/hduser/gutenberg/* \
-D mapred.reduce.tasks=16\
-D mapred.local.dir=/tmp/local\
-output /user/hduser/gutenberg-output


"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print "%s%s%d" % (current_word, separator, total_count)
        except ValueError:
            # count was not a number, so silently discard this item
            pass

if __name__ == "__main__":
    main()