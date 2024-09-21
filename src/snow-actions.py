import random


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


print(calculate_snow_load_shape_coeff_pitched())


#  Snow loads on roofs for the persistent/transient design situations:
def calculate_snow_loads(α=55, C_e=1, C_t=1, S_k=1550):
    μ_i = calculate_snow_load_shape_coeff_monopitch(α)
    print(μ_i, S_k)
    S = μ_i * C_e * C_t * S_k

    return f"{S/1000} kH/m2"

print(calculate_snow_loads())