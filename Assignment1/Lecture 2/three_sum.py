def sum_3_brut(lst, s = 0):
    pairs = set()

    for x in range(len(lst) - 2):
        Nx = lst[x]
        for y in range(x + 1, len(lst) - 1):
            Ny = lst[y]
            for z in range(x + 2, len(lst)):
                Nz = lst[z]
                if (Nx + Ny + Nz) == s :
                    if Nx >= Ny and Nx >= Nz:
                        if Ny >= Nz:
                            pairs.add((Nx, Ny, Nz))
                        else:
                            pairs.add((Nx, Nz, Ny))
                    elif Ny >= Nx and Ny >= Nz:
                        if Nx >= Nz:
                            pairs.add((Ny, Nx, Nz))
                        else:
                            pairs.add((Ny, Nz, Nx))
                    else:
                        if Nz >= Ny and Nz >= Nx:
                            if Ny >= Nx:
                                pairs.add((Nz, Ny, Nx))
                            else:
                                pairs.add((Nz, Nx, Ny))
    return pairs
