# Rewrite in c++ or java, python is too slow
import os
import time
import sys

def remove_non_commands(code, commands):
    return ''.join(c for c in code if c in commands)

def bf(code, input_tape, expected_output, time_limit) -> tuple[int, str]:
    num_zeros = 30000
    input_read_pos = 0
    tape = [0] * num_zeros
    tickerpos = 15000
    commands = set("><+-.,[]?")
    code = remove_non_commands(code, commands)
    output = ""
    i = 0
    
    start=time.time()
    while i < len(code):
        if time.time()-start>time_limit:
            return 3, output
        char = code[i]
        if char == '>':
            tickerpos += 1
            if tickerpos >= num_zeros:
                return 2, output
        elif char == '<':
            tickerpos -= 1
            if tickerpos < 0:
                return 2, output
        elif char == '+':
            tape[tickerpos] = (tape[tickerpos] + 1) % 256
        elif char == '-':
            tape[tickerpos] = (tape[tickerpos] - 1) % 256
        elif char == '.':
            if tape[tickerpos] == 150:
                #print("–",end='')
                output+="–"
            elif tape[tickerpos] == 151:
                #print('—',end='')
                output+="—"
            else:
                #print(chr(tape[tickerpos]), end='')
                output+=chr(tape[tickerpos])
        elif char == ',':
            if input_read_pos >= len(input_tape):
                tape[tickerpos] = 0
            else:
                tape[tickerpos] = ord(input_tape[input_read_pos]) % 256
                input_read_pos += 1
        elif char == '[':
            if tape[tickerpos] == 0:
                    # find matching ]
                    count = 1
                    while count > 0:
                        i += 1
                        if code[i] == "[":
                            count += 1
                        elif code[i] == "]":
                            count -= 1
        elif char == ']':
            if tape[tickerpos] != 0:
                    # find matching [
                    count = 1
                    while count > 0:
                        i -= 1
                        if code[i] == "]":
                            count += 1
                        elif code[i] == "[":
                            count -= 1
        elif char == '?':
            print(*tape[15000:15015])
        else:
            pass
        i += 1
    if output == expected_output:
        return 0, output
    else:
        return 4, output
    
def main() -> int:
    if len(sys.argv) == 4:
        if not os.path.exists(sys.argv[1]):
            print("Program file not found")
            return 1
        if not os.path.exists(sys.argv[2]):
            print("Input file not found")
            return 1
        if not os.path.exists(sys.argv[3]):
            print("Output file not found")
            return 1
        with open(sys.argv[1], 'r') as f:
            code = f.read()
        with open(sys.argv[2], 'r') as f:
            input_tape = f.read()
        with open(sys.argv[3], 'r') as f:
            expected_output = f.read()
        
        resp = bf(code, input_tape, expected_output, 1.0)
        print(f"Expected output: {expected_output}")
        print(f"Program output: {resp[1]}")
        return resp[0]
    else:
        print("Usage: python bf.py [file] [input.txt] [output.txt]")
        return 1

if __name__ == "__main__":
    start = time.time()
    code = main()
    match code:
        case 0:
            print(f"Program passed in {(time.time()-start):.2f} seconds.")
        case 1:
            pass
        case 2:
            print(f"RE")
        case 3:
            print(f"TLE")
        case 4:
            print(f"WA")