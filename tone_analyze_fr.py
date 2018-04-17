import urllib.request
#import urllib.parse
import json
import base64

#greeting and script usage
print('Tone Analyzer v2')
print("This script will allow you to interract with Watson Tone analyzer")
print('just type your sentence and Watson will automatically decrypt your tone')
print('Type \'quit\' to exit the program')
print('(Note that You can also find dialog results in the configured file path...)')
print('\nPress any key to Continue!')
input()

#end greeting

#Variable start
analyze_full_sentence=True #set it to true if you want to analyze the full sentence of false if overall content analyzis is required

write2file=False #Set to True if you want to also write result to file
file_path='/Users/elyes.fayache/Desktop/Watson/result_fr.txt' #Please check that file path is correct

username="a1c5416e-735d-4eb8-a0f8-b36607e594f4"
password="G7k0LVJ8Eror"
credential=username + ':' + password
credential=base64.b64encode(bytes(credential,'utf-8'))
credential=base64.b64decode(credential)

url="https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21"

headers={'Content-Type' : "application/json" # Don t delete it
        ,'Content-Language' : 'fr' #Comment this line if language is us
        ,'Accept-Language' : 'fr' #Comment this line if language is us
        }

#End variables

#Authentication
pwd_mgr=urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwd_mgr.add_password(None,url,username,password)
handler=urllib.request.HTTPBasicAuthHandler(pwd_mgr)
opener=urllib.request.build_opener(handler)
urllib.request.install_opener(opener)
#end authentication

#Open file to write
if write2file:
    try:
        file=open(file_path, 'w')  #Write to file
    except:
        print('Error opening file, exiting...')
        exit(1)
#End open file to write

#Starting the While loop
msg = input('msg: ')  # capturing new sentence

while(msg != 'quit'):

    values = {'text': msg
              }
    data = json.dumps(values)
    print("Sending: " + data)
    data = data.encode('utf-8')

    # Send request and retrieve answer
    req = urllib.request.Request(url, data, headers=headers)
    resp = urllib.request.urlopen(req)
    resp_body = json.load(resp)
    # end

    #print result to console and to file
    print('Tone Analyzer Result:')
    print(resp_body)  # print to console
    print('\n')

    if write2file:
      try: #Print result to a file
            file.write('msg:' + msg + '\n')
            file.write('Answer:' + json.dumps(resp_body,ensure_ascii=False) + '\n\n\n')
      except:
        print("Error writing to file, exiting...")
        exit(2)

    msg = input('msg: ')#capturing new sentence
#end while lopp

if write2file:
    try:
        file.close()
    except:
        print('Error closing file, exiting...')

print('\n Program exitted successfully...')

#EOF


