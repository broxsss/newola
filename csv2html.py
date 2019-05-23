import pandas as pd 
import codecs
df = pd.read_csv("/Users/akshay.saini/.jenkins/workspace/new/newola/RecordingTestPlan.csv")
df.to_html('/Users/akshay.saini/.jenkins/workspace/new/newola/RecordingTestPlan.html')
fn=codecs.open("/Users/akshay.saini/.jenkins/workspace/new/newola/RecordingTestPlan.html", 'r')
m = fn.read()
#print (m)
f = open("/Users/akshay.saini/.jenkins/workspace/new/newola/index.html",'r')
filedata = f.read() # read contents
f.close() # closes file
filedata = filedata.replace("replaceit2", m)
f = open("/Users/akshay.saini/.jenkins/workspace/new/newola/index.html",'w')
f.write(filedata)
f.close()