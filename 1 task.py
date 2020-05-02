data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]
res = {}
for i in data:
    if i['city'] in res:
        res[i['city']].append({'name': i['name'], 'age': i['age']})
    else:
        res[i['city']] = [{'name': i['name'], 'age': i['age']}]
for i in res:
    print(i, res[i])
