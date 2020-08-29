class Query(object):
    def __init__(self, table_name):
        self.query_condition = []
        self.table_name = table_name

    def add_condition(self, condition):
        self.query_condition.append(condition)

    def to_sql(self):
        init_str = "SELECT * FROM " + str(self.table_name)
        where_flag = 0
        while self.query_condition:
            this_condition = self.query_condition.pop(0)
            if where_flag == 0:
                init_str += " WHERE"
                init_str += " "
                init_str += this_condition.attribute
                init_str += " "
                init_str += self.transfer(this_condition.relation)
                init_str += " "
                init_str += this_condition.value
                where_flag += 1
            else:
                where_flag += 1
                init_str += " "
                init_str += this_condition.logic
                init_str += " "
                init_str += this_condition.attribute
                init_str += " "
                init_str += self.transfer(this_condition.relation)
                init_str += " "
                init_str += this_condition.value
        print(init_str)
        return init_str

    @staticmethod
    def transfer(relation):
        if relation == "equals":
            return "="
        elif relation == "not equals":
            return "<>"
        elif relation == "<":
            return "<"
        elif relation == ">":
            return ">"
        elif relation == ">=":
            return ">="
        elif relation == "<=":
            return "<="
        elif relation == "contains":
            return "like"