total = int(input('введите общее кол-во произведенных капсул: '))
pack = int(input('введите кол-во капсул в одной упаковке: '))

full_pack = total // pack
remain = total % pack

print('\n--- отчет фасовочного цеха ---')
print(f'полных упаковок:\t{full_pack}')
print(f'остаток капсул:\t\t{remain}')