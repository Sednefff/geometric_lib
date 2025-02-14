# My math library for calculate area and perimeter of some geometric figures

Library can use for calculate area and perimeter for:  
- Circle  
- Rectangle  
- Square  
- Triangle  

# Math formulas which use in functions:
## Area
- Circle: S = πR²           for circle_area
- Rectangle: S = ab         for rectangle_area
- Square: S = a²            for square_area
- Triangle: S = a * h / 2   for triangle_area

## Perimeter
- Circle: P = 2πR           for circle_perimeter
- Rectangle: P = 2a + 2b    for rectangle_perimeter
- Square: P = 4a            for square_perimeter
- Triangle: P = a + b + c   for triangle_perimeter

# Example use library function:

## Calculate area
```python
'''
For circle
Return 314.1592653589
'''
circle_area(10)

''' Return 25.1327412287 '''
circle_perimeter(4)

'''
For triangle
Return 30
'''
triangle_area(6, 10)

''' Return 23 '''
triangle_perimeter(7, 7, 9)

'''
For rectangle
Return 72
'''
rectangle_area(6, 12)

''' Return 26 '''
rectangle_perimeter(9, 4)

'''
For square
Return 100
'''
square_area(10)

''' Return 24 '''
square_perimeter(6)
```

# About unit tests

Unit tests in this library check a lot of different situation

[For get more information](tests.pdf)

___

 Use next command for start unit test for concrete file of library

`python -m unittest <name file>`

# History of work
- [[d80116](https://github.com/itmo-coder/geometric_lib_fork/commit/d8011695c5ec0061fb839ac5766b73b422fece4c)] add: automatic tests with github actions

- [[0499e7](https://github.com/itmo-coder/geometric_lib_fork/commit/0499e7af98f1d5373eb746417c1b1d95986eb602)] add: docs for unit tests in this library

- [[24e3fca](https://github.com/itmo-coder/geometric_lib_fork/commit/24e3fcafd3cf951e431bc7c93831a6cb9866bdbd)] add: unit test for all functions

- [[8dbc702](https://github.com/itmo-coder/geometric_lib_fork/tree/8dbc702512914a38746887ff7fcc0e7fa6669fd5)] add: examples of returns in README.md

- [[4b75e8d](https://github.com/itmo-coder/geometric_lib_fork/tree/4b75e8d343704df927ded1658fb99009a94968fb)] fix: use one style in all files

- [[f5a915a](https://github.com/itmo-coder/geometric_lib_fork/tree/f5a915ab1a760668251c3e50d5b30f14fb5eb70c)] add: description for all function and fix names

- [[ba98d8d](https://github.com/itmo-coder/geometric_lib_fork/tree/ba98d8d99032d9beee83558f505919ad219f4622)] fix: calculate perimetr of rectangle

- [[586b6da](https://github.com/itmo-coder/geometric_lib_fork/tree/586b6da25c268a0002b860dcdee1e89d6d586824)] add: functions for calculate triangle area and perimetr

- [[201cab2](https://github.com/itmo-coder/geometric_lib_fork/tree/201cab27083eb43ac003b53db7406185303d14f4)] add: file for calculate rectangle area and perimetr

