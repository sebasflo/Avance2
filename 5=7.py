
print("Menú de opciones:")
print("1. Saludar")
print("2. Despedirse")
print("3. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-3): ")

if opcion == "1":
    print("Hola, ¿cómo estás?")
elif opcion == "2":
    print("Adiós, hasta la próxima.")
elif opcion == "3":
    print("Cerrando el programa...")
    break
else:
     print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()