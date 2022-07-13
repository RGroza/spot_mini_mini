import time
import math
from datetime import datetime
import struct
import sys
import os
import fnmatch
import argparse
from time import sleep
import csv


def readLogFile(filename, verbose=True):
    f = open(filename, 'rb')

    print('Opened'),
    print(filename)

    keys = f.readline().decode('utf8').rstrip('\n').split(',')
    fmt = f.readline().decode('utf8').rstrip('\n')

    # The byte number of one record
    sz = struct.calcsize(fmt)
    # The type number of one record
    ncols = len(fmt)

    with open(filename + '.csv', 'w', encoding='UTF8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(keys)

        if verbose:
            print('Keys:'),
            print(keys)
            print('Format:'),
            print(fmt)
            print('Size:'),
            print(sz)
            print('Columns:'),
            print(ncols)

        lenChunk = sz
        log = list()
        chunkIndex = 0
        while (lenChunk):
            check = f.read(2)
            lenChunk = 0
            if (check == b'\xaa\xbb'):
                mychunk = f.read(sz)
                lenChunk = len(mychunk)
                chunks = [mychunk]
                if verbose:
                    print("num chunks:")
                    print(len(chunks))

                for chunk in chunks:
                    print("len(chunk)=", len(chunk), " sz = ", sz)
                    if len(chunk) == sz:
                        print("chunk #", chunkIndex)
                        chunkIndex = chunkIndex + 1

                        values = struct.unpack(fmt, chunk)
                        if values[2] == 1:
                            writer.writerow(values)

                        record = list()
                        for i in range(ncols):
                            record.append(values[i])
                            if verbose:
                                print("    ", keys[i], "=", values[i])

                        log.append(record)
            else:
                print("Error, expected aabb terminal")
        return log


numArgs = len(sys.argv)

print('Number of arguments:', numArgs, 'arguments.')
print('Argument List:', str(sys.argv))

all_fileNames = os.listdir('logs')
if len(all_fileNames) != 0:
    logIDs = []
    for f in all_fileNames:
        if f[-4:] != ".csv":
            logIDs.append(int(f[3]))
else:
    print("No files found!")
    exit()

if "log" + str(max(logIDs)) + ".csv" not in all_fileNames:
    if (numArgs > 1):
        fileName = sys.argv[1]
    else:
        fileName = "logs/log" + str(max(logIDs))

    print("Creating: " + fileName + ".csv\n")

    verbose = False

    readLogFile(fileName, verbose)
else:
    print("File already converted!")
