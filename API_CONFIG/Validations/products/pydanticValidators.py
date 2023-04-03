from fastapi import HTTPException, status

def emptySpace(cls, value, attribute): 
    if len(value) <= 0: 
        raise ValueError(f"The space {attribute} cant be empty")
    return value
    
def noQuanity(cls, value, attribute): 
    if value <= 0: 
        raise ValueError(f"The space {attribute} cant be 0 or less")
    return value