# bounce.py
#
# Exercise 1.5

ball_height = 100.0
BOUNCE_RATE = 0.6

for i in range(10):
    ball_height = ball_height * BOUNCE_RATE
    print(f"Ball bounced back to {round(ball_height,4)}")
