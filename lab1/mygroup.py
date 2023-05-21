groupmates = [
{
	 "name": "Александр",
	 "surname": "Сытов",
	 "exams": ['БЖ', 'КПТ', 'ИТиП'],
	 "marks": [5, 5, 4]
},
{
	 "name": "Илья",
	 "surname": "Белкин",
	 "exams": ['Электротехника', 'ИТиП', 'КПТ'],
	 "marks": [5, 5, 3]
},
{
	 "name": "Александр",
	 "surname": "Якимов",
	 "exams": ['ИТиП', 'БЖ', 'АИС'],
	 "marks": [3, 3, 5]
}
]

def sortbyavg(avg, studlist):
    for i in studlist:
        if sum(i["marks"])/len(i["marks"]) >= avg:
            print(i["name"], i["surname"])
target = float(input("Введите средний балл: "))
sortbyavg(target, groupmates)
