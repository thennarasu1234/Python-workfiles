# key-value pairs storing
#allows duplicate
#this is mutable(value)

dict_1={}
dict_2=dict()
type(dict_2)

# key-value pairs

dict_3={"nirmal":"Python class",0:[1,2,4,5,6]}
dict_3["nirmal"]
# mutable
dict_3["nirmal"]="Completed class"
print(dict_3)
dir(dict_3)

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

dict_1 = {"name":"thenn", "Rno":123,"course":"BE"}
print(dict_1)

# copy

dict_1 = {"name":"thenn", "Rno":123,"course":"BE"}
dict_1.copy()

# clear


dict_1 = {"name":"thenn", "Rno":123,"course":"BE"}
dict_1.clear()
print(dict_1)

# keys

dict_1 = {"name":"thenn", "Rno":123,"course":"BE"}
dict_1.keys()


# values

dict_1 = {"name":"thenn", "Rno":123,"course":"BE"}
dict_1.values()
dict_1.get("name")
dict_1.get("Rno")

# pop

dict_1 = {"name":"thenn", "Rno":123,"course":"BE","name":"ajay"}
dict_1.pop("ajay","not found")
print(dict_1)
dict_1.popitem()

# fromkeys

dict_2 = {"name":"thenn", "Rno":123,"course":"BE"}
dict_2.fromkeys("name","thenn")
a = ("b","c","d")
dict_2.fromkeys(a,"abc")

# update

dict_1 = {"name":"thenn", "Rno":123,"course":"BE"}
print(dict_1)
{"name": "thenn"}
dict_1.update({"Rno":123,"course":"BE"})
print(dict_1)

# setdefault
dict_3 = {"name":"thenn", "Rno":123,"course":"BE"}
print(dict_3)
{"name": "thenn", "course": "BE"}
dict_3.setdefault("Rno",123)

# get

dict_3= {"name":"thenn", "Rno":123,"course":"BE"}
print(dict_3)
print(dict_3.get("name"))


# items

dict_1 = {"name":"thenn", "Rno":123,"course":"BE"}
print(dict_1.items())
