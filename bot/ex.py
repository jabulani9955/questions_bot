from db.db import get_correct_answer
import pandas as pd

asns = get_correct_answer(question_id=1)

print(asns)