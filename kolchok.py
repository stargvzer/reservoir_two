import random

token = "1894255132:AAGtDWoujDO8S2vq5K6oTylDxdXwkdaHInU"

startAnswer = "Прет, обоссал тя, чмохенсон"
kolchok = ["Всем известно, что на колчане сидят морально разложившиеся дегенераты, "
           "у которых нет ничего святого. Тут это стало нормой.",
           "1чан окончательно потерял смысл своего существования."
          "Дискач", "Я решил признаться, я очень долго скрежетал зубами "
                    "от баттхерта по поводу девственности и того, "
           "что жиды кругом, "
           "поэтому стер все зубы, и теперь они у меня прочные, латунные."]

random_message = lambda: random.choice(kolchok)
