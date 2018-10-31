
class Query:

    @classmethod
    def count(cls, other_cls):
        count = 0
        for item in other_cls.all():
            count += 1
        return count
    @classmethod
    def find_by_name(cls, other_cls, name):
        for item in other_cls.all():
            if item.name == name:
                return item
                break
    @classmethod
    def name_starts_with(cls, other_cls, letter):
        empty = []
        for item in other_cls.all():
            if item.name.startswith(letter):
                empty.append(item)
        return empty
    @classmethod
    def is_older_than(cls, other_cls, number):
        empty = []
        for item in other_cls.all():
            if item.age > number:
                empty.append(item)
        return empty

    @classmethod
    def mean_age(cls, other_cls):
        all_ages = list(map(lambda item: item.age, other_cls.all()))
        return sum(all_ages)/len(all_ages)
