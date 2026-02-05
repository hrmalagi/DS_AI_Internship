contacts={"Vishwas":"9019949661","Pooja":"8618705702","Vachna":"9483935006"}
print(contacts)
contacts["Apoorva"]=9741750604
contacts["Vachna"]=7411388762
print(contacts)
exists=print(contacts.get("Vishwas"))
not_exists=print(contacts.get("Amogh",'Contact not found'))
for name,number in contacts.items():
    print(f'Contact:{name}|Phone:{number}')