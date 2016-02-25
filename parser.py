from itertools import groupby
import glob

def srt(file):
   subtitles = []
   # "chunk" our input file, delimited by blank lines
   with open(file) as f:
       res = [list(g) for b,g in groupby(f, lambda x: bool(x.strip())) if b]
       for element in res:
         subtitles.append(''.join(element[2:]))
   return subtitles

onlyfiles =glob.glob("./*.srt")

# parses all .srt files in the folder and prints to screen (redirect to store)
for file in sorted(onlyfiles):
  print ''.join(srt(file))
