import requests

api_url_all = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-063?Authorization=CWB-B28ED2C6-0A3F-40F5-AF0A-263D4631956E'

def retrieval_api(api_url):
  response = requests.get(api_url)
  # print('Status Code: ' + str(response.status_code))
  return str(response.json())

location_json = retrieval_api(api_url_all)

#print(location_json)
#print(type(location_json))

location_json = location_json.replace("\'", "\"")   # 將\'取代成\"
#print(location_json)

import json
location_dic = json.loads(location_json)   # 轉換成資料結構
#print(type(location_dic))
#print(location_dic)



country = location_dic['records']['locations'][0]['locationsName']
locationName = location_dic['records']['locations'][0]['location'][7]['locationName']
print(country + locationName + '天氣預報')

for i in range(7):
    startTime           = location_dic['records']['locations'][0]['location'][7]['weatherElement'][0]['time'][i]['startTime']
    endTime             = location_dic['records']['locations'][0]['location'][7]['weatherElement'][0]['time'][i]['endTime']
    Pop12h              = location_dic['records']['locations'][0]['location'][7]['weatherElement'][0]['time'][i]['elementValue'][0]['value']
    T                   = location_dic['records']['locations'][0]['location'][7]['weatherElement'][1]['time'][i]['elementValue'][0]['value']
    RH                  = location_dic['records']['locations'][0]['location'][7]['weatherElement'][2]['time'][i]['elementValue'][0]['value']
    MinCI               = location_dic['records']['locations'][0]['location'][7]['weatherElement'][3]['time'][i]['elementValue'][0]['value']
    WS                  = location_dic['records']['locations'][0]['location'][7]['weatherElement'][4]['time'][i]['elementValue'][0]['value']
    MaxAT               = location_dic['records']['locations'][0]['location'][7]['weatherElement'][5]['time'][i]['elementValue'][0]['value']
    Wx                  = location_dic['records']['locations'][0]['location'][7]['weatherElement'][6]['time'][i]['elementValue'][0]['value']
    MaxCI               = location_dic['records']['locations'][0]['location'][7]['weatherElement'][7]['time'][i]['elementValue'][0]['value']
    MinT                = location_dic['records']['locations'][0]['location'][7]['weatherElement'][8]['time'][i]['elementValue'][0]['value']
    UVI                 = location_dic['records']['locations'][0]['location'][7]['weatherElement'][9]['time'][i]['elementValue'][0]['value']
    UVILevel            = location_dic['records']['locations'][0]['location'][7]['weatherElement'][9]['time'][i]['elementValue'][1]['value']
    WeatherDescription  = location_dic['records']['locations'][0]['location'][7]['weatherElement'][10]['time'][i]['elementValue'][0]['value']
    MinAT               = location_dic['records']['locations'][0]['location'][7]['weatherElement'][11]['time'][i]['elementValue'][0]['value']
    MaxT                = location_dic['records']['locations'][0]['location'][7]['weatherElement'][12]['time'][i]['elementValue'][0]['value']
    WD                  = location_dic['records']['locations'][0]['location'][7]['weatherElement'][13]['time'][i]['elementValue'][0]['value']
    Td                  = location_dic['records']['locations'][0]['location'][7]['weatherElement'][14]['time'][i]['elementValue'][0]['value']
    
    info = '\n起始時間：' + str(startTime) \
        + '\n結束時間：' + str(endTime) \
        + '\n降雨機率：' + str(Pop12h) + '%' \
        + '\n平均溫度：' + str(T) + '度' \
        + '\n平均相對溼度：' + str(RH) + '%' \
        + '\n最小舒適度指數：' + str(MinCI) \
        + '\n最大風速：' + str(WS) + '公尺/秒' \
        + '\n最高體感溫度：' + str(MaxAT) + '度' \
        + '\n天氣現象：' + str(Wx) \
        + '\n最大舒適度指數：' + str(MaxCI) \
        + '\n最低溫度：' + str(MinT) + '度' \
        + '\n紫外線指數：' + str(UVI) + ' ' + str(UVILevel) \
        + '\n天氣預報綜合描述：' + str(WeatherDescription) \
        + '\n最低體感溫度：' + str(MinAT) + '度' \
        + '\n最高溫度：' + str(MaxT) + '度' \
        + '\n風向：' + str(WD) \
        + '\n平均露點溫度：' + str(Td) + '度'
    print(info)



'''
country = location_dic['records']['locations'][0]['locationsName']
locationName = location_dic['records']['locations'][0]['location'][7]['locationName']
print(country + locationName + '天氣預報')

for i in range(7):
    startTime = location_dic['records']['locations'][0]['location'][7]['weatherElement'][0]['time'][i]['startTime']
    endTime   = location_dic['records']['locations'][0]['location'][7]['weatherElement'][0]['time'][i]['endTime']
    print( '\n起始時間：' + str(startTime) + '\n結束時間：' + str(endTime) )
    for j in range(14):
        A = location_dic['records']['locations'][0]['location'][7]['weatherElement'][j]['time'][i]['elementValue'][0]['value']
        print( str(A) )
''' 




