
def dividir()
  print('Por gentileza, informe o primeiro valor: ')
  n1 = gets.chomp.to_i
  print('Por gentileza, informe o segundo valor: ')
  n2 = gets.chomp.to_i
  dividir = n1/n2
  printf('O resultado da divisão é %d', dividir)
end

def multiplicar()
  print('Por gentileza, informe o primeiro valor: ')
  n1 = gets.chomp.to_i
  print('Por gentileza, informe o segundo valor: ')
  n2 = gets.chomp.to_i
  multiplicar = n1*n2
  printf('O resultado da divisão é %d', multiplicar)
end

dividir

multiplicar