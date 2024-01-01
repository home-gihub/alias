heap = {}
aliascmds = {}

function lexer(command) {
    tokens = []

    i = 0
    j = 0

    while (i <= command.length - 1) {
        if (i == command.length - 1) {
            tokens.push(command.substring(j,command.length))
        } else if (command[i] == '"') {
            k = i + 1
            j = i
            while (k <= command.length - 1 && command[k] != '"') {
                k+=1
            }
            k += 1
            tokens.push(command.substring(j+1,k-1))
            j = k + 1
            i = k
        } else if (command[i] == " ") {
            tokens.push(command.substring(j,i))
            j = i + 1
        }
        
        i += 1
    }

    return tokens
}

function interpreter(tokens) {
    functions = {
        echo: function(tokens){
            console.log(tokens[1])
        },
        setvar: function(tokens){
            heap[tokens[1]] = tokens[2]
        },
        calcvar: function(tokens){
            switch (tokens[1]) {
                case "add":
                    heap[tokens[4]] = heap[tokens[1]] + heap[tokens[3]]
                    break;
                case "sub":
                    heap[tokens[4]] = heap[tokens[1]] - heap[tokens[3]]
                    break;
                case "mul":
                    heap[tokens[4]] = heap[tokens[1]] * heap[tokens[3]]
                    break;
                case "div":
                    heap[tokens[4]] = heap[tokens[1]] / heap[tokens[3]]
                    break;
                case "is":
                    heap[tokens[4]] = heap[tokens[1]] == heap[tokens[3]]
                    break;
                case "isnot":
                    heap[tokens[4]] = heap[tokens[1]] != heap[tokens[3]]
                    break;
            }
        },
        quit: function(tokens){
            throw new Error();
        },
        alias: function(tokens){
            temp = tokens
            temp = temp.slice(1)
            temp = temp.slice(1)
            aliascmds[tokens[1]] = temp
        },
        execalias: function(tokens){
            cmd = aliascmds[tokens[1]]
            for (i=0; i <= cmd.length; i++) {
                interpreter(lexer(cmd[i]))
            }
        }
    }

    functions[tokens[0]](tokens)
}

interpreter(lexer('echo "hello, World!'))