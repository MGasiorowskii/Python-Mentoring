api = \
{
    "data": [1, 2, 'asd', [2, 3, 4, 5]],
    'nested_analysis':
    {
        'analysis_1': [1, 10, 15, 120.2, '120'],
        'analysis_2': [10, 100, 'test', 200, 300],
    },
    'probes': [['probe_1', 'probe_2'], 'probe_3']
}

print(api)

string = []

for element in api.values():
    if type(element) == dict:
        for data in element.values():
            for info in data:
                if type(info) == str:
                    string.append(info)
    else:
        for data in element:
            if type(data) == list:
                for info in data:
                    if type(info) == str:
                        string.append(info)
            else:
                if type(data) == str:
                    string.append(data)

print(string)
