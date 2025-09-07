# Motion Type Identifier Template

 

# Function 1: Convert velocity to m/s

def convert_velocity(v_value, v_unit):

    if v_unit == "m/s":
        return v_value
    elif v_unit == "km/s":
        return v_value * 1000 # or value * 5/18
    elif v_unit == "mi/s":
        return v_value * 1609.344
    elif v_unit == "ft/s":
        return v_value * 0.3048
    else:
        return "Error. Enter a valid value."

    # TODO: Implement conversion using if-elif-else

    pass

 

# Function 2: Convert acceleration to m/s²

def convert_acceleration(a_value, a_unit):

    if a_unit == "m/s²":
        return a_value
    elif a_unit == "km/s²":
        return a_value * 1000   # or value * 5/18
    elif a_unit == "mi/s²":
        return a_value / 1609.344
    elif a_unit == "ft/s²":
        return a_value * 0.3048
    else:
        return "Error. Enter a valid value."
    
    # TODO: Implement conversion using if-elif-else

    pass

 

# Function 3: Determine motion type

def motion_type(a_value, a_unit):

    if a_value == 0:
        return "At Rest"
    elif a_value > 0 and a_unit == 0:
        return "Uniform Motion"
    elif a_value > 0 and a_unit > 0:
        return "Accelerated Motion"
    elif a_value > 0 and a_unit < 0:
        return "Decelerated Motion"
    else:
        return "Error. Enter valid value."

    # TODO: Implement selection structure to return motion type

    pass

 

# --- Main Program ---

 

# Step 1: Input velocity

v_value = float(input("Enter velocity value: "))

v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")

 

# Step 2: Input acceleration

a_value = float(input("Enter acceleration value: "))

a_unit = input("Enter acceleration unit (m/s², ft/s², km/s², mi/s²): ")

 

# Step 3: Convert to SI units

v_si = convert_velocity(v_value, v_unit)      # TODO: Call the conversion function

a_si = convert_acceleration(a_value, a_unit)  # TODO: Call the conversion function

 

# Step 4: Determine motion type

motion = motion_type(v_si, a_si)              # TODO: Call the motion type function

 

# Step 5: Display results

print("\n--- Results ---")

print(f"Velocity = {v_si:.3f} m/s")

print(f"Acceleration = {a_si:.3f} m/s²")

print(f"Motion Type = {motion}")