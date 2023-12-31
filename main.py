## Simple SIR model https://ja.wikipedia.org/wiki/SIR%E3%83%A2%E3%83%87%E3%83%AB
# 一つの都市における、SIRモデルに沿った感染の進行の仕方をモデルする
# 都市は、String のリストで表す。感受性保持者は"S", 感染者は、感染した日数を加えて"I0" や"I1", 復帰者は"R"
# 例えば、["S", "S", "I0", "I1", "R", "S"] は、感受性保持者3人、感染者2人（左から感染0日後、１日後）、復帰者1人の都市である。
# 簡略化のため、感染者と隣り合わせた"S"は必ず感染するものとする（感染力beta＝１）。
# また、感染者Iは、必ず決められた感染日数で回復して、復帰者Rになる。
# 例えば、感染日数が３であったら、I0 -> I1 -> I2 -> R （３日目には復帰者になっている）という変遷を辿る。
# 隣り合わせの個体は、隣人と捉え、隣人が感染者の時のみ、個体は感染する可能性がある。
# （これは、リストの各個体を都市の地区になぞらえて、地区同士の感染をモデル化するなどのマクロな視点取ることで正当化できる抽象化である）


def count_infected(city: list[str]) -> int:
    """
    ある都市を与えられた時に、その中の感染者の数を数えて、
    整数値で返す。
    例えば、city = ["S", "S", "I0", "I1", "R", "S"] の場合、
    2 を返す。
    """

    count = 0
    for num in city:
        if num[0] == "I":
            count = count + 1

    return count

def has_an_infected_neighbor(city: list[str], position: int) -> bool:
    """
    cityの与えられたposition にいる個人に、感染した隣人がいるかどうか確認。
    そのポジションの個人はSであることを前提して良い。
    """
    assert city[position] == "S" # 与えられたpositionの個人がS出ない場合はエラー
    n = len(city)
    has_infected_neighbor = False

    if position > 0 and city[position - 1][0] == "I":
        has_infected_neighbor = True
    elif position < n - 1 and city[position + 1][0]== "I":
        has_infected_neighbor = True
    else:
        has_infected_neighbor = False

    return has_infected_neighbor

### この下のコードは触らない

def main():
    return 0

if __name__ == "__main__":
    main()