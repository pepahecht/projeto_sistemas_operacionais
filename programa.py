import tkinter as tk
from tkinter import ttk, messagebox

class RockMusicSimulator:
    def __init__(self):
        self.storage_limit = 5
        self.phone_storage = []
        self.play_count = {}
        self.download_count = 0
        
        # Lista de 25 músicas de rock antigo
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
        
        # Inicializa contadores
        for music in self.rock_musics:
            self.play_count[music] = 0
            
        self.setup_gui()
    
    def setup_gui(self):
        # Janela principal
        self.root = tk.Tk()
        self.root.title("🎸 Simulador de Rock Antigo - TOP 5")
        self.root.geometry("800x700")
        self.root.configure(bg='#2b2b2b')
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = tk.Label(main_frame, 
                             text="🎸 SIMULADOR DE ROCK ANTIGO - TOP 5 AUTOMÁTICO",
                             font=('Arial', 16, 'bold'),
                             fg='white', bg='#2b2b2b')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Frame de estatísticas
        stats_frame = ttk.LabelFrame(main_frame, text="📊 Estatísticas", padding="10")
        stats_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.stats_label = tk.Label(stats_frame, 
                                  text="Celular: 0/5 | Downloads: 0",
                                  font=('Arial', 12),
                                  fg='white', bg='#2b2b2b')
        self.stats_label.pack()
        
        # Frame do TOP 5
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
        
        # Frame da lista de músicas
        music_frame = ttk.LabelFrame(main_frame, text="💿 LISTA DE MÚSICAS (25 clássicos)", padding="10")
        music_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Scrollbar para a lista de músicas
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
        
        # Preenche a lista de músicas
        for i, music in enumerate(self.rock_musics, 1):
            self.music_listbox.insert(tk.END, f"{i:2d}. {music}")
        
        # Frame de ações
        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Botão para tocar música
        play_btn = tk.Button(action_frame, 
                           text="🎵 Tocar Música Selecionada",
                           command=self.play_selected_music,
                           font=('Arial', 12, 'bold'),
                           bg='#4CAF50', fg='white',
                           padx=20, pady=10)
        play_btn.pack(side=tk.LEFT, padx=5)
        
        # Botão de reset
        reset_btn = tk.Button(action_frame,
                            text="🔄 Reiniciar Simulação", 
                            command=self.reset_simulation,
                            font=('Arial', 10),
                            bg='#FF9800', fg='white',
                            padx=15, pady=5)
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        # Botão de sair
        exit_btn = tk.Button(action_frame,
                           text="🚪 Sair",
                           command=self.root.quit,
                           font=('Arial', 10),
                           bg='#f44336', fg='white',
                           padx=15, pady=5)
        exit_btn.pack(side=tk.LEFT, padx=5)
        
        # Frame de log
        log_frame = ttk.LabelFrame(main_frame, text="📝 Log de Ações", padding="10")
        log_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        self.log_text = tk.Text(log_frame, 
                              height=4,
                              font=('Arial', 9),
                              bg='#1a1a1a', fg='white')
        self.log_text.pack(fill='both')
        
        # Configurar weights para responsividade
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        self.update_display()
    
    def log_action(self, message):
        """Adiciona mensagem ao log"""
        self.log_text.insert(tk.END, f"• {message}\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def update_top_5(self):
        """Atualiza o TOP 5 baseado no número de plays"""
        # Ordena por plays (decrescente)
        sorted_musics = sorted(self.rock_musics, key=lambda x: self.play_count[x], reverse=True)
        
        # Pega as top 5 músicas (com pelo menos 1 play)
        new_top_5 = [song for song in sorted_musics if self.play_count[song] > 0][:self.storage_limit]
        
        # Conta novos downloads
        old_phone_set = set(self.phone_storage)
        new_phone_set = set(new_top_5)
        new_downloads = new_phone_set - old_phone_set
        self.download_count += len(new_downloads)
        
        # Atualiza celular
        self.phone_storage = new_top_5
        
        return new_downloads
    
    def update_display(self):
        """Atualiza toda a interface"""
        # Atualiza estatísticas
        self.stats_label.config(text=f"Celular: {len(self.phone_storage)}/5 | Downloads: {self.download_count}")
        
        # Atualiza TOP 5
        for i in range(5):
            if i < len(self.phone_storage):
                music = self.phone_storage[i]
                count = self.play_count[music]
                self.top5_labels[i].config(text=f"{i+1}º → 🎸 {music} 🔊 {count} plays")
            else:
                self.top5_labels[i].config(text=f"{i+1}º → [VAGO]")
        
        # Atualiza lista de músicas
        self.music_listbox.delete(0, tk.END)
        for i, music in enumerate(self.rock_musics, 1):
            count = self.play_count[music]
            marker = "📱" if music in self.phone_storage else "  "
            self.music_listbox.insert(tk.END, f"{i:2d}. {marker} {music} 🔊 {count}")
    
    def play_selected_music(self):
        """Toca a música selecionada na lista"""
        selection = self.music_listbox.curselection()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione uma música da lista!")
            return
        
        index = selection[0]
        music_name = self.rock_musics[index]
        
        # Salva estado anterior
        was_in_phone = music_name in self.phone_storage
        old_count = self.play_count[music_name]
        
        # Incrementa plays
        self.play_count[music_name] += 1
        
        # Atualiza TOP 5
        new_downloads = self.update_top_5()
        
        # Log da ação
        action_msg = f"Tocando: {music_name} (plays: {old_count} → {self.play_count[music_name]})"
        
        if music_name in self.phone_storage and not was_in_phone:
            action_msg += " - 📥 ENTROU NO TOP 5!"
        elif not music_name in self.phone_storage and was_in_phone:
            action_msg += " - 🗑️ SAIU DO TOP 5"
        
        if new_downloads:
            action_msg += f" - 🔄 TOP 5 atualizado!"
        
        self.log_action(action_msg)
        self.update_display()
    
    def reset_simulation(self):
        """Reinicia toda a simulação"""
        self.phone_storage = []
        self.download_count = 0
        for music in self.rock_musics:
            self.play_count[music] = 0
        
        self.log_action("Simulação reiniciada!")
        self.update_display()
    
    def run(self):
        """Inicia a aplicação"""
        self.root.mainloop()

# Versão alternativa mais simples (caso queira testar rapidamente)
class SimpleRockSimulator:
    def __init__(self):
        self.storage_limit = 5
        self.phone_storage = []
        self.play_count = {}
        self.download_count = 0
        
        self.rock_musics = [
            "Stairway to Heaven - Led Zeppelin", "Bohemian Rhapsody - Queen",
            "Hotel California - Eagles", "Sweet Child O'Mine - Guns N'Roses", 
            "Smoke on the Water - Deep Purple", "Back in Black - AC/DC",
            "Comfortably Numb - Pink Floyd", "Paint It Black - Rolling Stones",
            "Purple Haze - Jimi Hendrix", "Whole Lotta Love - Led Zeppelin",
            "Imagine - John Lennon", "Light My Fire - The Doors", 
            "All Along the Watchtower - Jimi Hendrix", "Wish You Were Here - Pink Floyd",
            "Brown Sugar - Rolling Stones", "Highway to Hell - AC/DC",
            "Layla - Eric Clapton", "Dream On - Aerosmith",
            "Another Brick in the Wall - Pink Floyd", "Sweet Home Alabama - Lynyrd Skynyrd",
            "Free Bird - Lynyrd Skynyrd", "Black Dog - Led Zeppelin",
            "Roxanne - The Police", "Barracuda - Heart", "More Than a Feeling - Boston"
        ]
        
        for music in self.rock_musics:
            self.play_count[music] = 0
            
        self.setup_simple_gui()
    
    def setup_simple_gui(self):
        self.root = tk.Tk()
        self.root.title("Simulador Rock - TOP 5")
        self.root.geometry("700x600")
        
        # Título
        tk.Label(self.root, text="🎸 SIMULADOR ROCK ANTIGO", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Estatísticas
        self.stats_var = tk.StringVar(value="Celular: 0/5 | Downloads: 0")
        tk.Label(self.root, textvariable=self.stats_var, font=('Arial', 12)).pack()
        
        # TOP 5
        tk.Label(self.root, text="TOP 5 NO CELULAR:", font=('Arial', 11, 'bold')).pack(pady=5)
        self.top5_frame = tk.Frame(self.root)
        self.top5_frame.pack(pady=5)
        
        # Lista de músicas
        tk.Label(self.root, text="CLIQUE PARA TOCAR:", font=('Arial', 11, 'bold')).pack(pady=5)
        
        music_frame = tk.Frame(self.root)
        music_frame.pack(fill='both', expand=True, padx=10)
        
        # Criar botões para cada música
        self.music_buttons = []
        for i, music in enumerate(self.rock_musics):
            btn = tk.Button(music_frame, 
                          text=music,
                          command=lambda m=music: self.play_music(m),
                          font=('Arial', 9),
                          anchor='w',
                          relief='flat',
                          bg='#e0e0e0')
            btn.pack(fill='x', pady=1)
            self.music_buttons.append(btn)
        
        self.update_simple_display()
    
    def play_music(self, music_name):
        self.play_count[music_name] += 1
        self.update_top_5()
        self.update_simple_display()
    
    def update_top_5(self):
        sorted_musics = sorted(self.rock_musics, key=lambda x: self.play_count[x], reverse=True)
        new_top_5 = [song for song in sorted_musics if self.play_count[song] > 0][:self.storage_limit]
        
        old_set = set(self.phone_storage)
        new_set = set(new_top_5)
        self.download_count += len(new_set - old_set)
        
        self.phone_storage = new_top_5
    
    def update_simple_display(self):
        self.stats_var.set(f"Celular: {len(self.phone_storage)}/5 | Downloads: {self.download_count}")
        
        # Limpa TOP 5
        for widget in self.top5_frame.winfo_children():
            widget.destroy()
        
        # Atualiza TOP 5
        for i, music in enumerate(self.phone_storage):
            count = self.play_count[music]
            label = tk.Label(self.top5_frame, 
                           text=f"{i+1}º {music} 🔊 {count}",
                           font=('Arial', 9),
                           anchor='w')
            label.pack(fill='x')
        
        # Atualiza botões
        for i, (music, btn) in enumerate(zip(self.rock_musics, self.music_buttons)):
            count = self.play_count[music]
            in_phone = "📱" if music in self.phone_storage else ""
            btn.config(text=f"{in_phone} {music} 🔊 {count}")
    
    def run(self):
        self.root.mainloop()

# Executar a versão completa
if __name__ == "__main__":
    app = RockMusicSimulator()
    app.run()
    
    # Para testar a versão simples, descomente:
    # app_simple = SimpleRockSimulator()
    # app_simple.run()