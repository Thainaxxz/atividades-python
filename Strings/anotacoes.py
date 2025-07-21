


#var(9): pega a letra que esta na 10º posição
#var(9:13) pega a letra que esta na 10º posição até a posição antecessora da 13º posição (9,10,11,12)(13 é removido)
#var(9:21:2) vou começar no 9 parar no 21 e o último 2 significa que ele vai pular de 2 em 2
#var(:5) quando eu nao coloco onde inicia, ele começa do caractere 0 (0,1,2,3,4)
#var(15:) ele inicia no 15 e vai até o final da string
#var(9::13) começa no 9, vai até o final, pula de 3 em 3

#len(var) conta quantas caracteres tem na string
#var.count('o') ele conta quantas vezes a letra o na string
#var.count('o',0,13) conta quantas vezes tem a letra o da posição 0 ate a 13
#var.find('deo') ele mostra onde começou (posição) o 'deo' na string
#'curso' in var : tem a palavra 'curso' na string? true or false

#var.replace('python','android'): ele procura a palavra python e substitui por android
#var.upper(): ele coloca a string em maiúscula
#var.lower(): coloca a string em minuscula




#variavel.capitalize(): Joga todos os caracteres para minúsculo e a primeira letra ele joga para maiusculo
#variavel.title(): Analiza quantas palavras tem na string e coloca em maiúsculo cada letra de cada palavra
#variavel.trip(): remove todos os espaços inuteis do inicio e do fim da string
#variavel.rstrip(): ele so remove os espaços do final
#variavel.lstrip(): ele remove apenas os espaços do inicio da string

#funcionalidades de divisão
#var.split(): ele pega onde tem espaço na string e faz uma divisão
#  "joao fez arroz" = "joao" "fez" "arroz"
#'-'.join(frase): ele junta a cadeia com o traço (ou qualquer coisa) no meio
#joao-fez-arroz