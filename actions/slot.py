from enum import Enum


class PizzaSize(Enum):
    LARGE = 'large'
    MEDIUM = 'medium'
    SMALL = 'small'


class PizzaCrust(Enum):
    THICK = 'thick'
    THIN = 'thin'


class PizzaTopping(Enum):
    PEPPERONI = 'pepperoni'
    SAUSAGE = 'sausage'
    MUSHROOMS = 'mushrooms'
    GREEN_BELL_PEPPERS = 'green bell peppers'
    ONIONS = 'onions'
    BLACK_OLIVES = 'black olives'
    GREEN_OLIVES = 'green olives'
    BACON = 'bacon'
    PINEAPPLE = 'pineapple'
    HAM = 'ham'
    CHEESE = 'cheese'
