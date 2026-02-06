def calc_rectangle(length,width):
    area= length*width
    perimeter=2*(length+width)
    return area,perimeter

length= int(input("Enter the length of rectangle:"))
width= int(input("Enter the width of rectangle:"))
area,perimeter= calc_rectangle(length,width)
print(f'Area:{area}, Perimeter:{perimeter}')