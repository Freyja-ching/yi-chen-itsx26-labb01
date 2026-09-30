# Jag använde mina tidigare anteckningar från Programmering nivå 1.
# Funktionen räknar hur många loggrader som innehåller "ERROR".
def count_errors(loggrader):
    count = 0

    for line in loggrader:
        if "ERROR" in line:
            count += 1

    return count

# Jag lärde mig denna funktion med hjälp av AI.
# Den öppnar loggfilen och läser in alla loggrader till en lista.
with open("onsdag.example.log", "r") as file:
    loggrader = file.readlines()

antal_errors = count_errors(loggrader)
print("Antal ERROR: ", antal_errors)
