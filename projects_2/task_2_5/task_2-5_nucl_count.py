dna_seq = input('введите последовательность ДНК: ')
dna_seq_up = dna_seq.upper()
print(f"\nпоследовательность в верхнем регистре: {dna_seq_up}\n")

# подсчет нуклеотидов
a_count = dna_seq_up.count('A')
t_count = dna_seq_up.count('T')
c_count = dna_seq_up.count('C')
g_count = dna_seq_up.count('G')

# длина последовательности
seq_length = len(dna_seq_up)

# процентное содержание нуклеотидов
a_percent = (a_count / seq_length) * 100
t_percent = (t_count / seq_length) * 100
g_percent = (g_count / seq_length) * 100
c_percent = (c_count / seq_length) * 100


# так называемый вывод
print('подсчет нуклеотидов:\n')
print(f'A: {a_count} ({a_percent:.2f}%)')
print(f'T: {t_count} ({t_percent:.2f}%)')
print(f'G: {g_count} ({g_percent:.2f}%)')
print(f'C: {c_count} ({c_percent:.2f}%)\n')

print(f'общая длина: {seq_length} нуклеотидов')