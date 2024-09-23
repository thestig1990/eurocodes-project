import random
import sys

# Change the encoding to UTF-8, which supports a wide range of characters, including Greek symbols.
sys.stdout.reconfigure(encoding='utf-8')


# Calculate the snow load shape coefficient μ_i
def calculate_snow_load_shape_coeff(α=0):
    if 0 <= α <= 30:
        μ_1 = 0.8
    elif 30 < α < 60:
        μ_1 = round(0.8 * (60 - α) / 30, 3)
    else:
        μ_1 = 0

    return μ_1


# Calculate the snow load shape coefficient μ_1 for the Monopitch roofs:
def calculate_snow_load_shape_coeff_monopitch(α=0):
    μ_1 = calculate_snow_load_shape_coeff(α)

    return μ_1


# Calculate the snow load shape coefficient μ_1 for the Pitched roofs:
def calculate_snow_load_shape_coeff_pitched(α_1=0, α_2=0):
    cases = ['Case i', 'Case ii', 'Case iii']
    random_case = random.choice(cases)
    if random_case == 'Case i':
        μ_1_α_1 = calculate_snow_load_shape_coeff(α_1)
        μ_1_α_2 = calculate_snow_load_shape_coeff(α_2)
    elif random_case == 'Case ii':
        μ_1_α_1 = 0.5 * calculate_snow_load_shape_coeff(α_1)
        μ_1_α_2 = calculate_snow_load_shape_coeff(α_2)
    else:
        μ_1_α_1 = calculate_snow_load_shape_coeff(α_1)
        μ_1_α_2 = 0.5 * calculate_snow_load_shape_coeff(α_2)

    return μ_1_α_1, μ_1_α_2


# Calculate the snow load shape coefficient μ_1 and μ_2 for the Multi-span roofs:
def calculate_snow_load_shape_coeff_multispan(α_1=0, α_2=0):

    μ_1_α_1 = calculate_snow_load_shape_coeff(α_1)
    μ_1_α_2 = calculate_snow_load_shape_coeff(α_2)
    α = (α_1 + α_2) / 2
    μ_2_α = calculate_snow_load_shape_coeff(α)

    return μ_1_α_1, μ_1_α_2, μ_2_α


# Snow load on roofs for the persistent/transient design situations:
def calculate_snow_loads(α=0, S_k=1550, C_e=1, C_t=1):
    """_summary_

    Args:
        S_k (int, optional): _description_. Defaults to 1550.
        C_e (int, optional): _description_. Defaults to 1.
        C_t (int, optional): _description_. Defaults to 1.

    Returns:
        _type_: _description_
    """
    # Calculate Snow load for the Monopitch roofs
    μ_i = calculate_snow_load_shape_coeff_monopitch(α)
    S_monopitch = μ_i * C_e * C_t * S_k

    # Calculate Snow load for the Pitched roofs
    μ_1_α_1, μ_1_α_2 = calculate_snow_load_shape_coeff_pitched(30, 50)
    S_pitched_α_1 = μ_1_α_1 * C_e * C_t * S_k
    S_pitched_α_2 = μ_1_α_2 * C_e * C_t * S_k
    
    # Calculate Snow load for the Multi-span roofs
    μ_1_α_1, μ_1_α_2, μ_2_α = calculate_snow_load_shape_coeff_multispan(30, 50)
    S_multispan_α_1 = μ_1_α_1 * C_e * C_t * S_k
    S_multispan_α_2 = μ_1_α_2 * C_e * C_t * S_k
    S_multispan_α = μ_2_α * C_e * C_t * S_k
    
    return f"""Snow load on Monopitch roofs for the persistent/transient design situations: S = {round(S_monopitch/1000, 3)} kH/m2;
Snow load on Pitched roofs for the persistent/transient design situations: S_μ1(α1) = {round(S_pitched_α_1/1000, 3)} kH/m2; S_μ1(α2) = {round(S_pitched_α_2/1000, 3)} kH/m2;
Snow load on Multi-span roofs for the persistent/transient design situations: S_μ1(α1) = {round(S_multispan_α_1/1000, 3)} kH/m2; S_μ1(α2) = {round(S_multispan_α_2/1000, 3)} kH/m2; ; S_μ2(α) = {round(S_multispan_α/1000, 3)} kH/m2
    """

print(calculate_snow_loads())