import shapes

def main():
    print("--- Area Calculator ---")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        area = shapes.area_circle(radius)
        print(f"The area of the circle is: {area:.2f}")
        
    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = shapes.area_rectangle(length, width)
        print(f"The area of the rectangle is: {area:.2f}")
        
    elif choice == '3':
        # Treating length and width as base and height as requested by the prompt
        length = float(input("Enter the length (base) of the triangle: "))
        width = float(input("Enter the width (height) of the triangle: "))
        area = shapes.area_triangle(length, width)
        print(f"The area of the triangle is: {area:.2f}")
        
    else:
        print("Invalid choice! Please run the program again and select 1, 2, or 3.")

if __name__ == "__main__":
    main()
