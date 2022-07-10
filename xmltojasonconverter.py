import os 
import xmltodict,json  
PATH = "/home/kornbotdev/Automaticsoftware/mcu/"
TARGET = "/home/kornbotdev/Automaticsoftware/mcus/"
mcuextract = os.listdir(PATH) # Get list of the path dir 

def changenamealternative(dir,inputmcus):
          if "(" in list(inputmcus):  # Verify is there any bracket in the list splitter 
              if ")" in list(inputmcus): 
                           type1 = inputmcus.split(")")[0].split("(")[0] + inputmcus.split(")")[0].split("(")[1].split("-")[0] + inputmcus.split(")")[1].split(".")[0]+".json"
                           type2 = inputmcus.split(")")[0].split("(")[0] + inputmcus.split(")")[0].split("(")[1].split("-")[1] + inputmcus.split(")")[1].split(".")[0]+".json"
                           print(type1,type2)
                           #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                           stm32writer = open(dir+type1,'a')   # Write the json file converted from the xml to json in the target directory 
                           print(json.dumps(obj))
                           stm32writer.write(json.dumps(obj))   # Write the file into the directory 
                           #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                           stm32writer = open(dir+type2,'a')   # Write the json file converted from the xml to json in the target directory 
                           print(json.dumps(obj))
                           stm32writer.write(json.dumps(obj))   # Write the file into the directory 
for i in range(0,len(mcuextract)):
    print(mcuextract[i])
    try:
        if mcuextract[i].split(".")[1] == 'xml':
             stm32data = open(PATH+mcuextract[i],'r')  # Get the mcus data from the directory extraction 
             obj = xmltodict.parse(stm32data.read()) # extract and convert to dictionary 
             #print(obj)
             changenamealternative(TARGET,mcuextract[i]) 

             """
             stm32writer = open(TARGET+mcuextract[i].split(".")[0]+".json",'a')   # Write the json file converted from the xml to json in the target directory 
             print(json.dumps(obj))
             stm32writer.write(json.dumps(obj))   # Write the file into the directory 
             """ 
    except: 
        print("Now splitting.....",mcuextract[i])
    if i == len(mcuextract): 
          print("Converting complete.....")    