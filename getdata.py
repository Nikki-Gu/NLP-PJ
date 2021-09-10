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

import requests
import json
from py2neo import Graph, NodeMatcher, Subgraph


def get_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    graph = Graph("http://localhost:7474", auth=("neo4j", "133122"))
    area = requests.get(url).json()
    data = json.loads(area['data'])
    all_counties = data['areaTree']
    for country_data in all_counties:
        if country_data['name'] != '中国':
            continue
        else:
            all_provinces = country_data['children']
            for province_data in all_provinces:
                province_name = province_data['name']
                all_cities = province_data['children']
                for city_data in all_cities:
                    tx = graph.begin()
                    matcher = NodeMatcher(graph)
                    m = matcher.match("City")
                    new_nodes = list(m)
                    for node in new_nodes:
                        # TODO 需要用正则表达式匹配，找到开头为citydata中name的节点，然后更新
                        if node['cname'] == city_data['name']:
                            node['NowConfirm'] = city_data['total']['nowConfirm']
                            node['Confirm'] = city_data['total']['confirm']
                            node['Suspect'] = city_data['total']['suspect']
                            node['Heal'] = city_data['total']['heal']
                            node['Dead'] = city_data['total']['dead']
                    sub = Subgraph(nodes=new_nodes)
                    # 调用push更新
                    tx.push(sub)
                    graph.commit(tx)


if __name__ == '__main__':
    get_data()
