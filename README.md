# SpanningTreeTest
A testing script and a set of tests for FLP Spanning Tree project

Extract into the same folder as Makefile and necessary source files. The script loads both, the output and
reference output files, line by line, sorts them alphabetically and joins the lines with a newline character. 
The comparison is done on the basis of string comparison.
The script expects executable flp18-log in the same folder.

#### Usage
To test implementation on set of tests, execute the following command:
    $ python SpanningTreeTest.py

To get average (based on 10 executions) run times of all input files, execute:  
    $ python SpanningTreeTest.py --times
