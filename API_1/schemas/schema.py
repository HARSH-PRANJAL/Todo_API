def individual_serial(todo)->dict:
    return{
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "status": todo["status"]
    }

def all_serial(todo)->list: 
    return [individual_serial(item) for item in todo]