from project.player import Player

p = Player("Pall", 3, 3, 3, 3)
print(str(p))
result = str(p).strip()
print(result)

print(f"Player: Pall\nSprint: 3\nDribble: 3\nPassing: 3\nShooting: 3")