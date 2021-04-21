# This script was written by Paxton on 5/29/2020 to pull all of the properties within a certain distance in [CITY].

import requests, os
import pandas as pd
from datetime import datetime
from API_Module.API_keypull import get_api_key
Realtor_API_Key = get_api_key('Realtor')

currentdate = str(datetime.now())
filename =('[CITY] Houses for Sale_') + currentdate[0:10] + '.xlsx'

def property_list_for_sale(api_key, city, state, prop_type, limit=300):
    url = "https://realtor.p.rapidapi.com/properties/v2/list-for-sale"
# What I'm sorting for in my response
    querystring = {"sort":"relevance",
                    "beds_min":"1",
                    "radius":"20",
                    "price_max":"200000",
                    "city":[CITY],
                    "limit":"300",
                    "offset":"0",
                    "state_code":[STATE],
                    "prop_type":"single_family",
                    "is_pending":"false"}
# Headers is where the API website, and Key are entered
    headers = {
        'x-rapidapi-host': "realtor.p.rapidapi.com",
        'x-rapidapi-key': Realtor_API_Key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json() # Json Format

# Function for taking the output of the API pull, and inserting it into a table
def process_list_for_sale_response(response_json):
    dataframe_list =[]
    # iterate through each sale listing
    for l in response_json['properties']:
        temp_df = pd.DataFrame.from_dict(l, orient='index').T
        dataframe_list.append(temp_df)
    return pd.concat(dataframe_list, axis=0, ignore_index=True, sort=False)

#Variables
city = [CITY]
state = [STATE]
prop_type = "single_family"

properties_for_sale_response = property_list_for_sale(api_key=Realtor_API_Key,city=city,state=state,prop_type=prop_type,limit=300)
# print(properties_for_sale_response)
df_properties_for_sale_raw = process_list_for_sale_response(response_json=properties_for_sale_response)
df_properties_for_sale_raw.to_excel(r'C:\Users\Paxton\Documents\A Home for Us\Realtor API\Properties for Sale Spreadsheets' +'/' +  filename, index = None, header = True)

# df_properties_for_sale_raw.head()
