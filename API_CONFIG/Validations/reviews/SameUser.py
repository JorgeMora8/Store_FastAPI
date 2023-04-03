#This function ensure that the author of the review is the 
#same that wants to delete it

from fastapi import HTTPException, status 

def sameUser(userOnReview, currentUser): 
    if userOnReview != currentUser: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not same user.")
