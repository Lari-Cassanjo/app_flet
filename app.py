import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = 'sqlite:///projeto2.db'

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()

def main(page: ft.Page): # Atribui uma página em branco do flet a uma função
    
    page.title = 'Cadastro App'
    
    lista_produtos = ft.ListView()
    
    def cadastrar(e):
        novo_produto = Produto(titulo=produto.value, preco=preco.value)
        session.add(novo_produto)
        session.commit()
        lista_produtos.controls.append(ft.Text(produto.value))
        page.update()
        print('Produto salvo com sucesso!')
    
    txt_titulo = ft.Text('Título do produto: ')
    produto = ft.TextField(label='Digite o título do produto',text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do produto')
    preco = ft.TextField(value=0,label='Digite o preço do produto',text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)
    
    page.add(
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto
    )
    
    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(p.titulo)
            )
        )
        
    page.add(lista_produtos)

ft.app(target=main) # Cria o app e define a página que vai ser aberta (chamando a função)