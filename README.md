# StampLib

**Motivação para o projeto**

Eu coleciono selos postais e é trabalhoso manter eles organizados em categorias no meu caderno de selos. Além disso, volta e meia eu quero lembrar alguma informação do selo, como o seu ano ou a sua história e isso envolve pesquisar na internet aquilo que eu desejo saber.

Foi com o objetivo de me ajudar a manter a minha coleção organizada que eu criei o StampLib - uma aplicação Django que me permite adicionar os selos da minha coleção, além de ter uma opção de filtros que agiliza o processo de busca de determinado selo.

O backend foi desenvolvido em Python, com o framework Django e o frontend foi desenvolvido com Jinja Templates, dentro do próprio projeto Django. Para estilização foi utilizado o Bootstrap 5.

**Telas**

Tela principal com todos os selos da coleção

![image](https://github.com/ScotuzziJr/stamplib/assets/59208275/f6abbb24-8fde-46fb-aeb1-6f7b3557a5db)

Tela individual de cada selo com sua descrição e opção de exclusão (a tela é acessada por meio do botão view presente no card de cada selo na página principal)

![image](https://github.com/ScotuzziJr/stamplib/assets/59208275/661641a0-ac69-4f0a-9635-e1fc1bf98574)

Após excluir um selo a aplicação volta para a tela inicial e, no caso do selo excluído ser o único de sua categoria, a categoria também é excluída

![image](https://github.com/ScotuzziJr/stamplib/assets/59208275/d9065a84-7054-4bd3-9c7d-e82097883f0d)

Tela para adicionar um novo selo à coleção

![image](https://github.com/ScotuzziJr/stamplib/assets/59208275/82b9bea4-595f-4c13-989b-ff5a7c7c72fc)

Filtrando os selos pela categoria (nesse caso, Brazil)

![image](https://github.com/ScotuzziJr/stamplib/assets/59208275/68be2cdc-c489-4029-8a85-02d4b9ac40f9)
