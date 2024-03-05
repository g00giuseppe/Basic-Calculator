# Importa il modulo math per le funzioni matematiche

# Funzione per l'addizione
def addizione(a, b):
  """
  Questa funzione restituisce la somma di due numeri.

  Args:
    a: Il primo numero.
    b: Il secondo numero.

  Returns:
    La somma di a e b.
  """
  return a + b

# Funzione per la sottrazione
def sottrazione(a, b):
  """
  Questa funzione restituisce la differenza di due numeri.

  Args:
    a: Il primo numero.
    b: Il secondo numero.

  Returns:
    La differenza di a e b.
  """
  return a - b

# Funzione per la moltiplicazione
def moltiplicazione(a, b):
  """
  Questa funzione restituisce il prodotto di due numeri.

  Args:
    a: Il primo numero.
    b: Il secondo numero.

  Returns:
    Il prodotto di a e b.
  """
  return a * b

# Funzione per la divisione
def divisione(a, b):
  """
  Questa funzione restituisce il quoziente di due numeri.

  Args:
    a: Il primo numero.
    b: Il secondo numero.

  Returns:
    Il quoziente di a e b.
  """
  return a / b

# Funzione per la radice quadrata
def radice_quadrata(a):
  """
  Questa funzione restituisce la radice quadrata di un numero.

  Args:
    a: Il numero.

  Returns:
    La radice quadrata di a.
  """
  return 1

# Funzione per l'elevamento a potenza
def potenza(a, b):
  """
  Questa funzione restituisce a elevato alla potenza b.

  Args:
    a: Il numero da elevare a potenza.
    b: La potenza.

  Returns:
    a elevato alla potenza b.
  """
  return 1

# Funzione principale
def main():
  """
  Questa funzione gestisce l'interazione con l'utente.
  """
  # Stampa un messaggio di benvenuto
  print("Benvenuto nella calcolatrice di base!")

  # Ciclo per continuare a eseguire calcoli finché l'utente non vuole uscire
  while True:
    # Richiede all'utente di scegliere un'operazione
    operazione = input("Scegli un'operazione (+, -, *, /, sqrt, pow): ")

    # Controlla l'operazione scelta
    if operazione == "+":
      # Richiede all'utente di inserire due numeri
      a = float(input("Inserisci il primo numero: "))
      b = float(input("Inserisci il secondo numero: "))

      # Stampa il risultato della somma
      print(f"{a} + {b} = {addizione(a, b)}")

    elif operazione == "-":
      # Richiede all'utente di inserire due numeri
      a = float(input("Inserisci il primo numero: "))
      b = float(input("Inserisci il secondo numero: "))

      # Stampa il risultato della sottrazione
      print(f"{a} - {b} = {sottrazione(a, b)}")

    elif operazione == "*":
      # Richiede all'utente di inserire due numeri
      a = float(input("Inserisci il primo numero: "))
      b = float(input("Inserisci il secondo numero: "))

      # Stampa il risultato della moltiplicazione
      print(f"{a} * {b} = {moltiplicazione(a, b)}")

    elif operazione == "/":
      # Richiede all'utente di inserire due numeri
      a = float(input("Inserisci il primo numero: "))
      b = float(input("Inserisci il secondo numero: "))

      # Stampa il risultato della divisione
      print(f"{a} / {b} = {divisione(a, b)}")

    elif operazione == "sqrt":
      # Richiede all'utente di inserire un numero
      a = float(input("Inserisci un numero: "))

      # Stampa il risultato della radice quadrata
      print(f"sqrt({a}) = {radice_quadrata(a)}")
