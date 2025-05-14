Manual do Usuário – Agenda Telefônica HelaTech®
Versão: 1.0
Desenvolvedor: HelaTech®
Plataforma: Windows/Linux – Requer Python 3.10+ e bibliotecas tkinter, openpyxl.

Introdução

A Agenda Telefônica HelaTech® é uma aplicação simples, leve e funcional desenvolvida em Python, destinada ao gerenciamento de contatos pessoais ou profissionais. Com uma interface amigável, permite cadastrar, editar, buscar, excluir e exportar contatos para Excel de forma intuitiva.

Interface Principal

A interface está dividida em três partes:

Barra Superior (Cabeçalho) – Nome do aplicativo e identidade visual da marca.
Formulário de Entrada – Campos para digitar informações de contato.
Tabela (Treeview) – Exibe os contatos salvos e permite selecionar, editar ou excluir registros.

Funcionalidades

</span>
<div align="center">
<img src="https://github.com/user-attachments/assets/1b6bb6e0-0688-4ade-92a0-8858d1773fcf" />
</div>

1. Adicionar Contato
Preencha os campos:

Nome (obrigatório)
Sexo (F ou M)
Telefone (obrigatório e único)
E-mail (obrigatório)

Clique em "Adicionar" para salvar o contato.

2. Procurar Contato
Digite qualquer termo (nome, telefone, e-mail) no campo de busca e clique em "Procurar". Os resultados aparecerão na tabela.

3. Visualizar Todos os Contatos
Clique em "Ver Dados" para carregar todos os contatos registrados na agenda.

4. Atualizar Contato
</span>
<div align="center">
<img src="https://github.com/user-attachments/assets/1a85efae-d21f-4e03-bcf9-fd78c8543879" />
</div>
Clique sobre um contato na tabela.
Clique em "Atualizar".
Edite os campos na janela que se abrir.
Clique em "Salvar".

6. Deletar Contato(s)
Marque as caixas de seleção ao lado dos contatos.
Clique em "Deletar".
Dica: Use os botões ✓ (selecionar todos), ✗ (desmarcar todos) ou ⥁ (inverter seleção).

7. Exportar para Excel
Selecione os contatos desejados.
Clique em "Download".
Escolha o local e o nome do arquivo .xlsx.

Atalho de Teclado
Ctrl + a (minúsculo): Seleciona todos os contatos na tabela.

Ícone e Identidade Visual
O programa exibe um ícone customizado (fone.png) e segue o tema de cores da marca HelaTech®, com uma interface moderna, leve e acolhedora.

🐰 HelaTech & Hela, a Mascote
Desenvolvido pela HelaTech®, cujo símbolo é Hela, uma coelha curiosa e inteligente que representa agilidade, organização e carinho por tecnologia simples e útil.

Requisitos
Python 3.10 ou superior

Bibliotecas:

tkinter (interface gráfica)
openpyxl (exportação para Excel)
Arquivo dados.py com funções de manipulação dos dados

Estrutura Recomendada do Projeto
/Agenda-Telefonica-HelaTech
├── main.py
├── dados.py
├── fone.png
├── contatos.csv

Possíveis Problemas
Erro	                                Solução
TclError: bitmap not defined	        Use arquivos .png ao invés de .ico no Linux/macOS
Contato não aparece após adicionar	    Verifique se todos os campos obrigatórios foram preenchidos
Dados não são atualizados               Selecione um contato e clique em Atualizar

Projeto:
Nome: Thiago Vital Barroso
Tel.: [5592994353291](https://wa.me/5592994353291)
E-mail: thiagovitalbarroso@gmail.com
