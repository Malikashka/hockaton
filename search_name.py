
def search_object(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        id = args[1]
        for product in self.objects:
            if product['id'] == id:
                kwargs.update(object_=product)
                return func(*args, **kwargs)
        kwargs.update(object_=None) 
         
        return func(*args, **kwargs)

    return wrapper

search_object