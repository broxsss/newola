from pathlib import Path
import pandas as pd 
import codecs
import os
relative = Path("")
absolute = relative.absolute()
print (absolute)
df = pd.read_csv(str(absolute)+"/workspace/new/newola/RecordingTestPlan.csv")
df.to_html(str(absolute)+'/workspace/new/newola/RecordingTestPlan.html')
fn=codecs.open(str(absolute)+"/workspace/new/newola/RecordingTestPlan.html", 'r')
m = fn.read()
#print (m)
f = open(str(absolute)+"/workspace/new/newola/index.html",'r')
filedata = f.read() # read contents
f.close() # closes file
filedata = filedata.replace("replaceit2", m)
f = open(str(absolute)+"/workspace/new/newola/index.html",'w')
f.write(filedata)
f.close()