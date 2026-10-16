import json

# Lista de ofertas da Shopee (exemplo)
ofertas = [
    {
        "id": 1,
        "titulo": "Fone de Ouvido Bluetooth Sem Fio TWS AirDots",
        "preco_antigo": "R$ 89,90",
        "preco_promocional": "R$ 29,90",
        "desconto": "-66%",
        "imagem": "https://via.placeholder.com/300x300?text=Fone+Bluetooth",
        "link_afiliado": "https://shopee.com.br"
    },
    {
        "id": 2,
        "titulo": "Relógio Smartwatch Digital Esportivo Waterproof",
        "preco_antigo": "R$ 120,00",
        "preco_promocional": "R$ 45,00",
        "desconto": "-62%",
        "imagem": "https://via.placeholder.com/300x300?text=Smartwatch",
        "link_afiliado": "https://shopee.com.br"
    },
    {
        "id": 3,
        "titulo": "Carregador Rápido Tipo C para Celular 20W",
        "preco_antigo": "R$ 50,00",
        "preco_promocional": "R$ 19,99",
        "desconto": "-60%",
        "imagem": "https://via.placeholder.com/300x300?text=Carregador+Tipo+C",
        "link_afiliado": "https://shopee.com.br"
    },
    {
        "id": 4,
        "titulo": "Mini Umidificador de Ar Aromatizador LED",
        "preco_antigo": "R$ 65,00",
        "preco_promocional": "R$ 24,90",
        "desconto": "-61%",
        "imagem": "https://via.placeholder.com/300x300?text=Umidificador+LED",
        "link_afiliado": "https://shopee.com.br"
    }
]

print("Buscando menores preços do dia na Shopee...")

# Salva a lista de produtos em um arquivo JSON que o site vai ler
with open("produtos.json", "w", encoding="utf-8") as f:
    json.dump(ofertas, f, ensure_ascii=False, indent=4)

print("produtos.json atualizado com sucesso!")
