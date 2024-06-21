from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson, Subscription
from lms.validators import LinkValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkValidator(field="link_to_video")]


class CourseDetailSerializer(ModelSerializer):
    count_lessons_course = SerializerMethodField()
    lessons_titles = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    is_active_subscription = SerializerMethodField(read_only=True)

    def get_count_lessons_course(self, course):
        return course.lesson_set.count()

    def get_lessons_titles(self, course):
        return [lesson.title for lesson in Lesson.objects.filter(course=course)]

    def get_is_active_subscription(self, course):
        if course.subscriptions.filter(user=self.context["request"].user).exists():
            return True
        return False

    class Meta:
        model = Course
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
