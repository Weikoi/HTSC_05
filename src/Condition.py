class Condition(object):
    def __init__(self, attribute, relation, value, logic):
        self.attribute = attribute
        self.relation = relation  # == < > <= >= contains !=
        self.value = value
        self.logic = logic  # and/or
