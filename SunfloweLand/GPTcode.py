from datetime import timedelta

# Definição dos preços das sementes
prices_coins = {
    "sunflower": 0.01,
    "potato": 0.1,
    "pumpkin": 0.2,
    "carrot": 0.5,
    "cabbage": 1.0,
    "soybean": 1.5,
    "beetroot": 2.0,
    "cauliflower": 3.0,
    "parsnip": 5.0,
    "eggplant": 6.0,
    "corn": 7.0,
    "radish": 7.0,
    "wheat": 5.0,
    "kale": 7.0
}

# Quantidade de sementes por Block Buck (estoque inicial)
seeds_per_blockbuck = {
    "sunflower": 400,
    "potato": 200,
    "pumpkin": 150,
    "carrot": 100,
    "cabbage": 90,
    "soybean": 90,
    "beetroot": 80,
    "cauliflower": 80,
    "parsnip": 60,
    "eggplant": 50,
    "corn": 50,
    "radish": 40,
    "wheat": 40,
    "kale": 30
}

# Grow time de cada plantação (modifique baseado em seus buffs verifique no sfl.world>boost)
growth_times = {
    "sunflower": timedelta(seconds=43),
    "potato": timedelta(minutes=3, seconds=38),
    "pumpkin": timedelta(minutes=21, seconds=48),
    "carrot": timedelta(minutes=43, seconds=36),
    "cabbage": timedelta(hours=1, minutes=27, seconds=12),
    "soybean": timedelta(hours=2, minutes=10, seconds=48),
    "beetroot": timedelta(hours=2, minutes=54, seconds=25),
    "cauliflower": timedelta(hours=5, minutes=48, seconds=50),
    "parsnip": timedelta(hours=8, minutes=43, seconds=15),
    "eggplant": timedelta(hours=11, minutes=37, seconds=40),
    "corn": timedelta(hours=14, minutes=32, seconds=6),
    "radish": timedelta(hours=17, minutes=26, seconds=31),
    "wheat": timedelta(hours=17, minutes=26, seconds=31),
    "kale": timedelta(hours=26, minutes=9, seconds=46)
}

# Buff específico para cada planta
buffs = {
    "sunflower": 1.27,
    "potato": 1.27,
    "pumpkin": 1.27,
    "carrot": 1.27,
    "cabbage": 1.27,
    "soybean": 1.27,
    "beetroot": 1.27,
    "cauliflower": 1.27,
    "parsnip": 1.27,
    "eggplant": 1.27,
    "corn": 1.27,
    "radish": 1.27,
    "wheat": 1.27,
    "kale": 1.27
}

# Outras variáveis de controle/valor
valorBlockB = 0.15
cropPlot = 33

def reduce_seeds_and_generate_report():
    total_time = timedelta()
    daily_report = {}
    for seed, initial_stock in seeds_per_blockbuck.items():
        growth_time = growth_times[seed]
        buff = buffs[seed]
        while initial_stock > 0:
            plant_amount = min(initial_stock, cropPlot)
            initial_stock -= plant_amount
            total_time += growth_time
            day = total_time.total_seconds() // (3600 * 24)
            if day not in daily_report:
                daily_report[day] = {}
            if seed not in daily_report[day]:
                daily_report[day][seed] = {"cycles": 0, "total_planted": 0}
            daily_report[day][seed]["cycles"] += 1
            daily_report[day][seed]["total_planted"] += plant_amount
    return total_time, daily_report

# Exemplo de uso da função
total_time_taken, report = reduce_seeds_and_generate_report()
print(f"Tempo total para reduzir o estoque de sementes a 0: {total_time_taken}")
print("Relatório diário das plantas plantadas:")
for day, plants in report.items():
    print(f"Dia {int(day)+1}:")
    for seed, details in plants.items():
        print(f"  {seed} x{details['cycles']} ({details['total_planted'] * buffs[seed]:.2f} seeds)")
