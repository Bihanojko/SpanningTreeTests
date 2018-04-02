from __future__ import print_function
import os
import sys
import shutil
import subprocess
import commands


ITERATION_COUNT = 10

OutputFilepath = './Tests/Output/'
if not os.path.exists(OutputFilepath):
    os.makedirs(OutputFilepath)

InputFiles = os.listdir('./Tests/Input')
failures = 0

times = False
if len(sys.argv) >= 2 and sys.argv[1] == '--times':
    times = True

if not times:
    for idx, inputFile in enumerate(sorted(InputFiles)):
        sys.stdout.write('TEST ' + str(idx + 1) + ': ')
        os.system('./flp18-log < ./Tests/Input/' + inputFile + ' > ./Tests/Output/' + inputFile)

        with open('./Tests/Output/' + inputFile, 'r') as o:
            with open('./Tests/RefOutput/' + inputFile, 'r') as ro:
                oContent = '\n'.join(sorted([x for x in o.read().split("\n") if x.strip() != '']))
                roContent = '\n'.join(sorted([x for x in ro.read().split("\n") if x.strip() != '']))

                if oContent != roContent:
                    sys.stdout.write("\033[1;31m" + "FAIL!" + "\033[0;0m" + " (" + inputFile + ")\n")
                    failures += 1
                else: 
                    sys.stdout.write("\033[0;32m" + "SUCCESS!\n" + "\033[0;0m")

    print('\nAll tests checked, totalling ' + str(failures) + ' errors!')

else:
    elapsedTimes = [0] * ITERATION_COUNT
    for inputFile in sorted(InputFiles):
        for i in range(ITERATION_COUNT):
            output = commands.getstatusoutput('time ./flp18-log < ./Tests/Input/' + inputFile)[1].decode('utf-8').split('\n')
            elapsedTime = output[-3][5:]
            minutes = int(elapsedTime[:elapsedTime.find('m')])
            seconds = float(elapsedTime[elapsedTime.find('m') + 1:elapsedTime.find('s')])
            elapsedTimes[i] = minutes * 60 + seconds
        averageTime = sum(elapsedTimes) / float(ITERATION_COUNT)
        print("{0}\t{1}".format(inputFile, averageTime))
