AC

take input
,>,,>,,<<

copy b to 4th cell
>[->>+>+<<<]>>>[-<<<+>>>]<<<<

subtract A from B
[->-<]

subtract b from c
>>>[-<->]<<<

set cell 1 to flag: 1 if cell 2 is nonzero and 0 if cell 2 is zero
>[<+>[-]]<

set cell 2 to flag: 1 if cell 3 is zero and 0 if cell 3 is nonzero
>+>[<->[-]]<<

set cell 3 to intersection of cell 1 and 2: 1 if both are 1 but 0 if either is 0
[>>>+<<<[-]]>[>>+<<[-]]>+>--[<->[-]]<<<

if cell 3 is 1 then output Yes else output No
>>[[-]+[--->++<]>+++.[->++++<]>+.[--->+<]>----.>>>>>>->]<+[--[--->+<]>-------.-[--->+<]>.[-]]

minified code (remove the [-])
[-][,>,,>,,<[->>+>+<<<]>>>[-<<<+>>>]<<<<[->-<]>>>[-<->]<<[<+>[-]]+>[<->[-]]<<[>>>+<<<[-]]>[>>+<<[-]]>+>--[<->[-]]<[[-]+[--->++<]>+++.[->++++<]>+.[--->+<]>----.>>>>>>->]<+[--[--->+<]>-------.-[--->+<]>.[-]]]