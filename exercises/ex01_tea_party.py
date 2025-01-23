"""Katherine_Agudelo_Marin: Planning a tea party"""

__author__: str = "730655640"


def main_planner(guests: int) -> None:
    """All the information of tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Total number of teabags"""
    return people * 2


def treats(people: int) -> int:
    """Calculating number of treats"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Caluculating cost of tea bags and treats combined"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
