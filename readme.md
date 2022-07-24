# E-commerce 
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Igorcand/E-commerce-Flask/blob/master/LICENSE) 

# About the Project
E-commerce Flask é uma aplicação completa desenvolvida utilzando o framework Flask como back server side, ou seja, renderizando o front-end a partir de código em Flask. A ideia do projeto é um site em que possa adicionar produtos em um carrinho de compras, ver informações do produto, filtar a pesquisa por marca, categoria, e até o nome. Durante o desenvolvimento foi adicionado sempre um requerimento de login para seguir com as compras, criptografia de senha, upload de imagens, entre outras extensões do Flask. Na aplicação criada também existe uma aba de administrador para poder adicionar produtos, bem similar a página criada pelo Flask-Admin, nessa região existe rotas para ver produtos, marcas e categorias e também para adiciona-los.

## Layout 
When the code is runned, this is a home page without project on database
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/homepage.png) 

## Navbar 
Na aba de navegação temos rotas para filtar os produtos cadastrados, podendo ver a partir das marcas ou categorias, ou até pesquisar o nome. E também para fazer login e se registrar.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/navbar.png) 

### Filtring 
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/filtring.png)
### Login 
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/login_customer.png) 
### Register
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/registring.png) 

## Single Page 
Em cada produto no site existe um botão de detalhes, para poder analisar uma melhor descrição do produto, ver as cores disponiveis e para adicionar o produto no carrinho de acordo com a quantidade e cores necessárias.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/single_page.png) 

## Cart
Após adicionar todos os produtos necessários no carrinho, você poderá analisar, editar e deletar os items adicionados acessando o item "cart()" na navbar da página.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/carts.png) 

## Orders
Após verificar os produtos adicionados no carirnho, você poderá gerar a ordem para o pedido clicando no botão "order now" que está no carrinho de compras, que irá mostrar os produtos escolhidos e o valor da compra. Caso alguém deseje usar esse modelo de site para alguma aplicação real deve integrar com alguma API de pagamentos, como o Stripe, para processeguir nos proximos passos.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/orders.png) 





## Admin Login 
To register some product on database, you can login on Admin Page and acess this page clicking at the button "Admin" in navbar.
Para fazer o login você precisa necessariamente de estar registrado no banco de dados, caso não esteja você poderá clicar no botão "Register" e se cadastrar.


##Home page Admin
Essa é a página inicial de adiministração, onde você poderá ver todos os produtos cadastrados, deletar e edita-los.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/admin_homepage.png) 

##Brands Admin
Essa é a página de adiministração, onde você poderá ver todos as marcas cadastradas e fazer atualizações
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/admin_brands.png) 

##Categories Admin
Essa é a página de adiministração, onde você poderá ver todos as categorias de produtos cadastradas e fazer atualizações
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/admin_categories.png) 

## Navbar Admin  
Para adicionar algo no banco de dados, seja produto, marca ou categoria, você tem acesso na aba de navegação dentro da página de adiministrador.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/admin_navbar.png) 

### Add Produt 
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/add_prod.png) 
### Add Brand  
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/add_brand.png) 
### Add Category 
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/add_cat.png) 




# Technology used

## Front end
- HTML  
- CSS 
- Bootstrap4

## Back end
- Python
- Flask

## Data Base
- SQLite


# How run this project

```bash
# clone this repository
git clone [https://github.com/Igorcand/Form-Lexus.git](https://github.com/Igorcand/Pydaria-Flask)

# Enter the folder 
E-commerce-Flask

# Install modules
pip install -r requirements.txt

# Execute the file 
python run.py
```


# Author

Igor Cândido Rodrigues

https://www.linkedin.com/in/igorc%C3%A2ndido/
