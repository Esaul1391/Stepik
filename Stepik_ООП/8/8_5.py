def add_attr_to_class(**attrs):
    def decorator(cls):
        for attr, value in attrs.items():
            setattr(cls, attr, value)
        return cls
    return decorator




# def track_instances(cls):
#     cls.instances = []
#
#     def new_init(self, *args, **kwargs):
#         cls.instances.append(self)
#         cls.__init_original__(self, *args, **kwargs)
#
#     cls.__init_original__ = cls.__init__
#     cls.__init__ = new_init
#     return cls

