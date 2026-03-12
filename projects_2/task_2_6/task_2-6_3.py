donor = input("введите группу крови донора (A, B, AB, O): ").strip().upper()
recipient = input("введите группу крови пациента (A, B, AB, O): ").strip().upper()

# совместимы?
if donor == "O":
    print(f"переливание возможно: донор {donor} → пациент {recipient}")
elif donor == "A" and (recipient == "A" or recipient == "AB"):
    print(f"переливание возможно: донор {donor} → пациент {recipient}")
elif donor == "B" and (recipient == "B" or recipient == "AB"):
    print(f"переливание возможно: донор {donor} → пациент {recipient}")
elif donor == "AB" and recipient == "AB":
    print(f"переливание возможно: донор {donor} → пациент {recipient}")
else:
    print(f"переливание невозможно: донор {donor} → пациент {recipient}")