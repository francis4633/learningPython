from jsonpath import jsonpath

data = {'key1': {'key2': {'key3': {'key4': {'key5': {'key6': {'python'}}}}}}}

#print(data['key1']['key2']['key3']['key4']['key5']['key6'])

#jsonpath的结果是列表，获取数据需要索引 [{'python'}]
print(jsonpath(data, '$.key1.key2.key3.key4.key5.key6')[0])
#$..key6 表示再根节点（$）内部（..）找key6
print(jsonpath(data, '$..key6')[0])
