import cPickle
import numpy
### This is a very rudimentary script to kind of help with debugging this horrible test case
orig = numpy.load(open('results_2QO8-results_11032.pdb.cPickle.orig'))
new = numpy.load(open('results_2QO8-results_11032.pdb.cPickle'))


for i,j in zip(orig,new):
    if i != j:
        diff= numpy.array(i[2])-numpy.array(j[2])
        print diff
