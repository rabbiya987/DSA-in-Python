class hashmap:
    
    def __init__(self,size):
        self.size=size
        self.hashmap=self.create_buckets()

    #Create buckets of given size
    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    def hashing(self,key,size):
        return hash(key) % self.size

    #Creating a function to add values
    def insert(self, key, val):
        #Get index from key 
        hashed_key=self.hashing(key,self.size)

        #Get to the corresponding bucket
        bucket=self.hashmap[hashed_key]
        found_key= False
        for index,record in enumerate(bucket):
            record_key,record_value=record #unpacking the record tuple
            #Check if key already exist
            if record_key==key:
                found_key=True
                break
        if found_key:
                bucket[index]=(key,val)
        else:
                bucket.append((key,val))

    def get(self,key):
        #Get index from key 
        hashed_key=self.hashing(key,self.size)
        #Get the bucket
        bucket=self.hashmap[hashed_key]

        foundkey=False
        for index,record in enumerate(bucket):
            record_key,record_value=record

             #Check if key already exist
            if record_key==key:
                found_key=True
                break

            # If the bucket has same key as the key being searched,Return the value found
            if found_key:
                return record_value
            else:
                return "no records"
        

    def delete(self,key):
        #Get index from key 
        hashed_key=self.hashing(key,self.size)
        #Get the bucket
        bucket=self.hashmap[hashed_key]

        found_key=False
        for index,record in enumerate(bucket):
            record_key,record_value=record

             #Check if key already exist
            if record_key==key:
                found_key=True
                break

        if found_key:
            bucket.pop(index)
        
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hashmap)
    

hash_map=hashmap(10)

hash_map.insert(1,'rabia')
hash_map.insert(2,'ammara')
print(hash_map)
print(hash_map.get('rabia'))
hash_map.delete(1)
print(hash_map)


    
    

    
        
   
    





