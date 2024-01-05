import understand as ud

db = ud.open("/home/mehran/Desktop/test/src/src.udb")

print ("\n")

for entity in db.ents("class"):
    print(entity.longname())  # Changed variable names from 'class_entity' to 'entity'

class_count = len(db.ents("class"))  # Changed variable name 'res' to 'class_count'
print (f"\n\n******* Number of Classes: {class_count} *******\n\n")  # Changed string formatting slightly
