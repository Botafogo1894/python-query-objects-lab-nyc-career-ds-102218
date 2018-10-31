from person import Person
from query import Query

jeff = Person("Jeff", 31)
molly = Person("Molly", 24)
kevin = Person("Kevin", 38)
rachel = Person("Rachel", 27)
devin = Person("Devin", 25)
michelle = Person("Michelle", 33)
jeff2 = Person("Jeff", 33)

Query.find_by_name(Person, "Jeff") == Person.find_by_name("Jeff")
Person.count() == Query.count(Person)
Query.name_starts_with(Person, "M") == Person.name_starts_with("M")
Person.is_older_than(30) == Query.is_older_than(Person, 30)
Query.mean_age(Person)  == Person.mean_age() 
