# Rates
STOP_RATE = 0.02  # 2 cents per second
MOVE_RATE = 0.05  # 5 cents per second
VAT_RATE = 0.21   # 21% VAT(Value Added Tax = IVA)

def calculate_cost(time_stopped, time_moving):
    """   Calculate the total cost based on time stopped and time moving.
    """
    cost_stopped = time_stopped * STOP_RATE
    cost_moving = time_moving * MOVE_RATE
    return cost_stopped + cost_moving

def apply_vat(cost):
    """
    Apply 21% VAT to the total cost.
    """
    return cost * (1 + VAT_RATE)