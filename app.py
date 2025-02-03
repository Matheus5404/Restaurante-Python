from modelos.restaurante import Restaurante

def main():
    # Crie uma instância de Restaurante
    restaurante = Restaurante('Praça', 'Gourmet')
    restaurante.receber_avaliacao('Gui', 10)
    restaurante.receber_avaliacao('Lais', 8)
    restaurante.receber_avaliacao('Emy', 2)
    
    # Liste os restaurantes
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()