from typing import Optional


class User:   
            
    #private variable to get unique id for books 
    # - need figure it out concurrency issue later
    _id_counter = 0    
    
    user_id: int
    name: str
    
    #for later replaced by google login
    user_name: Optional[str] = None
    password: Optional[int] = None
    
    #normal or admin
    status: Optional[str] = None
    
       
    
    
    
    def __init__(self, name) -> None:
        self.name = name
        self.user_id = User._get_next_id()
  
     
     
     
     
     
     
    ###################################################################################    
    #private function to get unique id for books 
    # - need figure it out concurrency issue later
    @classmethod
    def _get_next_id(cls):
        cls._id_counter += 1
        return cls._id_counter
        
    #helpper function
    #getters
        
    def get_user_id(self):
        return self.user_id
    
    def get_name(self):
        return self.name
    
    def get_user_name(self):
        return self.user_name
    
    def get_password(self):
        return self.password
        
    def get_status(self):
        return self.status 

    
    #setters
    def set_name(self, name):
        self.name = name
    
    def set_user_name(self, user_name):
        self.user_name = user_name
        
    def set_password(self, password):
        self.password = password
        
    def set_status(self, status):
        self.status = status
    
    
    
###############################################################
#test
###############################################################

p1 = User("peter")
p2 = User("Tom")


print(p1.get_name())
print(p1.get_user_id())

print(p2.get_name())
print(p2.get_user_id())