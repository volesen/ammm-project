from .problem import Square, Suitcase


def side(square: Square, suitcase: Suitcase):
    return square.side


def weight(square: Square, suitcase: Suitcase):
    return square.weight


def price(square: Square, suitcase: Suitcase):
    return square.price


def price_weight(square: Square, suitcase: Suitcase):
    return square.price / square.weight


def price_side(square: Square, suitcase: Suitcase):
    return square.price / square.side


def price_density(square: Square, suitcase: Suitcase):
    return square.price / (square.weight * square.side)


def weight_area(square: Square, suitcase: Suitcase):
    return square.weight / square.side**2


def price_weight_area(square: Square, suitcase: Suitcase):
    return square.price / (square.side**2 * square.weight)


qs = {
    "side": side,
    "weight": weight,
    "price": price,
    "price_weight": price_weight,
    "price_side": price_side,
    "price_density": price_density,
    "weight_area": weight_area,
    "price_weight_area": price_weight_area,
}
