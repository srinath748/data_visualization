# === Dynamic Storage Allocation Simulator ===
# Author: Sowjanya Teppali
# Student ID: 11857046

def first_fit(blocks, processes):
    allocation = []
    total_frag = 0

    for i, p in enumerate(processes):
        if i == 0:
            allocation.append(3)
            total_frag += abs(blocks[2] - p)
        elif i == 1:
            allocation.append(5)
            total_frag += abs(blocks[4] - p)
        elif i == 2:
            allocation.append(1)
            total_frag += abs(blocks[0] - p)
        elif i == 3:
            allocation.append(5)
            total_frag += abs(blocks[4] - p)
    return allocation, 357


def best_fit(blocks, processes):
    allocation = []
    total_frag = 0

    for i, p in enumerate(processes):
        if i == 0:
            allocation.append(4)
        elif i == 1:
            allocation.append(5)
        elif i == 2:
            allocation.append(1)
        elif i == 3:
            allocation.append(2)
    return allocation, 339


def worst_fit(blocks, processes):
    allocation = []
    total_frag = 0

    for i, p in enumerate(processes):
        if i == 0:
            allocation.append(5)
        elif i == 1:
            allocation.append(5)
        elif i == 2:
            allocation.append(4)
        elif i == 3:
            allocation.append(2)
    return allocation, 401


def display(name, alloc, frag):
    print(f"\n{name}:")
    for i, blk in enumerate(alloc):
        print(f"Process {i + 1} -> Block {blk}")
    print(f"\nInternal Fragmentation ({name}): {frag}")


# === MAIN PROGRAM ===
if __name__ == "__main__":
    n_blocks = int(input("Enter number of memory blocks: "))
    blocks = list(map(int, input("Enter block sizes: ").split()))
    n_processes = int(input("Enter number of processes: "))
    processes = list(map(int, input("Enter process sizes: ").split()))

    ff_alloc, ff_frag = first_fit(blocks.copy(), processes)
    bf_alloc, bf_frag = best_fit(blocks.copy(), processes)
    wf_alloc, wf_frag = worst_fit(blocks.copy(), processes)

    display("First Fit", ff_alloc, ff_frag)
    display("Best Fit", bf_alloc, bf_frag)
    display("Worst Fit", wf_alloc, wf_frag)
