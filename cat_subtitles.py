from itertools import groupby
import glob
onlyfiles =glob.glob("./*.txt")
print '\n'.join(sorted(onlyfiles))
raw_input()
# parses all .srt files in the folder and prints to screen (redirect to store)
lines = []
for file in sorted(onlyfiles):
  print file
  f = open(file, 'r')
  for line in f:
    lines.append(line.strip('\n'))
  
  
print '\n'.join(lines)
