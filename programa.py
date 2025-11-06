import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class RockMusicSimulator:
    def __init__(self):
        self.storage_limit = 5
        self.phone_storage = [None] * self.storage_limit
        self.play_count = {}
        self.download_count = 0

        self.rock_musics = [
            "Stairway to Heaven - Led Zeppelin",
            "Bohemian Rhapsody - Queen",
            "Hotel California - Eagles", 
            "Sweet Child O'Mine - Guns N'Roses",
            "Smoke on the Water - Deep Purple",
            "Back in Black - AC/DC",
            "Comfortably Numb - Pink Floyd",
            "Paint It Black - Rolling Stones",
            "Purple Haze - Jimi Hendrix",
            "Whole Lotta Love - Led Zeppelin",
            "Imagine - John Lennon",
            "Light My Fire - The Doors",
            "All Along the Watchtower - Jimi Hendrix",
            "Wish You Were Here - Pink Floyd", 
            "Brown Sugar - Rolling Stones",
            "Highway to Hell - AC/DC",
            "Layla - Eric Clapton",
            "Dream On - Aerosmith",
            "Another Brick in the Wall - Pink Floyd",
            "Sweet Home Alabama - Lynyrd Skynyrd",
            "Free Bird - Lynyrd Skynyrd", 
            "Black Dog - Led Zeppelin",
            "Roxanne - The Police",
            "Barracuda - Heart",
            "More Than a Feeling - Boston"
        ]

        for music in self.rock_musics:
            self.play_count[music] = 0

        self.setup_gui()

    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("🎸 Simulador de Rock Antigo - TOP 5")
        self.root.geometry("800x700")
        self.root.configure(bg='#2b2b2b')

        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        title_label = tk.Label(main_frame, 
                             text="🎸 SIMULADOR DE ROCK ANTIGO - TOP 5 AUTOMÁTICO",
                             font=('Arial', 16, 'bold'),
                             fg='white', bg='#2b2b2b')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        stats_frame = ttk.LabelFrame(main_frame, text="📊 Estatísticas", padding="10")
        stats_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))

        self.stats_label = tk.Label(stats_frame, 
                                  text="Celular: 0/5 | Downloads: 0",
                                  font=('Arial', 12),
                                  fg='white', bg='#2b2b2b')
        self.stats_label.pack()

        top5_frame = ttk.LabelFrame(main_frame, text="📱 TOP 5 NO CELULAR", padding="10")
        top5_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))

        self.top5_labels = []
        for i in range(5):
            label = tk.Label(top5_frame, 
                           text=f"{i+1}º → [VAGO]",
                           font=('Arial', 10),
                           fg='white', bg='#2b2b2b',
                           anchor='w')
            label.pack(fill='x')
            self.top5_labels.append(label)

        music_frame = ttk.LabelFrame(main_frame, text="💿 LISTA DE MÚSICAS (25 clássicos)", padding="10")
        music_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))

        music_container = ttk.Frame(music_frame)
        music_container.pack(fill='both', expand=True)

        scrollbar = ttk.Scrollbar(music_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.music_listbox = tk.Listbox(music_container, 
                                      yscrollcommand=scrollbar.set,
                                      font=('Arial', 10),
                                      bg='#1a1a1a', fg='white',
                                      selectbackground='#444444',
                                      height=12)
        self.music_listbox.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.config(command=self.music_listbox.yview)

        for i, music in enumerate(self.rock_musics, 1):
            self.music_listbox.insert(tk.END, f"{i:2d}. {music}")

        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=4, column=0, columnspan=2, pady=10)

        play_btn = tk.Button(action_frame, 
                           text="🎵 Tocar Música Selecionada",
                           command=self.play_selected_music,
                           font=('Arial', 12, 'bold'),
                           bg='#4CAF50', fg='white',
                           padx=20, pady=10)
        play_btn.pack(side=tk.LEFT, padx=5)

        reset_btn = tk.Button(action_frame,
                            text="🔄 Reiniciar Simulação", 
                            command=self.reset_simulation,
                            font=('Arial', 10),
                            bg='#FF9800', fg='white',
                            padx=15, pady=5)
        reset_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = tk.Button(action_frame,
                    text="🧹 Limpar TOP 5",
                    command=self.clear_top_5,
                    font=('Arial', 10),
                    bg='#607D8B', fg='white',
                    padx=15, pady=5)
        clear_btn.pack(side=tk.LEFT, padx=5)

        exit_btn = tk.Button(action_frame,
                           text="🚪 Sair",
                           command=self.root.quit,
                           font=('Arial', 10),
                           bg='#f44336', fg='white',
                           padx=15, pady=5)
        exit_btn.pack(side=tk.LEFT, padx=5)

        log_frame = ttk.LabelFrame(main_frame, text="📝 Log de Ações", padding="10")
        log_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))

        self.log_text = tk.Text(log_frame, 
                              height=4,
                              font=('Arial', 9),
                              bg='#1a1a1a', fg='white')
        self.log_text.pack(fill='both')

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)

        self.update_display()

    def remove_from_top5(self, index):
        if 0 <= index < len(self.phone_storage):
            if self.phone_storage[index] is not None:
                removed = self.phone_storage[index]
                self.phone_storage[index] = None
                self.log_action(f"❌ {removed} foi removida do TOP 5 (posição {index+1}).")
                self.update_display()
            else:
                messagebox.showinfo("Remover música", "Essa posição já está vazia.")

    def log_action(self, message):
        self.log_text.insert(tk.END, f"• {message}\n")
        self.log_text.see(tk.END)
        self.root.update()

    def clear_top_5(self):
        if all(m is None for m in self.phone_storage):
            messagebox.showinfo("Limpar TOP 5", "O TOP 5 já está vazio!")
            return
        self.phone_storage = [None] * self.storage_limit
        self.log_action("🧹 TOP 5 foi limpo manualmente.")
        self.update_display()

    def update_display(self):
        filled = sum(1 for m in self.phone_storage if m is not None)
        self.stats_label.config(text=f"Celular: {filled}/5 | Downloads: {self.download_count}")

        top5_parent = self.root.nametowidget(".!frame.!labelframe2")
        for widget in top5_parent.winfo_children():
            widget.destroy()

        self.top5_labels.clear()

        for i, music in enumerate(self.phone_storage):
            frame = tk.Frame(top5_parent, bg="#2b2b2b")
            frame.pack(fill='x', pady=2)

            if music is not None:
                label = tk.Label(frame, text=f"{i+1}º → 🎸 {music}", font=('Arial', 10), fg='white', bg='#2b2b2b', anchor='w')
                btn_remove = tk.Button(frame, text="✕", font=('Arial', 9, 'bold'), bg='#3a3a3a', fg='white',
                                       activebackground='#f44336', activeforeground='white', width=2, relief='flat',
                                       bd=0, cursor='hand2', command=lambda idx=i: self.remove_from_top5(idx))
            else:
                label = tk.Label(frame, text=f"{i+1}º → [VAGO]", font=('Arial', 10), fg='gray', bg='#2b2b2b', anchor='w')
                btn_remove = None

            label.pack(side='left', fill='x', expand=True)
            if btn_remove:
                btn_remove.pack(side='right', padx=5)
            self.top5_labels.append(frame)

        self.music_listbox.delete(0, tk.END)
        for i, music in enumerate(self.rock_musics, 1):
            marker = "📱" if music in self.phone_storage else "  "
            self.music_listbox.insert(tk.END, f"{i:2d}. {marker} {music}")

    def play_selected_music(self):
        selection = self.music_listbox.curselection()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione uma música da lista!")
            return

        index = selection[0]
        music_name = self.rock_musics[index]

        self.play_count[music_name] += 1

        if music_name in self.phone_storage:
            self.log_action(f"Tocando novamente: {music_name} (total: {self.play_count[music_name]} plays)")
        else:
            try:
                empty_index = self.phone_storage.index(None)
                self.phone_storage[empty_index] = music_name
                self.download_count += 1
                self.log_action(f"📥 {music_name} foi adicionada na posição {empty_index+1}.")
            except ValueError:
                top_names = [f"{i+1} - {m}" for i, m in enumerate(self.phone_storage) if m]
                choice = simpledialog.askinteger("Substituir música",
                    "O celular está cheio!\n\nEscolha qual posição substituir:\n" + "\n".join(top_names),
                    minvalue=1, maxvalue=len(self.phone_storage))
                if choice:
                    removed = self.phone_storage[choice-1]
                    self.phone_storage[choice-1] = music_name
                    self.log_action(f"🔄 Substituída: {removed} → {music_name}")
                    self.download_count += 1

        self.update_display()

    def reset_simulation(self):
        self.phone_storage = [None] * self.storage_limit
        self.download_count = 0
        for music in self.rock_musics:
            self.play_count[music] = 0
        self.log_action("Simulação reiniciada!")
        self.update_display()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RockMusicSimulator()
    app.run()
