import urllib2
import time
import datetime
import os.path

stocksToPull = ('AAPL','TSLA')

def pullData(stock):
    try:
        print 'currently pulling', stock
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S' ))
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
        saveFileLine = stock +'.txt'
        
        print os.path.isfile(saveFileLine)
        
        if(os.path.isfile(saveFileLine)):
            try: 
                readExistingData = open(saveFileLine,'r').read()
                splitExisting = readExistingData.split('\n')
                mostRecentLine = splitExisting[-2]
                lastUnix = mostRecentLine.split(',')[0]
                print 'existing file...'
				
            except Exception,e:
                print 'opening file error',e
        else:
            lastUnix = 0
            print 'non-existing file...'
            
        saveFile = open(saveFileLine,'a')
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')
                                   
        for eachLine in splitSource:
            if 'values' not in eachLine:
                splitLine = eachLine.split(',')
                if len(splitLine) == 6:
                    if int(splitLine[0]) > int(lastUnix):
                        lineToWrite = eachLine + '\n'
                        saveFile.write(lineToWrite)
                    
        saveFile.close()
    
        print 'Pulled',stock
        print 'sleeping...'
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S' ))
        time.sleep(10)
    
        
    except Exception,e:
        print 'main loop',e

for eachStock in stocksToPull:
    pullData(eachStock)

print 'end of script'