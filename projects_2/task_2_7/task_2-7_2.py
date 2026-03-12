seqs = ["ATATACGCGTA", "CTTCGGNGGA"]

print('\n=== перебор последовательностей ===')
for sequence in seqs:
    print(f'\nполная последовательность: {sequence}')
    print('построчно:')
    for nucleotide in sequence:
        print(nucleotide)

print('\nцикл выполнен')