import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(product):
    """Создает продукт на оплату."""

    name_product = (f"{product.paid_course}" if product.paid_course else f"{product.paid_lesson}")
    stripe_product = stripe.Product.create(name=f"{name_product}")
    return stripe_product.get("id")


def create_stripe_price(sum_payment, stripe_product_id):
    """Создает цену в страйпе."""

    # print('sum_payment', sum_payment) # Что передается в 'sum_payment'

    return stripe.Price.create(
        currency="rub",
        unit_amount=sum_payment * 100,
        # product_data={"name": "Payments"},
        product=stripe_product_id,
    )


def create_stripe_session(sum_payment):
    """Создает сессию на оплату в страйпе."""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": sum_payment.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
