__author__ = 'shleger'

import os
import re
import subprocess

handlePath = "d:/bin/handle.exe"
handler = "coverage.xml"

p = subprocess.Popen([handlePath, handler], stdout=subprocess.PIPE)
out, err = p.communicate()
print "Process dump with: " + handlePath
for i in out.splitlines():
    # print(i)
    m = re.search('pid:\s+(\d+)\s+type: File\s+(\w+):', i)
    if m:
        binPid = m.group(1)
        hexPid = m.group(2)
        execLine = handlePath + " -c " + hexPid + " -p " + binPid
        print execLine
        # os.system(execLine)  TODO uncomment
print "done."







