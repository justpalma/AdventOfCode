filename = "resources/day_10_input.txt"
#filename = "resources/debug.txt"


def reset_buffer():
    buff = []
    for x in range(40):
        buff.append('.')
    return buff


def update_CRT_row(crt, index, pixel, action):
    if action:
        crt[index][pixel] = '#'
    else:
        crt[index][pixel] = '.'
    return crt


def update_sprite(x):
    s = reset_buffer()
    s[x] = '#'
    if x-1 >= 0:
        s[x-1] = '#'
    if x+1 < 40:
        s[x+1] = '#'
    return s


def get_index_cicle(cicle):
    if cicle == 240:
        cicle = 239
    return (cicle // 40)


def update(pixel, sprite_pos):
    return True if sprite_pos[pixel] == '#' else False





def resolve():
    try:
        x = 1
        CRT_rows = [reset_buffer() for x in range(6)]
        sprite_pos = update_sprite(x)
        cicle = 0
        pixel = 0
        with open(filename) as file:
            for line in file:
                line = line.rstrip()
                command = line.split(' ')[0]
                if command == 'addx':
                    inc = int(line.split(' ')[1])
                    for sub in range(2):
                        cicle += 1
                        if pixel == 40:
                            pixel = 0
                        index = get_index_cicle(cicle)
                        update_CRT_row(CRT_rows, index, pixel, update(pixel, sprite_pos))
                        if sub == 1:
                            x+= inc
                        pixel += 1
                else:
                    cicle += 1
                    if pixel == 40:
                        pixel = 0
                    index = get_index_cicle(cicle)
                    update_CRT_row(CRT_rows, index, pixel, update(pixel, sprite_pos))
                    pixel += 1

                sprite_pos = update_sprite(x)
        print(CRT_rows[0])
    except Exception as e:
        print(f'x {x}, cicle {cicle}, pixel {pixel}')
    finally:
        for x in CRT_rows:
            print(''.join(x))




resolve()
