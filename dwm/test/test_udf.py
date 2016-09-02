def ex_udf(data, histObj):

    data['field1'] = 'goodvalue'

    return data, histObj

def sort_udf_1(data, histObj):

    data['field1'] = 'badvalue'

    return data, histObj

def sort_udf_2(data, histObj):

    data['field1'] = 'anotherbadvalue'

    return data, histObj
