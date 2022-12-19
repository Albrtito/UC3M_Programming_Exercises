from city import City

ci = City(20,20)
ci.create_streets()
ci.create_snowplows()
ci.snow(100)
a = ci.streets_to_clean()
print("Streets to clean:\n" + a)
ci.clean_street()
a = ci.streets_to_clean()
print("Streets not cleaned:\n" + a)