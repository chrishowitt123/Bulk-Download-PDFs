import requests
import time

filenames = pd.read_excel('filenamesnew.xlsx')
filenames = filenames['New']
filenames = filenames.tolist()

url_list = dfurl['URLS'].tolist()

b = 0

for url in pdf_list:
    a = url
    
    r = requests.get(a, stream=True)
    
    #time.sleep(10)
    

    with open(filenames[b], 'wb') as f:
        f.write(r.content)
        
        b = b+1
