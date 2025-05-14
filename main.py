import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from openpyxl import Workbook
from dados import ver_dados_com_indices, adicionar_dados, remover_dados, atualizar_dados, pesquisar_dados

# Cores
CORES = {
    "fundo": "#f0f3f5",
    "black": "#000000",
    "branco": "#feffff",
    "azul": "#0000ff",
    "cinza_escuro": "#403d3d",
    "azul_claro": "#6f9fbd",
    "vermelho": "#ef5350",
    "verde": "#93cd95",
    "LightGray": "#D3D3D3",
    "Cyan": "#00FFFF",
    "LightCyan": "#E0FFFF",
    "Chartreuse": "#7FFF00",
    "Khaki": "#F0E68C",
}

# Variável global para armazenar o estado dos checkboxes
checkbox_state = {}

# Janela principal
janela = tk.Tk()
janela.title("HelaTech®")
janela.geometry('500x450')
janela.configure(background=CORES["fundo"])
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")


import os
from tkinter import PhotoImage

def inserir_icone_janela(janela, caminho_icone):
    """
    Define o ícone da janela principal.
    Suporta arquivos .ico (Windows) ou .png/.gif (usando PhotoImage).
    
    :param janela: instância da janela principal
    :param caminho_icone: caminho absoluto ou relativo para o ícone
    """
    if caminho_icone.endswith(".ico"):
        try:
            janela.iconbitmap(caminho_icone)
        except Exception as e:
            print(f"Erro ao definir ícone .ico: {e}")
    else:
        try:
            img = PhotoImage(file=caminho_icone)
            janela.iconphoto(False, img)
        except Exception as e:
            print(f"Erro ao definir ícone de imagem: {e}")


inserir_icone_janela(janela, "hela.png")

# Frames
frame_topo = tk.Frame(janela, width=500, height=50, bg=CORES["verde"], relief="flat")
frame_topo.grid(row=0, column=0, pady=1, sticky="nsew")

frame_formulario = tk.Frame(janela, width=500, height=150, bg=CORES["fundo"], relief="flat")
frame_formulario.grid(row=1, column=0, pady=1, sticky="nsew")

frame_tabela = tk.Frame(janela, width=500, height=248, bg=CORES["branco"], relief="flat")
frame_tabela.grid(row=2, column=0, padx=10, pady=1, sticky="nsew")

# Label topo
tk.Label(frame_topo, text='Agenda Telefônica', anchor="ne",
         font=('Tahoma', 20, 'bold'), bg=CORES["verde"], fg=CORES["black"]).place(x=5, y=5)
tk.Label(frame_topo, text=" ", width=500, anchor="nw", font=('Tahoma', 1),
         bg=CORES["black"]).place(x=0, y=46)

# Entradas
tk.Label(frame_formulario, text="Nome*", font=('Tahoma', 10, 'bold'),
         bg=CORES["fundo"], fg=CORES["cinza_escuro"]).place(x=10, y=20)
entry_nome = tk.Entry(frame_formulario, width=25)
entry_nome.place(x=80, y=20)

tk.Label(frame_formulario, text="Sexo*", font=('Tahoma', 10, 'bold'),
         bg=CORES["fundo"], fg=CORES["cinza_escuro"]).place(x=10, y=50)
combo_sexo = ttk.Combobox(frame_formulario, width=4, values=['', 'F', 'M'])
combo_sexo.place(x=80, y=50)

tk.Label(frame_formulario, text="Telefone*", font=('Tahoma', 10, 'bold'),
         bg=CORES["fundo"], fg=CORES["cinza_escuro"]).place(x=10, y=80)
entry_telefone = tk.Entry(frame_formulario, width=25)
entry_telefone.place(x=80, y=80)

tk.Label(frame_formulario, text="E-mail*", font=('Tahoma', 10, 'bold'),
         bg=CORES["fundo"], fg=CORES["cinza_escuro"]).place(x=10, y=110)
entry_email = tk.Entry(frame_formulario, width=25)
entry_email.place(x=80, y=110)

# Procurar
entry_procurar = tk.Entry(frame_formulario, width=16)
entry_procurar.place(x=347, y=21)

def procurar():
    termo = entry_procurar.get().strip()
    if not termo:
        messagebox.showwarning("Aviso", "Por favor, insira um termo de busca.")
        return

    resultados = pesquisar_dados(termo)
    for i in tree.get_children():
        tree.delete(i)  # Limpar a tabela

    if not resultados:
        messagebox.showinfo("Nenhum Resultado", "Nenhum dado encontrado.")
        return

    for item in resultados:
        iid = tree.insert('', 'end', values=('[ ]', *item))
        checkbox_state[iid] = False

btn_procurar = tk.Button(frame_formulario, text="Procurar", command=procurar,
                         bg=CORES["Khaki"], fg=CORES["cinza_escuro"], font=('Consolas', 8, 'bold'))
btn_procurar.place(x=280, y=20)

# Treeview
colunas = ['Selecionar', 'Nome', 'Sexo', 'Telefone', 'E-mail']
tree = ttk.Treeview(frame_tabela, columns=colunas, show='headings')

tree.heading('Selecionar', text='✓', anchor='center')
tree.column('Selecionar', width=30, anchor='center')

for col in colunas[1:]:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=145 if col == 'Nome' else 100)

tree.grid(row=0, column=0, sticky='nsew')

def toggle_checkbox(event):
    col = tree.identify_column(event.x)
    if col != '#1':  # Só alterna se clicar na primeira coluna
        return

    row_id = tree.identify_row(event.y)
    if not row_id:
        return

    current = checkbox_state.get(row_id, False)
    checkbox_state[row_id] = not current
    tree.set(row_id, 'Selecionar', '[X]' if not current else '[ ]')

tree.bind("<Button-1>", toggle_checkbox)

# Mostrar dados
def mostrar_dados():
    for i in tree.get_children():
        tree.delete(i)
    checkbox_state.clear()

    dados = ver_dados_com_indices()
    if not dados:
        messagebox.showinfo("Informação", "Nenhum dado encontrado.")
        return

    for indice, item in dados:
        iid = str(indice)  # identificador único baseado na posição no CSV
        tree.insert('', 'end', iid=iid, values=('[ ]', *item))
        checkbox_state[iid] = False



# Adicionar
def inserir():
    nome = entry_nome.get()
    sexo = combo_sexo.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    if not all([nome, sexo, telefone, email]):
        messagebox.showwarning('Aviso', 'Por favor, preencha todos os campos.')
        return
    
    try:
        adicionar_dados([nome, sexo, telefone, email])
        messagebox.showinfo('Sucesso', 'Dados adicionados com sucesso.')
        limpar_campos()
        mostrar_dados()
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao adicionar os dados:\n{e}')

def limpar_campos():
    entry_nome.delete(0, 'end')
    combo_sexo.set('')
    entry_telefone.delete(0, 'end')
    entry_email.delete(0, 'end')

# Atualizar
def atualizar():
    try:
        item = tree.item(tree.focus())['values']
        if not item:
            raise ValueError("Nenhum item selecionado")

        nome, sexo, telefone_antigo, email = item[1:]

        # Função para salvar as edições
        def salvar_edicao():
            novo_nome = entry_nome_popup.get().strip()
            novo_sexo = combo_sexo_popup.get().strip()
            novo_telefone = entry_telefone_popup.get().strip()
            novo_email = entry_email_popup.get().strip()

            if not all([novo_nome, novo_sexo, novo_telefone, novo_email]):
                messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos.")
                return

            sucesso = atualizar_dados([telefone_antigo, novo_nome, novo_sexo, novo_telefone, novo_email])

            if sucesso:
                messagebox.showinfo("Sucesso", "Contato atualizado com sucesso.")
                popup.destroy()  # Fecha a janela pop-up
                mostrar_dados()  # Recarrega os dados na tabela
            else:
                messagebox.showerror("Erro", "Não foi possível atualizar o contato.\nVerifique se o telefone original existe.")

        # Função de cancelar
        def cancelar():
            popup.destroy()

        # Criar janela popup
        popup = tk.Toplevel(janela)
        popup.title("Atualizar Contato")
        popup.geometry("300x200")
        popup.resizable(False, False)
        popup.configure(bg=CORES["fundo"])

        # Definir o ícone da popup
        inserir_icone_janela(popup, "hela.png")

        # Campos na popup
        tk.Label(popup, text="Nome:", bg=CORES["fundo"]).place(x=10, y=10)
        entry_nome_popup = tk.Entry(popup, width=30)
        entry_nome_popup.insert(0, nome)
        entry_nome_popup.place(x=80, y=10)

        tk.Label(popup, text="Sexo:", bg=CORES["fundo"]).place(x=10, y=40)
        combo_sexo_popup = ttk.Combobox(popup, width=3, values=["", "F", "M"])
        combo_sexo_popup.set(sexo)
        combo_sexo_popup.place(x=80, y=40)

        tk.Label(popup, text="Telefone:", bg=CORES["fundo"]).place(x=10, y=70)
        entry_telefone_popup = tk.Entry(popup, width=30)
        entry_telefone_popup.insert(0, telefone_antigo)
        entry_telefone_popup.place(x=80, y=70)

        tk.Label(popup, text="E-mail:", bg=CORES["fundo"]).place(x=10, y=100)
        entry_email_popup = tk.Entry(popup, width=30)
        entry_email_popup.insert(0, email)
        entry_email_popup.place(x=80, y=100)

        # Botões da popup
        tk.Button(popup, text="Salvar", command=salvar_edicao,
                  bg=CORES["verde"], fg=CORES["black"]).place(x=160, y=140)

        tk.Button(popup, text="Cancelar", command=cancelar,
                  bg=CORES["vermelho"], fg=CORES["black"]).place(x=206, y=140)

    except Exception as e:
        messagebox.showwarning('Erro', f'Ocorreu um erro: {str(e)}')

# Função para selecionar todos com Ctrl + A
def selecionar_com_ctrl_a(event):
    # Verificar se o evento é Ctrl + A
    if event.state == 12 and event.keysym == 'a':  # 12 == Ctrl
        # Verificar se todos os itens estão selecionados
        todos_selecionados = all(checkbox_state.get(iid, False) for iid in tree.get_children())

        # Se todos estão selecionados, desmarcar todos
        if todos_selecionados:
            desmarcar_todos()
        else:
            selecionar_todos()


# Deletar
def deletar():
    selecionados = [iid for iid, marcado in checkbox_state.items() if marcado]

    if not selecionados:
        messagebox.showwarning('Erro', 'Selecione um ou mais itens para deletar marcando as caixas.')
        return

    indices_para_deletar = [int(iid) for iid in selecionados]

    remover_dados(indices_para_deletar)  # agora passa os índices

    for iid in selecionados:
        tree.delete(iid)
        checkbox_state.pop(iid, None)

    messagebox.showinfo('Sucesso', 'Contato(s) deletado(s) com sucesso.')
    mostrar_dados()




# Associa a função de selecionar todos com Ctrl + A
janela.bind('<Control-a>', selecionar_com_ctrl_a)

# Exportar
def exportar_excel():
    selecionados = [iid for iid, marcado in checkbox_state.items() if marcado]
    if not selecionados:
        messagebox.showwarning("Atenção", "Selecione pelo menos um item com a caixa de seleção.")
        return

    wb = Workbook()
    ws = wb.active
    ws.append(['Nome', 'Sexo', 'Telefone', 'E-mail'])

    for iid in selecionados:
        valores = tree.item(iid)['values'][1:]  # Ignora o campo "Selecionar"
        ws.append(valores)

    path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")])
    if path:
        wb.save(path)
        messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso.")

def selecionar_todos():
    for iid in tree.get_children():
        checkbox_state[iid] = True
        tree.set(iid, 'Selecionar', '[X]')

def desmarcar_todos():
    for iid in tree.get_children():
        checkbox_state[iid] = False
        tree.set(iid, 'Selecionar', '[ ]')

def inverter_selecao():
    selecionados = tree.selection()
    if not selecionados:
        messagebox.showinfo("Informação", "Nenhum item selecionado na tabela.")
        return

    for iid in selecionados:
        atual = checkbox_state.get(iid, False)
        checkbox_state[iid] = not atual
        tree.set(iid, 'Selecionar', '[X]' if not atual else '[ ]')

def selecionar_com_ctrl_a(event):
    if event.keysym == 'a' and event.state & 0x0004:  # Verifica Ctrl pressionado
        selecionar_todos()

# Botões
tk.Button(frame_formulario, text="Ver Dados", command=mostrar_dados, width=10,
          bg=CORES["Cyan"], fg=CORES["black"]).place(x=280, y=50)
tk.Button(frame_formulario, text="Adicionar", command=inserir, width=10,
          bg=CORES["verde"], fg=CORES["black"]).place(x=400, y=50)
tk.Button(frame_formulario, text="Atualizar", command=atualizar, width=10,
          bg=CORES["verde"], fg=CORES["black"]).place(x=400, y=80)
tk.Button(frame_formulario, text="Deletar", command=deletar, width=10,
          bg=CORES["vermelho"], fg=CORES["black"]).place(x=400, y=110)
tk.Button(frame_formulario, text="Download", command=exportar_excel, width=10,
          bg=CORES["Cyan"], fg=CORES["black"]).place(x=280, y=80)

tk.Button(frame_formulario, text="✓", command=selecionar_todos, width=2,
          bg=CORES["Cyan"], fg=CORES["black"]).place(x=280, y=110)
tk.Button(frame_formulario, text="✗", command=desmarcar_todos,
          width=2, bg=CORES["Cyan"], fg=CORES["black"]).place(x=310, y=110)
tk.Button(frame_formulario, text="⥁", command=inverter_selecao,
          width=2, bg=CORES["Cyan"], fg=CORES["black"]).place(x=340, y=110)

# Inicializar tabela
mostrar_dados()

janela.mainloop()