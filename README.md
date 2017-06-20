# stalker
O URI ONLINE JUDGE (https://www.urionlinejudge.com.br) é uma plataforma que tem como objetivo promover a prática de programação e o compartilhamento de conhecimento. Atualmente o URI ONLINE JUDGE oferece um conjunto bem limitado de estatísticas para um usuário, dados que poderiam ajudar a um competidor durante sua preparação para Maratona de Programação. Porém, através de um questionários feito por eles, pretende-se adicionar mais funcionalidas, então esta aplicação pode futuramente estar obsoleta.
<br><br>
A Universidade do Oeste do Paraná (UNIOESTE) possui um programa que prepará seus alunos do curso de Ciência da Computação, para a Maratona de programção. Apesar de possuir outras, o URI ONLINE JUDGE é a principal plataforma utilizada pelo seus alunos, pensando nisso e no tópico levantado anteriormente, está aplicação tem o objetivo de fornecer mais dados para que os alunos possam tomar melhores decisões para sua rotina de treinos.   

## O que faz?
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

#### Flags Disponíveis
__-I__ = Inciante<br>
__-A__ = Ad-Hoc<br>
__-S__ = Strings<br>
__-E__ = Estruturas e Bibliotecas<br>
__-M__ = Matemática<br>
__-P__ = Paradigmas<br>
__-G__ = Grafos<br>
__-C__ = Geometrica Computacional<br>

As flags podem ser concatenadas em qualquer ordem para mostra mais de uma categoria. Por exemplo:
>python3 __stalker.py__ _show-problems-solved_ 1464 20268 36720 -PSG 

#### Informações Úteis
Algumas comandos podem ser úteis durante a visualização do gráfico gerado:
<br>
* Aperte <kbd>O</kbd> e arreste o mouse criando uma área para poder dar zoom in (botão esquerdo) ou zoom out (botão direito);
* Aperte <kbd>P</kbd> e clique com o botão esquerdo para transladar o gráfico ou o botão direito para escala-lo;
* Aperte <kbd>H</kbd> para restaurar seu estado original.

## Cálculo da Pontuação
O código escrito em _c_ a seguir mostra como o cálculo da pontuação é feita.

```c
double pontuacao = 0

for(int i = 0; i < N_PROBLEMAS_RESOLVIDOS; i++)
{
    pontuacao += pow(level_do_problema[i], EULER_CONSTANT); 
}
```

A tabela a seguir mostra o valor associado a um nível de algum problema. Uma interpretação que pode ser feita é que para resolver um problema nível 10 equivale a resolver 522 problemas nível 1. A intenção é que a pontuação possa estimar de uma forma heurística, a partir da sua pontuação, a dificuldade máxima de um problema que essa pessoa poderia resolver, o nível de problema que essa pessoa já se sente confortável em resolver e, principalmente, quais problemas essa pessoa deveria focar para aumentar seu desempenho da melhor da forma possível.

| Nível | Valor    |
|:-----:|:--------:|
| 1     |  1.000   |
| 2     |  6.5808  |
| 3     | 19.8129  |
| 4     | 43.3080  |
| 5     | 79.4323  |
| 6     | 130.3870 |
| 7     | 198.2506 |
| 8     | 285.0054 |
| 9     | 392.5546 |
| 10    | 522.7352 |

Um grande problema atual do cálculo da pontuação é que ele confia muito na classificação dos problemas feitos pelo URI ONLINE JUDGE, que pode estar sujeito a uma avaliação que não representa a real dificuldade do problema. Outro problema que o cáluculo não considera em sua conta que tipo de problema foi resolvido, por exemplo, caso alguém tenha apenas resolvido problemas que aborda o mesmo assunto, a pontuação resultante não pode representar muito bem seu real desempenho em uma competição. Também, resolver apenas problemas fáceis, por exemplo 1000 deles, não garante que ele será capaz de resolver um problema nível 10, este ponto está relacionado ao ponto anterior no sentido que muitos dos problemas nível um possuem uma baixa diversidade de conceitos e técnicas envolvidas, então isso deveria ser considerado de alguma forma no cálculo da pontuação. Esses tipos de informações devem ser consideradas e sua participação no cálculo da pontuação futuramente será  considerada.

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
