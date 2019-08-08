#!/usr/bin python
# -*- coding: utf-8 -*- 

from tkinter import *
import sqlite3


conn = sqlite3.connect("produtos.db")
cursor = conn.cursor()

def criarTabela():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            matricula INTEGER NOT NULL PRIMARY KEY,
            nome TEXT NOT NULL,
            origem TEXT NOT NULL
        );
    """)

criarTabela()

#### Definições da Aplicação Principal ###
principal = Tk()
principal.title("Cadastro de Produtos")
principal.geometry("600x333")
principal.resizable(FALSE, FALSE)

#### Funções ###
def adicionar_produto():
    matricula = etMatricula.get()
    nome = etNome.get()
    origem = etOrigem.get()
    cursor.execute("""
        INSERT INTO produtos (matricula, nome, origem) VALUES (?, ?, ?)""", (matricula, nome, origem))
    conn.commit()
    lstProdutos.insert(END, (matricula, nome, origem))

def deletar_produto():
    matricula_produto = etMatriculaDeletar.get()
    cursor.execute(""" DELETE FROM produtos WHERE nome(?) """, (matricula))
    conn.commit()
    lstProdutos.delete(0, END)
    lista = cursor.execute("""
        SELECT * FROM produtos;
        """)
    for i in lista:
        lstProdutos.insert(END, i)

def mudar_origem():
    matricula_produto = etMatriculaMudar.get()
    nova_origem = etNovaOrigem.get()
    cursor.execute("""
        UPDATE produtos SET origem = ? WHERE matricula = ?""", (nova_origem, matricula_produto))
    conn.commit()
    lstProdutosdelete(0, END)
    lista = cursor.execute("""
        SELECT * FROM produtos;
        """)
    for i in lista:
        lstProdutos.insert(END, i)

def exportar():
    with io.open('produtos.sql', 'w') as f:
        for linha in conn.iterdump():
            f.write('%s\n' % linha)
    cursor.execute("""
        SELECT * FROM produtos;
    """)
    with io.open('produtos.txt', 'w') as f:
        for linha in cursor.fetchall():
            linha = str(linha)
            f.write('%s\n' % linha)

lblTitulo = Label(principal, text="Cadastro")
lblNomeNota = Label(principal, text="Matrícula / Nome / Origem")

### Widgets - Adicionar  ###
lblAdicionarProduto = Label(principal, text="Adicionar Produto")
lblMatricula = Label(principal, text="Matrícula: ")
lblNome = Label(principal, text="PRODUTO: ")
lblOrigem = Label(principal, text="ORIGEM: ")
etMatricula = Entry(principal)
etProduto = Entry(principal)
etNome = Entry(principal)
etOrigem = Entry(principal)
btnAdd = Button(principal, text="Adicionar", command=adicionar_produto)

### Widgets - Deletar ###
lblDeletarProduto = Label(principal, text="Deletar produto (id)")
lblMatriculaDeletar = Label(principal, text="Matrícula: ")
etMatriculaDeletar = Entry(principal, width=10)
btnDel = Button(principal, text="Deletar", command=deletar_produto)

### Widgets - Mudar origem ###
lblMudarOrigem = Label(principal, text="Mudar Origem")
lblMatriculaMudar = Label(principal, text="Origem: ")
lblNovaOrigem = Label(principal, text="Nova origem: ")
etMatriculaMudar = Entry(principal)
etNovaOrigem = Entry(principal)
btnMudarOrigem = Button(principal, text="Mudar Origem", command=mudar_origem)

### Widgets - Listar produtos ###
scrollbar = Scrollbar(principal)
lstProdutos = Listbox(principal, width=35, height=16)
lstProdutos.config(yscrollcommand=scrollbar.set)
#scrollbar.config(command=lstProdutos.yview)
lista = cursor.execute("""
    SELECT * FROM produtos;
    """)
for i in lista:
    lstProdutos.insert(END, i)

### Posicionamento de Widgets - Principal ###
lblTitulo.place(x=275)
lblNomeNota.place(x=308, y=30)

### Posicionamento de Widgets - Listar produtos ####
lstProdutos.place(x=310, y=52)
scrollbar.place()

### Posicionamento de Widgets - Adicionar produtos ###
lblAdicionarProduto.place(x=100, y=30)
lblMatricula.place(x=10, y=52)
etMatricula.place(x=115, y=50)
lblNome.place(x=10, y=82)
etNome.place(x=115, y=80)
lblOrigem.place(x=10, y=112)
etOrigem.place(x=115, y=110)
btnAdd.place(x=115, y=145)

### Posicionamento de Widgets - FUnção Deletar ###
lblDeletarProduto.place(x=100, y=175)
lblMatriculaDeletar.place(x=10, y=197)
etMatriculaDeletar.place(x=80, y=195)
btnDel.place(x=175, y=198)

### Posicionamento de Widgets - Função Mudar  ###
lblMudarOrigem.place(x=105, y=225)
lblMatriculaMudar.place(x=10, y=247)
etMatriculaMudar.place(x=115, y=245)
lblNovaOrigem.place(x=10, y=277)
etNovaOrigem.place(x=115, y=275)
btnMudarOrigem.place(x=115, y=308)

if __name__ == '__main__':

    principal.mainloop()
