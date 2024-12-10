# Sort-Kudrna
import random

# Generování pole náhodných čísel v rozsahu 0-100 o délce 10
array = [random.randint(0, 100) for _ in range(10)]
print("Původní pole1:", array)

# Bubble sort procházení pole a výměna sousedních prvků, pokud nejsou ve správném pořadí
for i in range(len(array)):
    # Každá iterace zmenší rozsah kontrolovaných prvků
    for j in range(len(array) - 1 - i):
        if array[j] > array[j + 1]:
            # Výměna prvků
            array[j], array[j + 1] = array[j + 1], array[j]
print("Seřazené pole (bubble sort):", array)

# Generování pole náhodných čísel v rozsahu 0-100 o délce 5
arrayA = [random.randint(0, 100) for _ in range(5)]
print("Původní pole2:", arrayA)

# Bogo sort: náhodně přeskupujeme pole, dokud není seřazené
while arrayA != sorted(arrayA):  # Kontrola, zda je pole seřazené
    random.shuffle(arrayA)       # Náhodné promíchání prvků
print("Seřazené pole (bogo sort):", arrayA)

# Generování pole náhodných čísel v rozsahu 0-100 o délce 10
arrayB = [random.randint(0, 100) for _ in range(10)]
print("Původní pole3:", arrayB)

# Selection sort hledání nejmenšího prvku a jeho přesunutí na správnou pozici
for i in range(len(arrayB)):
    for j in range(i + 1, len(arrayB)):
        if arrayB[j] < arrayB[i]:
            # Výměna aktuálního prvku s nalezeným menším prvkem
            arrayB[i], arrayB[j] = arrayB[j], arrayB[i]
print("Seřazené pole (selection sort):", arrayB)

# Generování pole náhodných čísel v rozsahu 0-100 o délce 10
arrayC = [random.randint(0, 100) for _ in range(10)]
print("Původní pole4:", arrayC)

# Insertion sort postupné vkládání prvků na správné místo v seřazené části pole
for i in range(1, len(arrayC)):
    key = arrayC[i]       # Klíčový prvek k přesunutí
    j = i - 1
    # Posun větších prvků doprava
    while j >= 0 and key < arrayC[j]:
        arrayC[j + 1] = arrayC[j]
        j -= 1
    arrayC[j + 1] = key   # Vložení klíčového prvku na správné místo
print("Seřazené pole (insertion sort):", arrayC)
