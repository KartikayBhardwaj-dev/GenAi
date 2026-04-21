import json

def validate_and_clean(text: str):
    try:
        data = json.loads(text)
        # name
        name = data.get("name")
        if name is not None and not isinstance(name, str):
            return False, "Invalid type for name", None
        
        # Experience Years
        exp = data.get("experience_years")
        if exp is not None and isinstance(exp, str):
            if exp.isdigit():
                exp = int(exp)
            else:
                return False, "Invalid experience_years", None
        elif not isinstance(exp, int):
            return False, "Invalid experience_years", None
        
        # Tech Stack
        tech = data.get("tech_stack")
        if tech is None:
            tech = []
        elif isinstance(tech, list):
            tech = [str(x) for x in tech if x is not None]
        else:
            return False, "Invalid tech_stack", None
        
        # Role
        role = data.get("role")
        if role is not None and not isinstance(role, str):
            return False, "Invalid role", None
        
        cleaned = {
            "name": name,
            "experience_years": exp,
            "tech_stack": tech,
            "role": role
        }

        return True, None, cleaned
    
    except Exception as e:
        return False, f"JSON error: {str(e)}", None
