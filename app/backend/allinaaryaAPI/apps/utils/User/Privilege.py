import enum

# Describes all privileges with description.
# Should be in sync with privileges stored in database (table: feature_role_privilege).

class Privilege(enum.Enum):
    TEST_PRIVILEGE = "testing purpose"
    TEST_PRIVILEGE2 = "testing purpose2"
