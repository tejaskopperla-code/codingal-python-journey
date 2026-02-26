import random
import string
from typing import Final, List

class SecurityTerminal:
    """A system designed to test a subject's pattern recognition or luck."""
    
    def __init__(self, difficulty: int = 4) -> None:
        
        self.__target_pool: Final[str] = string.ascii_lowercase  
        self.__target: str = "".join(random.choice(self.__target_pool) for _ in range(difficulty))
        self.attempts_remaining: int = 5
        self.is_unlocked: bool = False

    def verify_guess(self, guess: str) -> bool:
        """Compares the subject's input against the hidden target."""
        if guess == self.__target:
            self.is_unlocked = True
            return True
        
        self.attempts_remaining -= 1
        return False

    def get_hint(self) -> str:
        """Provides the length of the target to the subject."""
        return f"Target length: {len(self.__target)} | Pool: Lowercase alphabets only."



def run_test() -> None:
    
    terminal = SecurityTerminal(difficulty=3)
    
    print("--- WHITE ROOM SECURITY CHALLENGE ---")
    print(terminal.get_hint())

    while terminal.attempts_remaining > 0 and not terminal.is_unlocked:
        
        user_input: str = input(f"\nAttempts remaining ({terminal.attempts_remaining}). Enter guess: ").lower().strip()
        
        if terminal.verify_guess(user_input):
            print("\n[SUCCESS] Access Granted. Identity verified.")
        else:
            if terminal.attempts_remaining > 0:
                print("[DENIED] Incorrect sequence. Retrying...")
            else:
                print(f"\n[TERMINATED] Lockout engaged. The target was: {terminal._SecurityTerminal__target}")

if __name__ == "__main__":
    run_test()