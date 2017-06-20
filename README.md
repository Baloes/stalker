# stalker
O URI ONLINE JUDGE (https://www.urionlinejudge.com.br) é uma plataforma que tem como objetivo promover a prática de programação e o compartilhamento de conhecimento. Atualmente o URI ONLINE JUDGE oferece um conjunto bem limitado de estatísticas para um usuário, dados que poderiam ajudar a um competidor durante sua preparação para Maratona de Programação. Porém, através de um questionários feito por eles, pretende-se adicionar mais funcionalidas, então esta aplicação pode futuramente estar obsoleta.
<br><br>
A Universidade do Oeste do Paraná (UNIOESTE) possui um programa que prepará seus alunos do curso de Ciência da Computação, para a Maratona de programção. Apesar de possuir outras, o URI ONLINE JUDGE é a principal plataforma utilizada pelo seus alunos, pensando nisso e no tópico levantado anteriormente, está aplicação tem o objetivo de fornecer mais dados para que os alunos possam tomar melhores decisões para sua rotina de treinos.   

## O que faz
Atualmente, possui uma quantidade bem limitada de funções, em que pretende expandi-las futuramente. Atualmente, você pode comparar seu desempenho com outra pessoa através de uma pontuação e visualizar quantos problemas você fez em cada categoria durante um período de tempo. 

## Como instalar
Atualmente para usar você apenas precisa baixar os arquivos (Download -> Download zip), descompactar e usar o executar no terminal usando o "python3". 

## Como usar
Importante, a aplicação só funcionará com uma versão do python >= 3. Para usar
<br><br>
 Para comparar a pontuação de diferentes pessoas use o comando:
>pyhon3 __stalker.py__ _show-score_ *[lista com IDs das pessoas]*

Para comparar o número de problemas diferentes pessoas fizeram use o comando:
>python3 __stalker.py__ _show-problems-solved__ *[lista com IDs das pessoas]* *-[flags das categorias que serão análisadas]* 

Algumas comandos podem ser úteis durante a visualização do gráfico gerado:
<br>
* Aperte <kbd>O</kbd> e arreste o mouse criando uma área para poder dar zoom in (botão esquerdo) ou zoom out (botão direito);
* Aperte <kbd>P</kbd> e clique com o botão esquerdo para transladar o gráfico ou o botão direito para escala-lo;
* Aperte <kbd>H</kbd> para restaurar seu estado original.

## Cálculo da Pontuação


## Dependencias
Para funcionar é necessários ter instalado em sua máquina os seguintes pacotes:<br>
* BeautifulSoup4 - Usado para extrair informações do URI 
* Matplotlib - Usado para visualizar os dados extraidos
* Tkinter - Usado pelo Matplotlib como GUI

Caso não tenha algum deles instalados, use os seguintes comandos no terminal:<br>
> pip3 install beautifulsoup4<br>
> pip3 install matplotlib<br>
> sudo apt-get install python3-tk

Atualmente a aplicação só foi testado no sistema operacional Ubuntu 16.04.
