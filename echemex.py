import numpy as np

def readcv(FILE, cycle, E_ref, area):
    
    if cycle == -1:
        full = 1
    else:
        cycle = cycle - 1
        full = 0
        
    with open(FILE, "r") as f:
        for s in range(13):
            _ = f.readline()
        
        scanrate = []
        scan = f.readline().split()
        scan = np.array(scan)
        scanrate.append(float(scan[2]))
            
        for r in range(51):
            _ = f.readline()
                    
        V = []
        I = []
        counter = 0;
        
        for x in f:
            data = x.split()
            data = np.array(data)
            
            try:
                float(data[0])
                if (counter == cycle) or (full == 1):
                    V.append(float(data[2]))
                    I.append(float(data[3]))
            except:
                counter = counter + 1
                for skip in range(2):
                    _ = f.readline()
        f.close()
        counter = counter + 1
        V = np.array(V)-E_ref
        I = np.array(I)*1000/area
        
        numcyc = counter
                
        scanrate = format(float(np.array(scanrate)), '.0f')
        
    return V, I, scanrate, numcyc
