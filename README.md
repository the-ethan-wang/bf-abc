# BF ABC

example usage
```bash
python bf.py 451/01.bf 451/in3.txt 451/out3.txt
python bftc.py 451 3
```
Notes: bftc assumes problem A(01.bf). Also my file management hasn't accounted for testcases for other problems lol.

## Snippets

### Input to an array terminating at newline

- Takes input to an array
- Requires |S| cells to the right
- array starts at cell 2 and point ends at cell 2

```
>,----------[++++++++++>,----------]<[<]>
```

### Yes/No from flag cell

- Outputs Yes if the current cell is nonzero and No if zero
- Requires 1 empty cell to the right
- Lossy function

```
[[-]+[--->++<]>+++.[-<++++>]<+.[--->+<]>----.[-]-<]>+[[-]-[---<+>]<-------.-[--->+<]>.[-]]
```

cases in `000/`

```bash
python bftc.py 000 1
python bftc.py 000 2
```

### Output 1-3 digit integers from a cell

- Outputs the current cell in decimal representation
- requires ~10 cells to the right, give it 15 to be safe
- lossy

```
>++++++++++<
[>[<->->>+>->]<+[->>+>[<<+>>-]>[-]]<<<<]>[[-]<->]<+[>>+>[<<+>>-]<<<[-]]>[-]>[-<<+>>]>[-<<+>>]<<<
>[->>>>>+<<<<<]<
>++++++++++<
[>[<->->>+>->]<+[->>+>[<<+>>-]>[-]]<<<<]>[[-]<->]<+[>>+>[<<+>>-]<<<[-]]>[-]>[-<<+>>]>[-<<+>>]<<<
[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]>
[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]>>>>>
++++++++++++++++++++++++++++++++++++++++++++++++.[-]
```

cases in `001/`

```bash
python bftc.py 001 1
python bftc.py 001 2
python bftc.py 001 3
python bftc.py 001 4
python bftc.py 001 5
```

## Notes

thinking about how to take in space separated inputs...  
notes on this will be in `bf-abc/454/01.bf`

Also thinking about how to take in an integer n (1<=n<=255) to a cell (wait you can just write to an array terminating at space)

## AC list

### problem A
- 442
- 443
- 444
- 445
- 446
- 450
- 451
- 455

## Submit these

## problem A
- none
