class Carro:
    def calcular_custo(self, distancia):
        # Exemplo: R$ 0.50 por km
        return distancia * 0.50

class Caminhao:
    def calcular_custo(self, distancia):
        # Exemplo: R$ 0.85 por km
        return distancia * 0.85

class Moto:
    def calcular_custo(self, distancia):
        # Exemplo: R$ 0.35 por km
        return distancia * 0.35

def calcular_custo_total(veiculos, distancia=200):
    custo_total = 0.0
    for veiculo in veiculos:
        custo_total += veiculo.calcular_custo(distancia)
    return custo_total

# Exemplo de uso:
frota = [Carro(), Caminhao(), Moto()]
custo_geral = calcular_custo_total(frota, 200)
print(f"O custo total da viagem de 200 km para a frota é: R$ {custo_geral:.2f}")
