import world_sentiment as world
from pytest import approx

def check_avg_score:
  assert world.generate_average_sentiment_score == average_score;
def check_score:
  assert world.first_score == world.generate_average_sentiment_score(first_thing)
  assert world.second_score == world.generate_average_sentiment_score(second_thing)

 def check_greater:
  assert world.if(first_score>second_score):
      print(f"The humanity prefers {first_thing} over {second_thing}")
 else:
      print(f"The humanity prefers {second_thing} over {first_thing}")
