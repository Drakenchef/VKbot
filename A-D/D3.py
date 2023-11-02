import re


json = [
    '{"en": "Male", "es": "Macho"},',
    '{"en": "Female", "es": "Hembra"},',
    '{"en": "Population", "es": "Poblacion"},',
]
csv = []

for el in json:
    regex = re.compile('".*?"')
    res = regex.findall(el)
    res = [i for i in res if len(i) > 4]
    csv.append(res[0] + ";" + res[1])
print(*csv, sep='\n')
