import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_price(sum_payment):
    """Создает цену в страйпе."""

    return stripe.Price.create(
        currency="rub",
        unit_amount=sum_payment * 100,
        product_data={"name": "Payments"},
    )


def create_stripe_session(sum_payment):
    """Создает сессию на оплату в страйпе."""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": sum_payment.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
