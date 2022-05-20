class Carro
  attr_accessor :marca, :modelo

  def initialize(marca, modelo)
    @marca = marca
    @modelo = modelo
  end

  def Descricao
    "\nMarca: #{marca}\nModelo: #{modelo}"
  end
end

carro = Carro.new "Tesla", "Model S"
puts carro

#*********************************

#carro = Carro.new
#carro.marca = "Ford"
#carro.modelo = "Focus"

#*********************************

puts "Marca: "+carro.marca
puts "Modelo: "+carro.modelo
puts "\nDescrição: "+carro.Descricao