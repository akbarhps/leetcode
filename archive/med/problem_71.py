path = "/home/user/Documents/../Pictures"
# path = "/home//foo/"
# path = "/../"
# path = "/.../a/../b/c/../d/./"

def simplifyPath(path: str) -> str:
    pathSplitted = path.split('/')    
    
    output = []
    for i, item in enumerate(pathSplitted): 
        if item in ['', '.']:
            continue
        elif item == '..':
            if len(output) > 0: output.pop()
            continue
            
        output.append(item) 
        print(output)
        
    print(output)
    return f'/{'/'.join(output)}' if len(output) else '/'


print(simplifyPath(path))