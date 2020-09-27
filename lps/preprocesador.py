import numpy as np

words = [
    'Parar',
    'Cargar',
    'CargarValor',
    'Almacenar',
    'SaltarSiCero',
    'SaltarSiNeg',
    'SaltarSiPos',
    'SaltarSiDes',
    'Saltar',
    'Copiar',
    'Sumar',
    'Restar',
    'Mult',
    'Div',
    'imprimir'
]

words_params = {
    'Parar': [],
    'Cargar': [1, 0],
    'CargarValor': [1, 0],
    'Almacenar': [1, 0],
    'SaltarSiCero': [0],
    'SaltarSiNeg': [0],
    'SaltarSiPos': [0],
    'SaltarSiDes': [0],
    'Saltar': [0],
    'Copiar': [1, 1],
    'Sumar': [1, 1],
    'Restar': [1, 1],
    'Mult': [1, 1],
    'Div': [1, 1],
    'imprimir': [0]
}


def procesar(file):
    code = [line for line in open("test.pim") if line.strip() != ""]

    memory = np.empty(1024, dtype=np.uint16)

    for i, x in enumerate(code):
        line = x.split()

        if len(line) > 2:
            print("Error en:'", x, "'en la linea:", i + 1)
            return -1

        instr = line[0]

        if instr == words[0]:
            memory[i] = 4096
            continue

        params = line[1].split(sep = ',')

        if instr not in words:
            print("No se reconoce el comando:'", instr, "'en la linea:", i + 1)
            return -1

        params_dt = words_params.get(instr)
        
        num_params = len(params_dt)

        if len(params) != num_params:
            print("Se esperan ", num_params, "parametros y se encontraron", len(params), ". Error en: ", x, "en la linea:", i + 1)
            return -1

        y = (words.index(instr) + 1) * 4096

        for j, param_t in enumerate(params_dt):
            params[j] = int(params[j])
            if param_t == 1:
                if params[j] > 3:
                    print("No existe el registro:", params[j], ". Error en: ", x, "en la linea:", i + 1)
                    return -1

                y += (1024 * params[j])
            elif param_t == 0:
                if params[j] > 1023:
                    print("Solo hay 1024 direcciones de memoria [0 - 1023], se encontro:", params[j], ". Error en: ", x, "en la linea:", i + 1)
                    return -1

                y += params[j]


        memory[i] = y    

    return memory