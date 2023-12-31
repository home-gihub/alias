heap = {}
aliascmds = {}


def lexer(command):
    tokens = []

    j=0
    i=0

    while i <= len(command) - 1:
        if i == len(command) - 1:
            tokens.append(command[j:len(command)])
        elif command[i] == '"':
            k = i + 1
            j = i
            while k <= len(command) - 1 and command[k] != '"':
                k+=1
            k += 1
            tokens.append(command[j+1:k-1])
            j = k + 1
            i = k
        elif command[i] == " ":
            tokens.append(command[j:i])
            j = i + 1
        i+=1

    return tokens


def interpreter(tokens):
    def quit_c(tokens):
        quit(0)

    def echo(tokens):
        if len(tokens) != 2:
            quit(1)
        print(tokens[1])

    def setvar(tokens):
        if len(tokens) != 3:
            quit(1)
        heap[tokens[1]] = tokens[2]

    def alias(tokens):
        if len(tokens) < 3:
            quit(1)
        temp = tokens
        temp.pop(0)
        temp.pop(0)
        aliascmds[tokens[1]] = temp

    def execalias(tokens):
        cmd = aliascmds[tokens[1]]
        for i in range(0, len(cmd)):
            interpreter(lexer(cmd[i]))


    def calcvar(tokens):
        if len(tokens) != 5:
            quit(1)

        match tokens[2]:
            case "add":
                heap[tokens[4]] = heap[tokens[1]] + heap[tokens[3]]
            case "sub":
                heap[tokens[4]] = heap[tokens[1]] - heap[tokens[3]]
            case "mul":
                heap[tokens[4]] = heap[tokens[1]] * heap[tokens[3]]
            case "div":
                heap[tokens[4]] = heap[tokens[1]] / heap[tokens[3]]
            case "is":
                heap[tokens[4]] = heap[tokens[1]] == heap[tokens[3]]
            case "isnot":
                heap[tokens[4]] = heap[tokens[1]] != heap[tokens[3]]

    functions = {
        "echo": echo,
        "setvar": setvar,
        "calcvar": calcvar,
        "quit": quit_c,
        "alias": alias,
        "execalias": execalias
    }

    functions[tokens[0]](tokens)
