import random
import string

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    print("🔐 Generador de Contraseñas")
    print("-" * 30)
    longitud = int(input("¿De cuántos caracteres quieres tu contraseña? "))
    nueva = generar_contraseña(longitud)
    print(f"\n✅ Tu contraseña es: {nueva}")
