def can_close(opener, closer):
    if closer == ')':
        return opener == '('
    if closer == '}':
        return opener == '{'
    if closer == ']':
        return opener == '['
    return False

def checker(array):
    queue = list()
    opens = ['(','{','[']
    for word in array:
        print (queue)
        if word in opens:
            queue.append(word)
        else:
            if len(queue) == 0:
                return False
            if can_close(queue[len(queue)-1], word):
                queue.pop()
            else:
                return False

    return len(queue) == 0


def enconding(pharse):
    letters = list()
    reps = list()
    for i in pharse:
        if not letters:
            letters.append(i)
            reps.append(1)
        else:
            last = len(letters)-1
            if letters[len(letters)-1] == i:
                reps[last] += 1
            else:
                letters.append(i)
                reps.append(1)
    encod = [str(item) for pair in zip(reps, letters) for item in pair]

    return "".join(encod)

def decode(pharse):
    idx = 0
    words = ''
    while idx < len(pharse):
        times = int(pharse[idx])
        word = pharse[idx+1]
        tmp = [word for i in range(times)]
        words += ''.join(tmp)
        idx+=2

    return words



def main():
    # print (checker('(([][{]))'))
    encod = 'AAABBBDDTEEEE'
    encond = enconding(encod)
    print (encond)
    print( decode(encond))

if __name__ == "__main__":
    main()