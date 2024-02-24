# while dengan nilai bool
status = True
has_loop = 1
while status:
    print(f"running.. {has_loop}")

    # stopling loop
    if has_loop == 10:
        status = False

    has_loop += 1

# while dengan kondisi
max_loop = 1
while max_loop <= 10:
    print(f'running max loop {max_loop}')
    max_loop += 1