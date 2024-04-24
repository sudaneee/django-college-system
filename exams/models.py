from django.db import models


# Create your models here.

class ExamResult(models.Model):
    student = models.CharField(max_length=100)
    session = models.ForeignKey("core.Session", on_delete=models.CASCADE)
    semester = models.ForeignKey("core.Semester", on_delete=models.CASCADE)
    course = models.ForeignKey("core.Course", on_delete=models.CASCADE)
    ca = models.IntegerField(default=0)
    exams = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.session} {self.semester} {self.course.course_code} Result for {self.student}'
    
    @property
    def total(self):
        return self.ca + self.exams

    @property
    def grade(self):
        total = self.ca + self.exams
        if total >= 70:
            return "A"
        elif total >= 60:
            return "B"
        elif total >= 50:
            return "C"
        elif total >= 45:
            return "D"
        elif total >= 40:
            return "E"
        else:
            return "F"  # Assuming below 40 is a fail

