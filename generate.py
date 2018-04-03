#!/usr/bin/env python3
import os
from subprocess import call


def rngame(*args, _out):
    call(["tools/rngame"]+[str(x) for x in args], stdout=_out)


def stgame(*args, _out):
    call(["tools/stgame"]+[str(x) for x in args], stdout=_out)


def generate_rngames(outdir, count, size, maxPrio, minOutDeg, maxOutDeg):
    for k in range(0, count):
        fn = "{}/rn-{}-{}-{}-{}-{}.pg".format(outdir, size, maxPrio, minOutDeg, maxOutDeg, k)
        if not os.path.isfile(fn) and not os.path.isfile(fn+".bz2"):
            with open(fn, "w+") as outfile:
                print("Generating random game {} with parameters {}, {}, {}, {}...".format(k, size, maxPrio, minOutDeg, maxOutDeg))
                rngame(size, maxPrio, minOutDeg, maxOutDeg, "x", _out=outfile)


def generate_stgames(count, size, minOutDeg, maxOutDeg, minInDeg, maxInDeg):
    print("Generating {} steady games with parameters {}, {}-{}, {}-{}...".format(count, size, minOutDeg, maxOutDeg, minInDeg, maxInDeg))
    for k in range(0, count):
        fn = "random/st-{}-{}-{}-{}-{}-{}.pg".format(size, minOutDeg, maxOutDeg, minInDeg, maxInDeg, k)
        if not os.path.isfile(fn):
            with open(fn, "w+") as outfile:
                stgame(size, minOutDeg, maxOutDeg, minInDeg, maxInDeg, _out=outfile)


if __name__ == "__main__":
    generate_rngames("random1", 20, 1000, 1000, 1, 1000)
    generate_rngames("random1", 20, 2000, 2000, 1, 2000)
    generate_rngames("random1", 20, 4000, 4000, 1, 4000)
    generate_rngames("random1", 20, 7000, 7000, 1, 7000)
    generate_rngames("random2", 20, 10000, 10000, 1, 2)
    generate_rngames("random2", 20, 20000, 20000, 1, 2)
    generate_rngames("random2", 20, 40000, 40000, 1, 2)
    generate_rngames("random2", 20, 70000, 70000, 1, 2)
    generate_rngames("random2", 20, 100000, 100000, 1, 2)
    generate_rngames("random2", 20, 200000, 200000, 1, 2)
    generate_rngames("random2", 20, 400000, 400000, 1, 2)
    generate_rngames("random2", 20, 700000, 700000, 1, 2)
    generate_rngames("random2", 20, 1000000, 1000000, 1, 2)
