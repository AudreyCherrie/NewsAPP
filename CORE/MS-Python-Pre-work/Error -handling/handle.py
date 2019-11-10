def get_age():
    print("How old are you")
    try:
      age = int(input())
      return age
    except ValueError:
      return "That was not a valid input"