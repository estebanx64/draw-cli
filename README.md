# Draw-cli python

![img for chanllengue](/home/esteban/Descargas/coding-chanllenge.png)

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

