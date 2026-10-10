import math

angle_degrees = float(input("Enter the angle in degrees: "))

angle_radians = math.radians(angle_degrees)

sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)

print(f"\nResults for {angle_degrees}°:")
print(f"Sine (sin):    {sin_value:.4f}")
print(f"Cosine (cos):  {cos_value:.4f}")

if math.isclose(cos_value, 0, abs_tol=1e-9):
    print("Tangent (tan): Undefined (Infinity)")
else:
    print(f"Tangent (tan): {tan_value:.4f}")
