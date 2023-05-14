class Cars:
    def __init__(self,marka,model,year,ob,color,type,price):
        self.marka = marka
        self.model = model
        self.year = year
        self.ob = ob
        self.color = color
        self.type = type
        self.price = price

from search_name import search_object

class CreateMixin:
    
    def _get_or_set_objects_and_id(self):
        try:
            self.id
            self.objects
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0
            
    def init(self) -> None:
        self._get_or_set_objects_and_id()     
    
    def post(self, **kwargs):
        self.id += 1
        obj = dict(id=self.id, **kwargs)
        self.objects.append(obj)
        return {'status': '201 created', 'msg': obj}
    
class ListingMixin:
    def list_(self):
        res = [{'id': obj['id'], 'marka': obj['marka'], 'date_of_issue': obj['date_of_issue'], 'engine_capacity': obj['engine_capacity'], 'color': obj['color'], 'body_type': obj['body_type'], 'mileage': obj['mileage'], 'price': obj['price']} for obj in self.objects]
        return {'status': '200 OK', 'msg': res}

class RetriaveMixin:
    @search_object
    def retriave(self, id, **kwargs):
        obj = kwargs['object_']
        
        if obj:
            return {'status': '200 OK!', 'msg': obj}
        return {'status': '404 Not Found!'}  
    
class UpdateMixin:
    @search_object
    def patch(self, id, **kwargs):
        obj = kwargs.pop('object_')
        
        try:
            obj.update(**kwargs)
            return {'status': '200 OK!', 'msg': obj}
        except AttributeError:
            return {'status': '404 Not Found!'} 
        
class DeleteMixin:
    @search_object
    def delete_(self, id, **kwargs):
        obj = kwargs['object_']

        if obj:
            self.objects.remove(obj)
            return {'status': '204 No Content', 'msg': 'Deleted'}
        return {'status': '404 Not Found!'}