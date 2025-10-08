u_n = input("Enter your full name (First, Middle, Last): ")

parts = u_n.strip().split(",")

first = parts[0].strip().capitalize()
middle = parts[1].strip().capitalize()
last = parts[2].strip().title()

m_i = middle[0] + "."

fin1 = last + ", " + first + " " + m_i

print(fin1)