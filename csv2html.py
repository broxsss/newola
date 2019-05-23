from pathlib import Path
import pandas as pd 
import codecs
import os
relative = Path("")
absolute = relative.absolute()
print (absolute)
df = pd.read_csv(str(absolute)+"/newola/RecordingTestPlan.csv")
df.to_html(str(absolute)+'/newola/RecordingTestPlan.html')
fn=codecs.open(str(absolute)+"/newola/RecordingTestPlan.html", 'r')
m = fn.read()
#print (m)
f = open(str(absolute)+"/newola/index.html",'r')
filedata = f.read() # read contents
f.close() # closes file
filedata = filedata.replace("JOB_IS $BUILD_STATUS", m)
f = open(str(absolute)+"/newola/index.html",'w')
f.write(filedata)
f.close()