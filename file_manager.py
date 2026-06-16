import os

try:
    folder =  input("Enter folder path: ")

    files = os.listdir(folder)

    print("\nFiles available:")

    for file in files:
        print(file)

    print("\nTask Completed Successfully")

except Exception as e:
    print("Error:", e)