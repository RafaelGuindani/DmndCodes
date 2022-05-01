def say_my_name(name)
    "You are " + name.capitalize
end

def city(cidade)
    "You live in #{cidade.capitalize}"
end

def age(idade)
    "you have #{idade}".capitalize
end

"*"*10
puts say_my_name "Rafael Guindani"
puts city "curitiba"
puts age "35 Years"