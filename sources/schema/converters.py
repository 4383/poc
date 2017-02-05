def to_json(schema):
    json = {}
    for zone in schema['zones']:
        json.update({zone['zone'].name: {}})
        for section in zone['sections']:
            variables = {}
            for section in zone['sections'][section]:
                for entry in section.entries.all():
                    variables.update({entry.internal_name: entry.value})
            json[zone['zone'].name].update({section.name: variables})
    return json


def to_yaml(schema):
    yaml = ""
    for zone in schema['zones']:
        yaml += zone['zone'].name + ":<br>"
        for section in zone['sections']:
            for section in zone['sections'][section]:
                yaml += "<span style='padding-left:5em'>" + section.name + ":</span><br>"
                for entry in section.entries.all():
                    yaml += "<span style='padding-left:10em'>- " + entry.internal_name + ": " + entry.value + "<br>"
    return yaml
