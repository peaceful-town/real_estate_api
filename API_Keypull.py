import csv, sys
API_key_dict = {}
def get_api_key(api_key_id):
    """This code was written on 10/25/2020 and is used to pull my API keys from the API_Keys.csv without directly putting my API key into my script. """

    with open('C:/Users/[REDACTED]/Documents/pax_scripts/API_Module/API_Keys.csv') as api_file:
        i = 0
        api_reader = csv.reader(api_file, delimiter=',')#, fieldnames='API','API Key')
        next(api_reader)
        for row in api_reader:
            API_key_dict[row[0]] = row[1] # This creates a dict with all of the APIs, and their associated keys as the option
            # print(API_key_dict)

    try:
      API_key_dict[api_key_id] # get key by id
      if API_key_dict[api_key_id] == '':
          print('Idiot, the key value is empty')
      else:
          return API_key_dict[api_key_id]
    except KeyError:
      api_key_id_list = API_key_dict.keys()
      print('Cannot map key. Please verify if file exists, and that key is saved to file. Please see list of APIs below. ')
      print(api_key_id_list)
      return
# get_api_key(Realtor)
