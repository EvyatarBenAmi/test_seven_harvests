import csv
from sqlmodel import SQLModel

def sort_by_distance(list_soldier) -> list[dict]:
    distance_sorted = list_soldier.sort(key = "distance")
    return distance_sorted

# class Soldier(SQLModel, table = True):
    persnal_num : int 
    first_name : str 
    last_name : str 
    gender : str 
    city : str 
    distance : int 
    placement_status : str 