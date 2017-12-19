import pandas,os
import googlemaps

df=pandas.read_csv("supermarkets.csv")
df["Address"]=df["StreeetNo"]+", "+df["StreetName_Suffix"]+", "+df["Municipality"]

gmaps_key=googlemaps.Client(key="AIzaSyBPVG1UE-3VOQM0Lg39kErgsKVtNdlL7us")

df["Latitude"]=None
df["Longitude"]=None
for i in range(len(df)):
    ans=gmaps_key.geocode(df.iat[i,8])
    try:
        lat=ans[0]["geometry"]["location"]["lat"]
        lon=ans[0]["geometry"]["location"]["lng"]
        df.iat[i,df.columns.get_loc("Latitude")]=lat
        df.iat[i,df.columns.get_loc("Longitude")]=lon
    except:
        lat=None
        lon=None

df.to_csv('result.csv', sep=',', encoding='utf-8')
