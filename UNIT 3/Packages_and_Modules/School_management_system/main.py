from student.add_student import add_student
from teacher.add_teacher import add_teacher
from utilities.logger import logger

logger("Application started")
add_student("Aarav" , "10th Grade")
add_teacher("Mr.Rudra" , "Mathematics")
logger("Application ended")