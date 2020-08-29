from Condition import Condition
from Query import Query

if __name__ == '__main__':
    query = Query("Customers")
    query.add_condition(Condition("Company name", "equals", "aaa", "None"))
    query.add_condition(Condition("Contact title", "not equals", "bbb", "and"))
    query.add_condition(Condition("Phone", "contains", "6", "or"))
    query.to_sql()
