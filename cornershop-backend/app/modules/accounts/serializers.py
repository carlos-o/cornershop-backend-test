from rest_framework import serializers


class UserSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    last_login = serializers.DateTimeField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    is_active = serializers.BooleanField()

