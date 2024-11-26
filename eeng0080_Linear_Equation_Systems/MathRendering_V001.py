def Mat2MD(M, name="", idx="", fmt=""):
    '''
    2D numpy matrix to markdown code. 
    Generates a markdown string which can be rendered, e.g. by 
    IPython.display.display(Math(Mat2MD(M))).
    
    Parameters:
    M: 2D numpy array, the matrix
    name: matrix name to be used in the rendering, 
          e.g. name="A" renders to $A=...$
    idx: index of the matrix name, 
         e.g. idx="k" renders to $A_k=...$
    fmt: number format of the matrix elements, 
         e.g. fmt=".2f" print floating point format with 2 decimals.
    '''
    matrix_string = ""
    for r in M:
        if matrix_string: matrix_string += r" \\ "
#        fmt_string = f"{x}"
        matrix_string += " & ".join([f"{x:{fmt}}" for x in r])
    if name:
        if idx:
            Mstr = name + "_" + idx + "="
        else:
            Mstr = name + "="
    else:
        Mstr = ""

    return(Mstr + r"\begin{pmatrix}" + matrix_string + r"\end{pmatrix}")


def Vec2MD(v, name="", idx="", fmt=""):
    '''
    2D numpy matrix to markdown code. 
    Generates a markdown string which can be rendered, e.g. by 
    IPython.display.display(Math(Mat2MD(M))).
    
    Parameters:
    v: 1D numpy array, the vector
    name: matrix name to be used in the rendering, 
          e.g. name="v" renders to $v=...$
    idx: index of the matrix name, 
         e.g. idx="k" renders to $v_k=...$
    fmt: number format of the matrix elements, 
         e.g. fmt=".2f" print floating point format with 2 decimals.
    '''
    matrix_string = ""
    for x in v:
        if matrix_string: matrix_string += r" \\ "
#        fmt_string = f"{x}"
        matrix_string += f"{x:{fmt}}"
    if name:
        if idx:
            Mstr = name + "_" + idx + "="
        else:
            Mstr = name + "="
    else:
        Mstr = ""

    return(Mstr + r"\begin{pmatrix}" + matrix_string + r"\end{pmatrix}")


def Gauss2MD(M, name="", idx="", fmt="g"):
    '''
    2D numpy matrix to markdown code, output format for Gauß elimination.
    Generates a markdown string which can be rendered, e.g. by 
    IPython.display.display(Math(Gauss2MD(M))).
    
    Parameters:
    M: 2D numpy array, the matrix
    name: matrix name to be used in the rendering, 
          e.g. name="A" renders to $A=...$
    idx: index of the matrix name, 
         e.g. idx="k" renders to $A_k=...$
    fmt: number format of the matrix elements, 
         e.g. fmt=".2f" print floating point format with 2 decimals.
    '''
    matrix_string = ""
    for r in M:
#        if matrix_string: matrix_string += r" \\ "
        matrix_string += " & ".join([f"{x:{fmt}}" for x in r]) + r"\\"
    if name:
        if idx:
            Mstr = name + "_" + idx + "="
        else:
            Mstr = name + "="
    else:
        Mstr = ""
        
    (m,n) = M.shape
    fmt = "{"+(n-1)*"c"+"|"+"c"+"}"
    
    return(Mstr + r"\left(\begin{array}" + fmt + matrix_string + r"\end{array}\right)")

