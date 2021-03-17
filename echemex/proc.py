import numpy as np

def readcv(FILE, cycle, E_ref, area, quiet=False):
    
    if cycle == -1:
        full = 1
    else:
        cycle = cycle - 1
        full = 0
        
    with open(FILE, "r") as f:
        V = []
        I = []
        check = 0
        counter = 0

        for x in f:
            data = x.split()
            if check == 0:
                if len(data) == 0:
                    _ = 0
                elif data[0] =="SCANRATE":
                    scanrate = data[2]
                elif data[0] == "CYCLES":
                    numcyc = data[2]
                elif data[0] == "CURVE1":
                    _ = f.readline()
                    _ = f.readline()
                    check = 1
                else:
                    _ = 0

            elif check == 1:
                try:
                    float(data[0])
                    if (counter == cycle) or (full == 1):
                        V.append(float(data[2]))
                        I.append(float(data[3]))
                    else:
                        _ = 0
                except:
                    _ = f.readline()
                    _ = f.readline()
                    counter += 1

        f.close()
        V = np.array(V)-E_ref
        I = np.array(I)*1000/area
        
    if not quiet:
        if area == 1:
            print("Current is not normalized, units are mA")
        elif area != 1:
            print("Current is normalized to area, units are mA/cm^2")
        
        scanrate = format(float(np.array(scanrate)), '.0f')
    return V, I, scanrate, numcyc

def readeis(FILE, E_ref):
    # FILE - filepath to data
    # E_ref - reference electrode potential
    # Note: original .DTA files may not be encoded in a way that is compatible with this function
    #       duplicating the file into another blank .txt file and renaming .DTA fixes this issue
    check = 0
    with open(FILE, "r") as f:
        for s in range(10):
            _ = f.readline()

        time = []
        freq = []
        real = []
        imag = []
        delt = []
        volt = []
        
        for x in f:
            data = x.split()
            if check == 0:
                if data[0] == "ZCURVE":
                    _ = f.readline()
                    _ = f.readline()
                    check = 1
                else:
                    _ = 0
            try:
                float(data[0])
                if check == 1:
                    data = np.array(data)
                    time.append(float(data[1]))
                    freq.append(float(data[2]))
                    real.append(float(data[3]))
                    imag.append(float(data[4]))
                    delt.append(float(data[7]))
                    volt.append(float(data[9]))
            except:
                _ = 0
                
        f.close()
        
        time = np.array(time)
        freq = np.array(freq)
        real = np.array(real)
        imag = -np.array(imag)
        delt = -np.array(delt)*np.pi/180
        volt = np.array(volt)-E_ref
       
    return time, freq, real, imag, delt, volt

def randcirc(w,sigma,Rct,Ro,Cd):
    # used for fitting EIS data
    # scipy.optimize.curvefit can match this function to the raw data
    # given starting guesses sigma, Rct, Ro, and Cd
    
    Zf  = Rct + (sigma/np.sqrt(w))
    Zre = Ro + Zf/(1+(Zf**2)*(w**2)*(Cd**2))
    return Zre

def readca(FILE, E_ref, area, quiet=False):
    
    time = []
    potential = []
    current = []
    counter = 0
    
    with open(FILE, "r") as f:
        
        for x in f:
            data = x.split()
            data = np.array(data)
            
            try:
                float(data[0])
                time.append(float(data[1]))
                potential.append(float(data[2]))
                current.append(float(data[3]))
            except:
                if data.shape == (0,):
                    _ = []
                elif data[0] == "CURVE":
                    for skip in range(2):
                        _ = f.readline()
                    counter = counter + 1
                    
        f.close()
        
        time = np.array(time)
        potential = np.array(potential)-E_ref
        current = np.array(current)*1000/area        
        
    if not quiet:
        if area == 1:
            print("Current is not normalized, units are mA")
        elif area != 1:
            print("Current is normalized to area, units are mA/cm^2")
            
    return time, potential, current

def readcp(FILE, E_ref, quiet=False):
    
    with open(FILE, "r") as f:
        for s in range(62):
            _ = f.readline()
                    
        V = []
        I = []
        t = []
        counter = 0;
        full = 0;
        
        for x in f:
            data = x.split()
            data = np.array(data)
            
            try:
                float(data[0])
                V.append(float(data[2]))
                I.append(float(data[3]))
                t.append(float(data[1]))
            except:
                for skip in range(2):
                    _ = f.readline()
        f.close()
        V = np.array(V)-E_ref
        I = np.array(I)*10**3
        t = np.array(t)
    
    if not quiet:
        print("Current is not normalized, units are mA")
        
    return t, V, I
