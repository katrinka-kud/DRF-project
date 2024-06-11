from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lessons_course = SerializerMethodField()
    lessons_titles = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_count_lessons_course(self, course):
        return course.lesson_set.count()

    def get_lessons_titles(self, course):
        return [lesson.title for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "description",
            "count_lessons_course",
            "lessons",
            "lessons_titles",
        )


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
