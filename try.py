# Moment Calculator
def calculate_moment(force, distance):
    """Calculate moment using M = F * d"""
    moment = force * distance
    return moment
# Input from user
force = float(input("Enter the force (N): "))
distance = float(input("Enter the perpendicular distance (m): "))
# Calculate and display result
moment = calculate_moment(force, distance)
print(f"The moment about the point is {moment:.2f} N·m")

#Changes