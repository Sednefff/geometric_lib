# Library for computing properties of some geometric objects
This project includes functions to calculate the area and the perimeter of such common geometric objects as circle, rectangle, square, triangle.


## Functions

### cicle

####  area(r):
Calculates the area of a circle

- **Input parameters**:
    - r (float/int): radius of a circle

- **Returns**:
    - float: area of the circle

- **Example**:
    ```python
    >>> area(5)
    78.53981633974483
    ```

#### perimeter(r):
Calculates the perimeter of a circle
    
- **Input parameters**:
    r (float/int): radius of a circle

- **Returns**:
    float: perimeter of the circle
    
- **Example**:
    ```python
    >>> perimeter(5)
    31.41592653589793
    ```

### rectangle

#### area(a, b):
Calculates the area of a rectangle
    
- **Input parameters**:
    - a (float/int): height of a rectangle
    - b (float/int): width of a rectangle

- **Returns**:
    - float: area of the rectangle
    
- **Example**:
    ```python
    >>> area(5,6)
    30
    ```

#### perimeter(a, b): 
Calculates the perimeter of a rectangle
    
- **Input parameters**:
    - a (float/int): height of a rectangle
    - b (float/int): width of a rectangle

- **Returns**:
    - float: perimeter of the rectangle
    
- **Example**:
    ```python
    >>> perimeter(5,6)
    22
    ```

### square

#### area(a):
Calculates the area of a square
    
- **Input parameters**:
    - a (float/int): length of square's side

- **Returns**:
    - float: area of the square
    
- **Example**:
    ```python
    >>> area(5)
    25
    ```


#### perimeter(a):
Calculates the perimeter of a square
    
- **Input parameters**:
    - a (float/int): length of square's side

- **Returns**:
    - float: perimeter of the square
    
- **Example**:
    ```python
    >>> perimeter(5)
    20
    ```

### triangle

#### area(a, h): 
Calculates the area of a triangle
    
- **Input parameters**:
    - a (float/int): length of triangle's side
    - h (float/int): height of a triangle connected to a-side

- **Returns**:
    float: area of the triangle
    
- **Example**:
    ```python
    >>> area(5,6)
    15
    
    ```

#### perimeter(a, b, c):
Calculates the perimeter of a triangle
    
- **Input parameters**:
    - a (float/int): length of triangle's side
    - b (float/int): length of triangle's side
    - c (float/int): length of triangle's side

- **Returns**:
    - float: perimeter of the triangle

- **Example**:
    ```python
    >>> perimeter(5,6,7)
    18
    
    ```

## Change history

| Commit hash | Changes |
|-|-|
|ca105708573b577e89db97e966fe3b91a57632c0| Added documentation|
|8b661c0d5aec962ef8abc44fbef25bcc43534099|added triangle.py, fixed rectangle.py|
|889c7d596a2cd14fe73b269ca52bb3622c6edcf7|added rectangle.py|