import pandas as pd 
from deep_translator import GoogleTranslator
import re
import sys

try:
    print("Translating .....")
    #importing a json file as a df
    #df = pd.read_json("main.json")
    df = pd.read_json(sys.argv[1])
    #transating all in the text list. 
    #REF: https://deep-translator.readthedocs.io/en/latest/usage.html#google-translate
    #df['translated'] = GoogleTranslator(source='auto', target='en').translate(df['text'])

    pattern = ", {.*"

    for i in range(len(df)):
        df.loc[i, 'text'] = re.sub("\[", '', str(df.loc[i, 'text']) )
        df.loc[i, 'text'] = re.sub("\\n", '', str(df.loc[i, 'text'] ))
        df.loc[i, 'text'] = re.sub(pattern, '', str(df.loc[i, 'text'] ))
        df.loc[i,'translated'] = GoogleTranslator(source='auto', target='en').translate(df.loc[i, "text"])
        #print(df.loc[i, "translated"])
        #trying to remove the crap after the text. There are more brackets going etc. Need to clean this. 

    df1 = df[['id','date','from','text','translated']]
    print("Done. check the output.csv")

    df1.to_csv('output.csv')

except:
    print("Bad input try the following syntax: python3 languages.py input.json")
    print("- Where input.json is the input file")