from __future__ import annotations
from dataclasses import dataclass, field


@dataclass(frozen=False , order = True)
class Item:
    name: str = field(compare=False)
    price: float  = field(compare=True)
    quantity: int = field(compare=False)

    def __post_init__(self):
        if not isinstance(self.name, str) or self.name.strip() == "":
            raise ValueError("Name must be a non-empty string")
        if not isinstance(self.price, (int, float)) or self.price < 0:
            raise ValueError("Price must be a non-negative number")
        if not isinstance(self.quantity, int) or self.quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")

    def total_value(self) -> float:
        return self.price * self.quantity

    def restock(self, amount: int) -> None:
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Restock amount must be a positive integer")
        self.quantity += amount

    def sell(self, amount: int) -> None:
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Sell amount must be a positive integer")
        if amount > self.quantity:
            raise ValueError(f"Cannot sell {amount}, only {self.quantity} available")
        self.quantity -= amount
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Item):
            return NotImplemented
        return self.quantity == other.quantity

    def __str__(self) -> str:
        return f"{self.name} | Price: {self.price} | Qty: {self.quantity} | Total: {self.total_value()}"


def main():
    item = Item(name="Apple", price=1.5, quantity=100)
    print(item)

    item.restock(50)
    print(f"After restock: {item}")

    item.sell(30)
    print(f"After sell: {item}")

    print(f"Total value: {item.total_value()}")

    try:
        item.sell(999)
    except ValueError as e:
        print(f"Error: {e}")
    
    item2 = Item(name="Banana", price=0.5, quantity=200)
    print(f"Comparing items: {item} < {item2} = {item < item2}")
    item.restock(50)
    print(f"Comparing items after restock: {item} < {item2} = {item < item2}")


if __name__ == "__main__":
    main()