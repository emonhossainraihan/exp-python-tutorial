## [Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names)


dict_component = {
    "type": "register",
    "number": "10-232-1213",
    "manufacturer": "honnai",
}

print(dict_component["type"])


class attrdict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

component = attrdict({
    "type": "register",
    "number": "10-232-1213",
    "manufacturer": "honnai",
})


print(f"{component.type =}")
print(f"{component.number =}")
print(f"{component.manufacturer =}")
