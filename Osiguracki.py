import os

# Define folder path
folder_path = "C://Documents/JewishMillionaires"

# List of prominent Jewish millionaires (public figures)
millionaires = [
    "Mark Zuckerberg – Co-founder of Facebook",
    "Larry Page – Co-founder of Google",
    "Sergey Brin – Co-founder of Google",
    "Michael Bloomberg – Founder of Bloomberg L.P.",
    "Sheldon Adelson – Casino magnate and philanthropist",
    "George Soros – Investor and philanthropist",
    "Howard Schultz – Former CEO of Starbucks",
    "Ronald Lauder – Heir to Estée Lauder and philanthropist",
    "Steven Spielberg – Film director and producer",
    "Jeffrey Katzenberg – Film producer and former Disney chairman"
]

# Create folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Write the files
for i in range(1, 11):
    file_path = os.path.join(folder_path, f"example{i}.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Prominent Jewish Millionaires:\n\n")
        for name in millionaires:
            file.write(f"- {name}\n")

print(f"10 files successfully created in: {folder_path}")
