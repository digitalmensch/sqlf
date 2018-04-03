import typeguard


################################################################################
# Text Processing
################################################################################

@typeguard.typechecked
def match(string1 : str, string2 : str) -> bool:
    import re
    return list(re.findall('[a-z0-9]+', string1.lower())) == \
           list(re.findall('[a-z0-9]+', string2.lower()))
