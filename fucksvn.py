#encoding: utf-8
import re
import os
import sys

VERSION_RE = re.compile(ur'(r\d+)\s+\|')
AUTHOR_RE = re.compile(ur'\|\s+(\w+)\s+\|')

SVN_LOG_CMD = "svn.exe log"
SVN_CAT_CMD = "svn.exe cat"

def backtrack(file, regxp):
    versions = getVersionsByFile(file, reverse=True)
    for version in versions:
        v, author = version

        fh = os.popen("%s -%s %s" % (SVN_CAT_CMD, v, file), "r")
        content = fh.read()
        m = re.search(regxp, content)
        if m is not None:
            print "version: %s, author: %s" % (v, author)
            break

def getVersionsByFile(file, reverse=True):
    fh = os.popen("%s %s" % (SVN_LOG_CMD, file), "r")
    versions = []

    for line in fh:
        m = VERSION_RE.match(line)
        
        if m is not None:
            versions.append(
                (m.group(1), AUTHOR_RE.search(line).group(1))
            )
            
    if reverse: versions.reverse()

    return versions

if __name__ == "__main__":
    try:
        file, regxp = sys.argv[1:3]
        backtrack(file, regxp)
    except ValueError:
        print "usage: fucksvn.exe filename regxp"
