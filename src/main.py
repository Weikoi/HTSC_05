from Condition import Condition
from Query import Query

if __name__ == '__main__':
    query1 = Query("Customers")
    query1.add_condition(Condition("Company name", "equals", "aaa", "None"))
    query1.add_condition(Condition("Contact title", "not equals", "bbb", "and"))
    query1.add_condition(Condition("Phone", "contains", "6", "or"))
    query1.to_sql()

    query2 = Query("Customers")
    query2.add_condition(Condition("Company name", "equals", "aaa", "None"))
    query2.to_sql()
