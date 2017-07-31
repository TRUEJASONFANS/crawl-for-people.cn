import urllib2
import sys
class HtmlDownloader(object):
    
    def __init__(self):
        self.type = sys.getfilesystemencoding();
        
    def download(self, url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:
            return None
        data = response.read();
 
        data = data.decode("GBK")
        print data
        return data.encode('utf-8')
    
    



