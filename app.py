import flet as ft

def main(page: ft.Page): # Atribui uma página em branco do flet a uma função
    
    page.title = 'Cadastro App'
    
    txt_titulo = ft.Text('Título do produto: ')
    produto = ft.TextField(label='Digite o título do produto',text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do produto')
    preco = ft.TextField(value=0,label='Digite o preço do produto',text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Cadastrar')
    
    page.add(
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto
    )

ft.app(target=main) # Cria o app e define a página que vai ser aberta (chamando a função)