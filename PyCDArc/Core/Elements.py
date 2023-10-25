"""CDA Component Utils"""
from .Exceptions import InvalidGivenValue, InvalidGivenSubelementData, InvalidNullFlavor


class Attribute:
    """ XML Attributes Class """

    def __new__(cls, name: str, data: dict, required: bool = False, fixed: str = '', default: str | None = '', nullable: bool = False) -> str | None:
        try:
            if not fixed:
                return data[name]
            else:
                return data[name] if data[name] == fixed else default
                # return data[name]
        except Exception as error:
            if nullable and "nullFlavor" not in data:
                raise InvalidNullFlavor(f"{name} is nullable but not nullFlavor was given")
            elif required and not default and not nullable:
                raise InvalidGivenValue(f"Something went wrong generating {name}") from error
            elif default:
                return default
            return None


class Component:
    """ XML Component Class """

    def __new__(cls, class_name: type, name: str, data: dict, required: bool = False, as_list: bool = True, nullFlavored: bool = False):
        try:
            if isinstance(data[name], list):
                for sub in data[name]:
                    if "nullFlavor" in sub and not nullFlavored:
                        raise InvalidNullFlavor(f"NullFlavor is given for {name} of type {class_name.__name__} but is not allowed")
            else:
                if "nullFlavor" in data[name] and not nullFlavored:
                    raise InvalidNullFlavor(f"NullFlavor is given for {name} of type {class_name.__name__} but is not allowed")

            if isinstance(data[name], dict):
                return class_name(name, data[name])
            elif isinstance(data[name], list) and as_list:
                return [class_name(name, elem) for elem in data[name]]
            else:
                if as_list:
                    raise InvalidGivenSubelementData(f"{name} of type {class_name.__name__} can't be listed")
                else:
                    raise InvalidGivenSubelementData(f"{name} of type {class_name.__name__} must be dict or list")
        except Exception as error:
            if required:
                raise InvalidGivenSubelementData(f"Something went wrong generating {name} of type {class_name.__name__}") from error
            return None
