import json

def validate_schema(text: str):
    try:
        data = json.loads(text)

        # name
        if not isinstance(data.get("name"), str):
            return False, "Invalid or missing 'name'", None

        # skills
        if not isinstance(data.get("skills"), list):
            return False, "Invalid or missing 'skills'", None

        # experience
        exp = data.get("experience_years")
        if not (isinstance(exp, int) or exp is None):
            return False, "Invalid 'experience_years'", None

        return True, None, data

    except Exception as e:
        return False, f"JSON error: {str(e)}", None