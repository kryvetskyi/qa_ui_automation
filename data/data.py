from dataclasses import dataclass


@dataclass
class Person:
    full_name: str
    email: str
    cur_addr: str
    permanent_addr: str
