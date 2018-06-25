HOURS = r"^\s*(0?\d|1\d|2[0-4])\s*$"
HOURS_MINUTES = r"^\s*((0?\d|1\d|2[0-3]))(\s*|\s*\-\s*|\s*\:\s*)(0?\d|[1-5]\d)\s*$"
DATE = r"^(1[0-9]|2[0-9]|3[01]|0?[1-9])(?:\s*|\s*\.\s*)(1[012]|0?[1-9])?(?:\s*|\s*\.\s*)([0-9]{4}|[0-9]{2})?\s*$"

FULL_DATETIME = r"^\s*(1\d|2[0-3]|0?\d)" +\
                r"(?:\s*|\s*\-\s*|\s*\:\s*)" +\
                r"([1-5]\d|0?\d)?" +\
                r"(?:\s*)" +\
                r"(1[0-9]|2[0-9]|3[01]|0?[1-9])?" +\
                r"(?:\s*|\s*\.\s*)" +\
                r"(1[012]|0?[1-9])?" +\
                r"(?:\s*|\s*\.\s*)" +\
                r"([0-9]{4}|[0-9]{2})?\s*$"