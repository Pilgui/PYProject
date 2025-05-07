import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def demo_widgets():
    # Główne okno
    root = tk.Tk()
    root.title("Demonstracja widżetów Tkinter")
    root.geometry("600x800")

    # Konfiguracja siatki. Określamy relatywne wagi (szerokości) kolumn
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # 1. Etykiety (Label)
    label = ttk.Label(root, text="Witaj w świecie Tkinter!", font=("Arial", 16))
    label.grid(row=0, column=0, columnspan=2,
               pady=10)  # Użycie columnspan do rozciągnięcia etykiety na dwie kolumny. Jest też rowspan

    # 2. Przyciski (Button)
    def button_click():
        messagebox.showinfo("Informacja", "Przycisk został kliknięty!")

    # command to funkcja, która zostanie wywołana po kliknięciu przycisku. Jeżeli chcemy przekazać argumenty do funkcji, to musimy użyć lambda
    # button = ttk.Button(root, text="Kliknij mnie", command=lambda: button_click("argument"))
    button = ttk.Button(root, text="Kliknij mnie", command=button_click)
    button.grid(row=1, column=0, columnspan=2, pady=10)  # pady dodaje odstęp w pionie

    # 3. Pole tekstowe (Entry)
    entry_label = ttk.Label(root, text="Wprowadź tekst:")
    entry_label.grid(row=2, column=0, sticky='e', padx=5)  # padx dodaje odstęp w poziomie
    entry = ttk.Entry(root, width=30)
    # sticky 'e' (east) oznacza, że etykieta będzie wyrównana do prawej, a 'w' (west) do lewej
    # sticky 'n' (north) oznacza, że etykieta będzie wyrównana do góry, a 's' (south) do dołu
    # Dozwolone są też kombinacje, np. 'nsew' czy 'ew'
    # sticky 'nsew' oznacza, że etykieta będzie rozciągnięta w czterech kierunkach
    entry.grid(row=2, column=1, sticky='w', padx=5)

    # 4. Pole wieloliniowe (Text)
    text_label = ttk.Label(root, text="Pole wieloliniowe:")
    text_label.grid(row=3, column=0, columnspan=2, pady=5)
    text_area = tk.Text(root, height=5, width=40)
    text_area.grid(row=4, column=0, columnspan=2, padx=10)

    # 5. Checkboxy
    def checkbox_changed():
        print(f"Checkbox 1: {checkbox1_var.get()}")
        print(f"Checkbox 2: {checkbox2_var.get()}")

    # Zamiast BooleanVar można użyć IntVar lub StringVar, ale wtedy musimy sami konwertować wartości
    checkbox1_var = tk.BooleanVar()
    checkbox2_var = tk.BooleanVar()

    checkbox1 = ttk.Checkbutton(
        root, text="Opcja 1", variable=checkbox1_var, command=checkbox_changed
    )
    checkbox2 = ttk.Checkbutton(
        root, text="Opcja 2", variable=checkbox2_var, command=checkbox_changed
    )

    checkbox1.grid(row=5, column=0, sticky='w', padx=10)
    checkbox2.grid(row=5, column=1, sticky='w')

    # 6. Radio buttons
    radio_label = ttk.Label(root, text="Wybierz opcję:")
    radio_label.grid(row=6, column=0, columnspan=2, pady=5)

    radio_var = tk.StringVar()
    radio_options = [("Opcja A", "A"), ("Opcja B", "B"), ("Opcja C", "C")]

    for idx, (text, value) in enumerate(radio_options, start=7):
        radio = ttk.Radiobutton(root, text=text, variable=radio_var, value=value)
        radio.grid(row=idx, column=0, columnspan=2, sticky='w', padx=10)

    # 7. Combobox
    combo_label = ttk.Label(root, text="Wybierz z listy:")
    combo_label.grid(row=10, column=0, sticky='e', padx=5)

    combo = ttk.Combobox(root, values=["Python", "Java", "C++", "Kotlin"])
    combo.grid(row=10, column=1, sticky='w', padx=5)

    # 8. Progressbar
    progress_label = ttk.Label(root, text="Pasek postępu:")
    progress_label.grid(row=11, column=0, columnspan=2, pady=5)

    progress = ttk.Progressbar(root, length=200, mode='determinate')
    progress.grid(row=12, column=0, columnspan=2)
    progress['value'] = 70  # Ustawienie wartości

    # 9. Slider (Scale)
    slider_label = ttk.Label(root, text="Suwak:")
    slider_label.grid(row=13, column=0, columnspan=2, pady=5)

    slider = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=200)
    slider.grid(row=14, column=0, columnspan=2)

    # 10. Dialogi
    def open_file():
        filename = filedialog.askopenfilename()
        print(f"Wybrano plik: {filename}")

    file_button = ttk.Button(root, text="Otwórz plik", command=open_file)
    file_button.grid(row=15, column=0, columnspan=2, pady=10)

    # Uruchomienie głównej pętli
    root.mainloop()


demo_widgets()