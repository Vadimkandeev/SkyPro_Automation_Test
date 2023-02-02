from smartphone import Smartphone


# создание списка
catalog = []
 
# наполнение списка
catalog.append(Smartphone("Xiaomi", "Redme NOTE 9 pro", "+71111111111"))
catalog.append(Smartphone("Honor", "20 S", "+72222222222"))
catalog.append(Smartphone("Motorola", "Razor Z3", "+73333333333"))
catalog.append(Smartphone("Siemens", "С 35", "+74444444444"))
catalog.append(Smartphone("Nokia", "3310", "+75555555555"))

for i in range(len(catalog)):
    catalog[i].print_list()




