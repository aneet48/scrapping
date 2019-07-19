import xmlrpclib
import urllib2
from datetime import date
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[96m'

def get_url_content(url):
        try:
            content = urllib2.urlopen(url)
            return content.read()
        except Exception as e:
            print('error! '+e)

def uploadFile(url):
    try:
        # print bcolors.OKBLUE+'---- uploading media '+url+bcolors.ENDC
        xfileType = 'image/jpeg'
        file_url = url
        extension = file_url.split(".")
        leng = extension.__len__()
        extension = extension[leng-1]
        if (extension == 'jpg'):
            xfileType = 'image/jpeg'
        elif(extension == 'png'):
            xfileType = 'image/png'
        elif(extension == 'bmp'):
            xfileType = 'image/bmp'

        file = get_url_content(file_url)
        file = xmlrpclib.Binary(file)
        server = xmlrpclib.Server('http://wp.test//xmlrpc.php')
        filename = str(date.today())+str(time.strftime('%H:%M:%S'))
        mediarray = {'name': filename+'.'+extension,
                    'type': xfileType,
                    'bits': file,
                    'overwrite': 'false'}
        xarr = ['1', 'admin', 'redefine123', mediarray]
        result = server.wp.uploadFile(xarr)
        # print bcolors.OKBLUE+'---- media uploaded at ' + result['url']+bcolors.ENDC
        return result
    except Exception as e:
        print(e)


