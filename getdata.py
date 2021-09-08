# 数据格式如下
"""
每一行中：
    0省份
    1城市
    2更新时间
    3目前确诊人数
    4累计确诊人数
    5疑似病例
    6死亡人数
    7死亡率
    9治愈人数
    10治愈率
    12风险评级
"""


import pandas as pd
import requests
import json


def get_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    area = requests.get(url).json()
    data = json.loads(area['data'])
    update_time = data['lastUpdateTime']
    all_counties = data['areaTree']
    all_list = []
    for country_data in all_counties:
        if country_data['name'] != '中国':
            continue
        else:
            all_provinces = country_data['children']
            for province_data in all_provinces:
                province_name = province_data['name']
                all_cities = province_data['children']
                for city_data in all_cities:
                    city_name = city_data['name']
                    city_total = city_data['total']
                    province_result = {'province': province_name, 'city': city_name,'update_time': update_time}
                    province_result.update(city_total)
                    all_list.append(province_result)

    df = pd.DataFrame(all_list)
    df.to_csv('/Users/mac/Desktop/自然语言处理PJ/数据获取/data.csv', index=False, encoding="utf_8_sig")


if __name__ == '__main__':
    get_data()
