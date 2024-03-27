def solution(new_id):
    new_id = new_id.lower()
    
    id = ""
    for c in new_id:
        if c.isalnum() or c in ['-','_','.']:
            id += c
    
    #주의
    while ".." in id:
        id = id.replace("..",".")
    
    id = id.strip(".")
    
    if len(id)==0:
        id = "a"
        
    if len(id)>=16:
        id = id[:15]
        id = id.rstrip(".")
            
    if len(id)==1:
        id = id*3
    elif len(id)==2:
        id = id[0]+id[1]*2
    
    return id