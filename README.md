# crawlerkonsi

# Desafio Software Engineer - Backend 

Olá! Esse desafio técnico tem como propósito medir suas habilidades, ver como estuda, pensa e se organiza na prática. A stack tecnológica utilizada é de sua escolha.

Após finalizar o desafio, nos envie um link para repositório do projeto ou um zip com o código.

Existem diversas maneiras e profundidades de solucionar o problema que estamos propondo. Vamos listar algumas sub-tasks que podem guiá-lo(a) em relação a essas possibilidades.

## O desafio

A Konsi coleta uma variedade de dados que não são facilmente acessíveis, para propor melhores opções de créditos para seus clientes. Um dos tipos de dados coletados é o número da matrícula do aposentado ou pensionista.

O desafio é fazer uma API que busque e retorne a matrícula do servidor em um determinado portal.

Será necessário desenvolver um `crawler` para coletar esse dado no portal e uma API para fazer input e buscar o resultado depois.

## Input

Você deve criar uma api para receber um json contendo o numero do CPF do cliente e credenciais de login do portal. 

## Output

O cliente tem que ser capaz de pegar o dado quando o processamento termina, então você deve criar um mecanismo que permita isso, retornando sempre um JSON.

## Crawler

É necessário realizar o login no portal do extratoclube com as credenciais que vamos fornecer, navegar no "MENU DE OPÇÕES", clicar em "BENEFÍCIOS DE UM CPF", consultar o CPF do cliente e retornar os números de benefícios encontrados.

- [Portal extratoclube](http://extratoclube.com.br/)


### Dado a ser coletado:

* Número da matrícula (número do benefício)


## Alguns pontos que serão analisados:

* Organização do código 
* Testes
* Facilidade ao rodar o projeto
* Escalabilidade: o quao facil é escalar os crawlers.
* Performance: aqui avaliaremos o tempo para crawlear o dado.


*Happy coding! :-)*
