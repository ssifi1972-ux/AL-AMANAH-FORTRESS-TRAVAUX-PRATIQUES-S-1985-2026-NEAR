# AL-AMANAH FORTRESS - 19 chars - Title المسجل
# Cadenas Renaissance - Hifz al-Mal
# Built by SIFI BOUKHARI - Batna 1985 → 2026

class Guardian:
    def __init__(self, ar, en, mission):
        self.ar = ar; self.en = en; self.mission = mission

VIGILANT = Guardian("النبيه", "The Vigilant", "VIGILANCE")
STEWARD = Guardian("القائد", "The Steward", "Leadership")

class AlAmanahFortress:
    def audit(self, code: str):
        is_vuln = "transfer" in code and "insert" in code and code.find("transfer") < code.find("insert")
        if is_vuln:
            print("🔒 Cadenas LOCKED by The Vigilant - VIGILANCE - FROZEN")
            return "FROZEN"
        else:
            print("🔓 RELEASED by The Steward - Sarfuhu fi Mawdi'ihi")
            return "RELEASED"

# Demo
fortress = AlAmanahFortress()
vuln = "Promise::new(user.clone()).transfer(amount.0); self.balances.insert(&user, &(balance - amount.0));"
fixed = "self.balances.insert(&user, &(balance - amount.0)); Promise::new(user.clone()).transfer(amount.0);"

print("TEST 1 VULNERABLE:")
fortress.audit(vuln)
print("\nTEST 2 FIXED:")
fortress.audit(fixed)
