class DICTfactory:
    def __init__(self, obj):
        self.obj = obj

    def to_dict(self):
        return self._to_dict(self.obj)

    def _to_dict(self, obj):
        if isinstance(obj, (int, float, str, bool)):
            return obj
        elif isinstance(obj, list):
            return [self._to_dict(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: self._to_dict(value) for key, value in obj.items()}
        elif "text" in dir(obj):
            return obj.text
        else:
            res = {}
            for attr in dir(obj):
                if not attr.startswith("__") and attr != "to_dict" and attr != "name":
                    index = attr[1:] if attr.startswith("_") else attr
                    if not isinstance(getattr(obj, attr), str):
                        res[index] = self._to_dict(getattr(obj, attr))
                    else:
                        res[f"__{index}"] = self._to_dict(getattr(obj, attr))
                    
            return res
            # {attr: self._to_dict(getattr(obj, attr)) for attr in dir(obj) if (not attr.startswith('__') and attr != "to_dict" and attr != "name")}
            # data = {}
            # for attr in dir(obj):
            #     if not attr.startswith("__") and attr != "to_dict":
            #         print("Passato ", attr)
            #         elem = getattr(obj, attr)
            #         if isinstance(elem, (str, int, bool)):
            #             data[f"_{attr}"] = elem
            #         elif isinstance(elem, (list))
            #             data
                
