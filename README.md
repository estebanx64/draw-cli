# Draw-cli python



## Coding challenge



### Introduction to the problem

you are free to implement any mechanism for feeding input into your solution. you should provide sufficient evidence with unit test that your solutions is complete. as a minimum, please use the provided test data to indicate that the solution works correctly, any programming language can be used to solve the problem.



### Drawning tool

you are given the task of writing a simple console version of a drawning program. at this time, the functionality of the program is quite limited but this might change in the future. in a nutshell, the program should work as follows:

1. Create a new canvas
2. Start drawning on the canvas by issuing various commands
3. Quit

At the moment, the program should support the following commands:

C w h      Should create a new canvas of width w and height h.

L x1 y1 x2 y2        Should create a new line from (x1, y1) to (x2, y2). Currently only horizontal or vertical lines are supported. Horizontal and vertical lines will be drawm using the 'x' character.

R x1 y1 x2 y2     Should create a new rectangle, whose upper left corner is (x1, y1) and lower right corner is (x2, y2). horizontal and vertical lines will be drawm using the 'x' character.

B x y c      Should fill the entire area connected to (x,y) with "colour" c. The behaviour of this is the same as that of the "bucket fill" tool in paint programs.

Q Should quit the program.



**Create a new matrix**

```bash
Enter command: c 20 4
|                    |
|                    |
|                    |
|                    |
```



**Create horizontal line**

```bash
Enter command: l 1 2 6 2
|                    |
|xxxxxx              |
|                    |
|                    |
```



**Create vertical line**

```bash
Enter command: l 6 3 6 4
|                    |
|xxxxxx              |
|     x              |
|     x              |
```



**Create rectangle**

```bash
Enter command: r 16 1 20 3
|               xxxxx|
|xxxxxx         x   x|
|     x         xxxxx|
|     x              |
```



**Flood fill**

```bash
Enter command: b 10 3 o
|oooooooooooooooxxxxx|
|xxxxxxooooooooox   x|
|     xoooooooooxxxxx|
|     xoooooooooooooo|
```



**Running test**

```bash
$ python test_draw.py -v
test_floodFill (__main__.TestDrawMethods) ... ok
test_line (__main__.TestDrawMethods) ... ok
test_newMatriz (__main__.TestDrawMethods) ... ok
test_rectangle (__main__.TestDrawMethods) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

